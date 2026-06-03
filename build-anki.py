#!/usr/bin/env python3
"""build-anki.py — compile a book's spaced-repetition layer into an Anki
deck (.apkg).

This is the spaced-repetition path from Chapter 16 of AI+1. Pure Python,
standard library only (sqlite3 + zipfile). It reads recall cards authored in
the same markdown source that produces the EPUB and the Canvas course, and
writes a .apkg the reader double-clicks to import into Anki.

Card source (two accepted forms, both plain markdown):
  1. A dedicated cards directory (default: recall/*.md)
  2. A "## Recall" or "## Spaced Repetition" section inside any chapter file
Each card is a Q/A pair:

    Q: What does imsmanifest.xml do in a Common Cartridge package?
    A: It is the course index — it tells the LMS what resources exist
       and how they are organized.

Blank line separates cards. One deck per book; one note type (Basic, two
fields). The .apkg is a ZIP containing:
  - collection.anki2   a SQLite database (Anki schema 11)
  - media              a JSON manifest ("{}" when there are no images)

What it does NOT do: it does not open Anki or sync. The reader imports the
file. Confirming the import is the reader's step, exactly like the Canvas
upload in Chapter 17.

Usage:
  python3 build-anki.py
  python3 build-anki.py --cards-dir recall --chapters-dir chapters --out output/ai+1.apkg
"""

import argparse
import hashlib
import json
import os
import re
import sqlite3
import time
import zipfile

# Anki "Basic" note type and a single deck. IDs are fixed-but-arbitrary
# (millisecond timestamps in real Anki; constants here for reproducibility).
MODEL_ID = 1607392319000
DECK_ID = 1607392319001


def read_metadata_title(source_dir):
    path = os.path.join(source_dir, "metadata.yaml")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r'^title:\s*(.+)$', line.strip())
                if m:
                    return m.group(1).strip().strip('"\'')
    return os.path.basename(os.path.abspath(source_dir))


# --------------------------------------------------------------------------
# Card extraction
# --------------------------------------------------------------------------
def parse_qa(text):
    """Yield (front, back) from a block of Q:/A: lines."""
    cards = []
    q, a = None, None
    mode = None
    for raw in text.split("\n"):
        line = raw.rstrip()
        mq = re.match(r'^\s*Q:\s*(.*)$', line)
        ma = re.match(r'^\s*A:\s*(.*)$', line)
        if mq:
            if q is not None and a is not None:
                cards.append((q.strip(), a.strip()))
            q, a, mode = mq.group(1), None, "q"
        elif ma:
            a, mode = ma.group(1), "a"
        elif not line.strip():
            if q is not None and a is not None:
                cards.append((q.strip(), a.strip()))
                q, a, mode = None, None, None
        else:
            if mode == "q":
                q = (q + " " + line.strip()).strip()
            elif mode == "a":
                a = (a + " " + line.strip()).strip()
    if q is not None and a is not None:
        cards.append((q.strip(), a.strip()))
    return cards


def collect_cards(cards_dir, chapters_dir):
    cards = []
    if cards_dir and os.path.isdir(cards_dir):
        for fn in sorted(os.listdir(cards_dir)):
            if fn.endswith(".md"):
                with open(os.path.join(cards_dir, fn), encoding="utf-8") as fh:
                    cards.extend(parse_qa(fh.read()))
    if chapters_dir and os.path.isdir(chapters_dir):
        for fn in sorted(os.listdir(chapters_dir)):
            if not fn.endswith(".md"):
                continue
            with open(os.path.join(chapters_dir, fn), encoding="utf-8") as fh:
                md = fh.read()
            m = re.search(
                r'^#{1,4}\s+(?:Recall|Spaced[ -]?Repetition)\b.*?$',
                md, re.IGNORECASE | re.MULTILINE)
            if m:
                # take to next heading of same-or-higher level, or EOF
                rest = md[m.end():]
                nxt = re.search(r'^#{1,4}\s', rest, re.MULTILINE)
                section = rest[:nxt.start()] if nxt else rest
                cards.extend(parse_qa(section))
    return cards


# --------------------------------------------------------------------------
# Anki collection schema (schema version 11)
# --------------------------------------------------------------------------
def guid(front, back):
    return hashlib.sha1((front + "\x1f" + back).encode("utf-8")).hexdigest()[:10]


