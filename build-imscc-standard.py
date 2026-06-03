#!/usr/bin/env python3
"""build-imscc-standard.py — compile a book's markdown source into a
portable IMS Common Cartridge 1.3 (.imscc) package.

This is the STANDARD path described in Chapter 13 of AI+1: pure Python,
no dependencies beyond the standard library, conservative Common Cartridge
that imports into Canvas, Moodle, Blackboard, and Brightspace without
modification.

It reads the same source that produces the EPUB:
  - metadata.yaml         (title, author, rights, ...)
  - chapters/*.md         (one chapter -> one module + one page)
  - TIKTOC.md  (optional) (used only to confirm the module order)

It writes:
  - <slug>.imscc          a ZIP containing imsmanifest.xml + web pages
                          + assignment/discussion shells for chapter exercises

What it deliberately does NOT do:
  - It does not call the Canvas API. The professor uploads one file:
    Settings -> Import Course Content -> Common Cartridge 1.x Package.
  - It does not write Canvas-flavored trigger files
    (course_settings/syllabus.html, course_settings/course_settings.xml).
    Those belong to the Canvas-optimized path, not the portable one.

Usage:
  python3 build-imscc-standard.py
  python3 build-imscc-standard.py --source-dir . --out output/ai+1.imscc
"""

import argparse
import html
import os
import re
import sys
import uuid
import zipfile
from xml.sax.saxutils import escape as xml_escape

CC_NS = "http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1"
LOM_MANIFEST_NS = "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/manifest"
LOM_RESOURCE_NS = "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/resource"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
SCHEMA_LOCATION = (
    "http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1 "
    "http://www.imsglobal.org/profile/cc/ccv1p3/ccv1p3_imscp_v1p2_v1p0.xsd"
)


# --------------------------------------------------------------------------
# Source reading
# --------------------------------------------------------------------------
def read_metadata(path):
    """Tiny YAML reader for the flat key: value metadata.yaml. No PyYAML."""
    meta = {}
    if not os.path.exists(path):
        return meta
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.strip() in ("---", "..."):
                continue
            m = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                    val = val[1:-1]
                meta[key] = val
    return meta


def chapter_number(filename):
    m = re.match(r'^(\d+)', os.path.basename(filename))
    return int(m.group(1)) if m else 9999


def collect_chapters(chapters_dir):
    """Return ordered (filename, path) for content chapters only.

    Numbering convention in this book:
      00          front matter / introduction  -> 'Start Here' module
      01-79       teaching chapters            -> one module each
      80-98       appendices                   -> 'Appendices' module pages
      99          back matter                  -> 'Back Matter' module
    """
    files = sorted(
        (f for f in os.listdir(chapters_dir) if f.endswith(".md")),
        key=chapter_number,
    )
    return [(f, os.path.join(chapters_dir, f)) for f in files]


def classify(num):
    if num == 0:
        return "front"
    if 1 <= num <= 79:
        return "chapter"
    if 80 <= num <= 98:
        return "appendix"
    return "back"


# --------------------------------------------------------------------------
# Minimal Markdown -> HTML (stdlib only; covers the subset this book uses)
# --------------------------------------------------------------------------
def md_inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def md_to_html(md, title):
    lines = md.split("\n")
    out = []
    i = 0
    in_code = False
    code_buf = []
    para_buf = []
    list_buf = []
    list_type = None

    def flush_para():
        if para_buf:
            out.append("<p>" + md_inline(" ".join(para_buf).strip()) + "</p>")
            para_buf.clear()

    def flush_list():
        nonlocal list_type
        if list_buf:
            tag = list_type
            out.append(f"<{tag}>")
            out.extend(f"<li>{md_inline(item)}</li>" for item in list_buf)
            out.append(f"</{tag}>")
            list_buf.clear()
            list_type = None

    while i < len(lines):
        line = lines[i]
        fence = line.strip().startswith("```")
        if fence:
            if not in_code:
                flush_para(); flush_list()
                in_code = True
                code_buf = []
            else:
                out.append("<pre><code>" +
                           html.escape("\n".join(code_buf), quote=False) +
                           "</code></pre>")
                in_code = False
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        if not line.strip():
            flush_para(); flush_list()
            i += 1
            continue

        h = re.match(r'^(#{1,6})\s+(.*)$', line)
        if h:
            flush_para(); flush_list()
            level = len(h.group(1))
            out.append(f"<h{level}>{md_inline(h.group(2).strip())}</h{level}>")
            i += 1
            continue

        ul = re.match(r'^[-*+]\s+(.*)$', line)
        ol = re.match(r'^\d+\.\s+(.*)$', line)
        if ul or ol:
            flush_para()
            this_type = "ul" if ul else "ol"
            if list_type and list_type != this_type:
                flush_list()
            list_type = this_type
            list_buf.append((ul or ol).group(1).strip())
            i += 1
            continue

        if re.match(r'^[-_*]{3,}\s*$', line):
            flush_para(); flush_list()
            out.append("<hr/>")
            i += 1
            continue

        flush_list()
        para_buf.append(line.strip())
        i += 1

    flush_para(); flush_list()
    body = "\n".join(out)
    return (
        "<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\"/>"
        f"<title>{html.escape(title)}</title></head>\n<body>\n{body}\n</body></html>\n"
    )


def extract_title(md, fallback):
    for line in md.split("\n"):
        h = re.match(r'^#\s+(.*)$', line)
        if h:
            return h.group(1).strip()
    return fallback


def find_exercises(md):
    """Detect an exercises section and return its raw markdown, or None.

    Produces assignment shells, not graded items: the standard cartridge
    carries the prompt; Bloom levels and points stay in the Blueprint.
    """
    m = re.search(
        r'^#{1,4}\s+(?:Assessable\s+)?Exercises?\b.*?$',
        md, re.IGNORECASE | re.MULTILINE,
    )
    if not m:
        return None
    return md[m.start():].strip()