def build_collection(db_path, deck_name, cards):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.executescript("""
    CREATE TABLE col (id integer primary key, crt integer, mod integer,
        scm integer, ver integer, dty integer, usn integer, ls integer,
        conf text, models text, decks text, dconf text, tags text);
    CREATE TABLE notes (id integer primary key, guid text, mid integer,
        mod integer, usn integer, tags text, flds text, sfld text,
        csum integer, flags integer, data text);
    CREATE TABLE cards (id integer primary key, nid integer, did integer,
        ord integer, mod integer, usn integer, type integer, queue integer,
        due integer, ivl integer, factor integer, reps integer, lapses integer,
        left integer, odue integer, odid integer, flags integer, data text);
    CREATE TABLE revlog (id integer primary key, cid integer, usn integer,
        ease integer, ivl integer, lastIvl integer, factor integer,
        time integer, type integer);
    CREATE TABLE graves (usn integer, oid integer, type integer);
    CREATE INDEX ix_notes_usn on notes (usn);
    CREATE INDEX ix_cards_usn on cards (usn);
    CREATE INDEX ix_cards_nid on cards (nid);
    CREATE INDEX ix_cards_sched on cards (did, queue, due);
    CREATE INDEX ix_revlog_cid on revlog (cid);
    CREATE INDEX ix_revlog_usn on revlog (usn);
    """)

    now = int(time.time())
    now_ms = now * 1000

    models = {str(MODEL_ID): {
        "id": MODEL_ID, "name": "Basic (AI+1)", "type": 0, "mod": now,
        "usn": -1, "sortf": 0, "did": DECK_ID, "tmpls": [{
            "name": "Card 1", "ord": 0,
            "qfmt": "{{Front}}",
            "afmt": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}",
            "bqfmt": "", "bafmt": "", "did": None}],
        "flds": [
            {"name": "Front", "ord": 0, "sticky": False, "rtl": False,
             "font": "Arial", "size": 20, "media": []},
            {"name": "Back", "ord": 1, "sticky": False, "rtl": False,
             "font": "Arial", "size": 20, "media": []}],
        "css": ".card{font-family:arial;font-size:20px;text-align:left;color:#111;background:#fff;}",
        "latexPre": "", "latexPost": "", "latexsvg": False, "req": [[0, "any", [0]]],
        "tags": [], "vers": []}}

    decks = {
        "1": {"id": 1, "name": "Default", "mod": now, "usn": -1,
              "lrnToday": [0, 0], "revToday": [0, 0], "newToday": [0, 0],
              "timeToday": [0, 0], "conf": 1, "desc": "", "dyn": 0,
              "collapsed": False, "extendNew": 10, "extendRev": 50},
        str(DECK_ID): {"id": DECK_ID, "name": deck_name, "mod": now, "usn": -1,
              "lrnToday": [0, 0], "revToday": [0, 0], "newToday": [0, 0],
              "timeToday": [0, 0], "conf": 1, "desc": "", "dyn": 0,
              "collapsed": False, "extendNew": 10, "extendRev": 50}}

    dconf = {"1": {"id": 1, "name": "Default", "mod": 0, "usn": 0, "maxTaken": 60,
        "autoplay": True, "timer": 0, "replayq": True,
        "new": {"bury": False, "delays": [1, 10], "initialFactor": 2500,
                "ints": [1, 4, 0], "order": 1, "perDay": 20, "separate": True},
        "rev": {"bury": False, "ease4": 1.3, "ivlFct": 1, "maxIvl": 36500,
                "perDay": 200, "hardFactor": 1.2},
        "lapse": {"delays": [10], "leechAction": 1, "leechFails": 8,
                  "minInt": 1, "mult": 0},
        "dyn": False}}

    conf = {"nextPos": 1, "estTimes": True, "activeDecks": [1], "sortType": "noteFld",
            "timeLim": 0, "sortBackwards": False, "addToCur": True, "curDeck": DECK_ID,
            "newSpread": 0, "dueCounts": True, "curModel": str(MODEL_ID),
            "collapseTime": 1200}

    c.execute("INSERT INTO col VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (
        1, now, now_ms, now_ms, 11, 0, 0, 0,
        json.dumps(conf), json.dumps(models), json.dumps(decks),
        json.dumps(dconf), json.dumps("{}" )))

    nid = now_ms
    cid = now_ms
    for i, (front, back) in enumerate(cards):
        g = guid(front, back)
        flds = front + "\x1f" + back
        sfld = front
        csum = int(hashlib.sha1(sfld.encode("utf-8")).hexdigest()[:8], 16)
        c.execute("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)", (
            nid + i, g, MODEL_ID, now, -1, "", flds, sfld, csum, 0, ""))
        c.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            cid + i, nid + i, DECK_ID, 0, now, -1, 0, 0, i + 1,
            0, 0, 0, 0, 0, 0, 0, 0, ""))

    conn.commit()
    conn.close()


def build(source_dir, out_path, cards_dir, chapters_dir):
    deck_name = read_metadata_title(source_dir)
    cards = collect_cards(cards_dir, chapters_dir)
    if not cards:
        raise SystemExit(
            "error: no recall cards found. Add recall/*.md (Q:/A: pairs) or a "
            "'## Recall' section to a chapter.")

    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    tmp_db = out_path + ".collection.anki2"
    if os.path.exists(tmp_db):
        os.remove(tmp_db)
    build_collection(tmp_db, deck_name, cards)

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(tmp_db, "collection.anki2")
        zf.writestr("media", "{}")
    os.remove(tmp_db)

    print(f"Built: {out_path}")
    print(f"  deck  : {deck_name}")
    print(f"  cards : {len(cards)}")
    print(f"  note  : Basic (Front/Back), Anki schema 11")
    return out_path, len(cards)


def main():
    ap = argparse.ArgumentParser(description="Build an Anki .apkg from a book's recall layer.")
    ap.add_argument("--source-dir", default=".")
    ap.add_argument("--cards-dir", default=None, help="dir of Q:/A: markdown (default: <source>/recall)")
    ap.add_argument("--chapters-dir", default=None, help="also scan chapters for ## Recall sections")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cards_dir = args.cards_dir or os.path.join(args.source_dir, "recall")
    chapters_dir = args.chapters_dir or os.path.join(args.source_dir, "chapters")
    out = args.out
    if out is None:
        slug = re.sub(r'[^A-Za-z0-9._+-]+', '-', read_metadata_title(args.source_dir)).strip("-").lower()
        out = os.path.join(args.source_dir, "output", f"{slug or 'deck'}.apkg")

    build(args.source_dir, out, cards_dir, chapters_dir)


if __name__ == "__main__":
    main()