# --------------------------------------------------------------------------
# Common Cartridge manifest
# --------------------------------------------------------------------------
def new_id(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def build_manifest(course_title, modules):
    """modules: list of dicts {title, items:[{title, resource_id}]}"""
    org_items = []
    for mod in modules:
        item_xml = []
        for it in mod["items"]:
            item_xml.append(
                f'        <item identifier="{new_id("item")}" '
                f'identifierref="{it["resource_id"]}">\n'
                f'          <title>{xml_escape(it["title"])}</title>\n'
                f'        </item>'
            )
        org_items.append(
            f'      <item identifier="{new_id("module")}">\n'
            f'        <title>{xml_escape(mod["title"])}</title>\n'
            + "\n".join(item_xml) +
            f'\n      </item>'
        )

    resources_xml = []
    for mod in modules:
        for it in mod["items"]:
            resources_xml.append(
                f'    <resource identifier="{it["resource_id"]}" '
                f'type="webcontent" href="{it["href"]}">\n'
                f'      <file href="{it["href"]}"/>\n'
                f'    </resource>'
            )

    manifest_id = new_id("manifest")
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{manifest_id}"
  xmlns="{CC_NS}"
  xmlns:lomimscc="{LOM_MANIFEST_NS}"
  xmlns:lom="{LOM_RESOURCE_NS}"
  xmlns:xsi="{XSI_NS}"
  xsi:schemaLocation="{SCHEMA_LOCATION}">
  <metadata>
    <schema>IMS Common Cartridge</schema>
    <schemaversion>1.3.0</schemaversion>
    <lomimscc:lom>
      <lomimscc:general>
        <lomimscc:title>
          <lomimscc:string>{xml_escape(course_title)}</lomimscc:string>
        </lomimscc:title>
      </lomimscc:general>
    </lomimscc:lom>
  </metadata>
  <organizations>
    <organization identifier="{new_id("org")}" structure="rooted-hierarchy">
      <item identifier="{new_id("root")}">
{chr(10).join(org_items)}
      </item>
    </organization>
  </organizations>
  <resources>
{chr(10).join(resources_xml)}
  </resources>
</manifest>
'''


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------
def build(source_dir, out_path, tiktoc=None):
    chapters_dir = os.path.join(source_dir, "chapters")
    if not os.path.isdir(chapters_dir):
        sys.exit(f"error: no chapters/ directory under {source_dir!r}")

    meta = read_metadata(os.path.join(source_dir, "metadata.yaml"))
    course_title = meta.get("title", os.path.basename(os.path.abspath(source_dir)))

    files = collect_chapters(chapters_dir)
    if not files:
        sys.exit(f"error: no .md files in {chapters_dir!r}")

    # group files into named modules
    group_titles = {
        "front": "Start Here",
        "appendix": "Appendices",
        "back": "Back Matter",
    }
    modules = []          # one module per teaching chapter; grouped for others
    grouped = {}          # kind -> module dict
    package_files = {}    # arcname -> bytes

    for fname, path in files:
        num = chapter_number(fname)
        kind = classify(num)
        with open(path, encoding="utf-8") as fh:
            md = fh.read()
        if not md.strip():
            continue  # skip empty stubs
        title = extract_title(md, fname)
        slug = os.path.splitext(fname)[0]
        page_href = f"web_resources/{slug}.html"
        package_files[page_href] = md_to_html(md, title).encode("utf-8")
        page_res = new_id("res")

        items = [{"title": title, "resource_id": page_res, "href": page_href}]

        # chapter exercises -> a discussion/assignment shell page
        if kind == "chapter":
            ex = find_exercises(md)
            if ex:
                ex_href = f"web_resources/{slug}-exercises.html"
                package_files[ex_href] = md_to_html(
                    ex, f"{title} — Exercises").encode("utf-8")
                ex_res = new_id("res")
                items.append({
                    "title": f"{title} — Exercises",
                    "resource_id": ex_res, "href": ex_href,
                })

        if kind == "chapter":
            modules.append({"title": title, "items": items})
        else:
            g = grouped.setdefault(kind, {"title": group_titles[kind], "items": []})
            g["items"].extend(items)

    # assemble final module order: front, chapters (already in order), appendices, back
    ordered = []
    if "front" in grouped:
        ordered.append(grouped["front"])
    ordered.extend(modules)
    if "appendix" in grouped:
        ordered.append(grouped["appendix"])
    if "back" in grouped:
        ordered.append(grouped["back"])

    manifest = build_manifest(course_title, ordered)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("imsmanifest.xml", manifest)
        for arcname, data in package_files.items():
            zf.writestr(arcname, data)

    n_pages = len(package_files)
    n_modules = len(ordered)
    print(f"Built: {out_path}")
    print(f"  course title : {course_title}")
    print(f"  modules      : {n_modules}")
    print(f"  web pages    : {n_pages}")
    print(f"  manifest     : imsmanifest.xml (Common Cartridge 1.3.0)")
    return out_path


def main():
    ap = argparse.ArgumentParser(description="Build a portable .imscc Common Cartridge from book markdown.")
    ap.add_argument("--source-dir", default=".", help="book root (contains chapters/ and metadata.yaml)")
    ap.add_argument("--out", default=None, help="output .imscc path")
    ap.add_argument("--tiktoc", default=None, help="optional TIKTOC.md for module-order confirmation")
    args = ap.parse_args()

    out = args.out
    if out is None:
        meta = read_metadata(os.path.join(args.source_dir, "metadata.yaml"))
        slug = re.sub(r'[^A-Za-z0-9._+-]+', '-', meta.get("title", "course")).strip("-").lower()
        out = os.path.join(args.source_dir, "output", f"{slug or 'course'}.imscc")

    build(args.source_dir, out, tiktoc=args.tiktoc)


if __name__ == "__main__":
    main()
