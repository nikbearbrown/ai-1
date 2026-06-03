#!/usr/bin/env python3
"""build-react-site.py — compile a book's markdown source into a Next.js-ready
site scaffold: one .mdx content file per chapter plus the .tsx page components
that render them.

This is the React-site path from Chapter 18 of AI+1. Pure Python (standard
library) to generate the scaffold; Node/Next.js to build and deploy it — that
last step is the developer's, not the author's. The author runs this script,
gets a working folder structure, and hands it off.

What it reads:  chapters/*.md + metadata.yaml
What it writes (under --out, default ./site):
  content/<slug>.mdx              chapter body as MDX (markdown + room for JSX)
  app/page.tsx                    home page: the table of contents
  app/<slug>/page.tsx             one route per chapter, imports the MDX
  app/layout.tsx                  shell + chapter nav
  components/AskAI.tsx            placeholder for the embedded Ask-AI panel (Ch 20)
  package.json, next.config.mjs, tsconfig.json, mdx-components.tsx

The author never hand-writes .mdx or .tsx. This script scaffolds them; the
source of truth stays chapters/*.md.

Usage:
  python3 build-react-site.py
  python3 build-react-site.py --out site
"""

import argparse
import json
import os
import re


def read_title(source_dir):
    p = os.path.join(source_dir, "metadata.yaml")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            m = re.match(r'^title:\s*(.+)$', line.strip())
            if m:
                return m.group(1).strip().strip('"\'')
    return "Book"


def chapter_title(md, fallback):
    for line in md.split("\n"):
        m = re.match(r'^#\s+(.*)$', line)
        if m:
            return m.group(1).strip()
    return fallback


def mdx_escape(md):
    """MDX parses {...} and <...> as JSX. Neutralize bare braces so prose that
    contains { or } does not break the parser. Code fences are left alone."""
    out, in_fence = [], False
    for line in md.split("\n"):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
        else:
            out.append(line.replace("{", "&#123;").replace("}", "&#125;"))
    return "\n".join(out)


def slug_of(fname):
    return os.path.splitext(os.path.basename(fname))[0]


def build(source_dir, out_dir):
    chapters_dir = os.path.join(source_dir, "chapters")
    if not os.path.isdir(chapters_dir):
        raise SystemExit(f"error: no chapters/ under {source_dir!r}")
    book = read_title(source_dir)

    files = sorted(f for f in os.listdir(chapters_dir) if f.endswith(".md"))
    chapters = []
    for f in files:
        md = open(os.path.join(chapters_dir, f), encoding="utf-8").read()
        if not md.strip():
            continue
        slug = slug_of(f)
        chapters.append({"slug": slug, "title": chapter_title(md, slug), "md": md})

    def mk(path, content):
        full = os.path.join(out_dir, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(content)

    written = []

    # content/*.mdx
    for ch in chapters:
        mk(f"content/{ch['slug']}.mdx", mdx_escape(ch["md"]) + "\n")
        written.append(f"content/{ch['slug']}.mdx")

    # app/<slug>/page.tsx
    for ch in chapters:
        comp = "".join(p.capitalize() for p in re.split(r'[^A-Za-z0-9]+', ch["slug"]) if p)
        page = (
            f'import Content from "@/content/{ch["slug"]}.mdx";\n'
            f'import AskAI from "@/components/AskAI";\n\n'
            f'export const metadata = {{ title: {json.dumps(ch["title"])} }};\n\n'
            f'export default function {comp}Page() {{\n'
            f'  return (\n'
            f'    <article className="prose">\n'
            f'      <Content />\n'
            f'      <AskAI chapter={json.dumps(ch["slug"])} />\n'
            f'    </article>\n'
            f'  );\n'
            f'}}\n'
        )
        mk(f"app/{ch['slug']}/page.tsx", page)
        written.append(f"app/{ch['slug']}/page.tsx")

    # app/page.tsx (table of contents)
    links = "\n".join(
        f'        <li><a href={json.dumps("/" + ch["slug"])}>{ch["title"]}</a></li>'
        for ch in chapters)
    mk("app/page.tsx",
        f'export default function Home() {{\n'
        f'  return (\n'
        f'    <main>\n'
        f'      <h1>{book}</h1>\n'
        f'      <ul>\n{links}\n      </ul>\n'
        f'    </main>\n'
        f'  );\n'
        f'}}\n')
    written.append("app/page.tsx")

    # app/layout.tsx
    mk("app/layout.tsx",
        'import type { ReactNode } from "react";\n\n'
        f'export const metadata = {{ title: {json.dumps(book)} }};\n\n'
        'export default function RootLayout({ children }: { children: ReactNode }) {\n'
        '  return (\n'
        '    <html lang="en">\n'
        '      <body>{children}</body>\n'
        '    </html>\n'
        '  );\n'
        '}\n')
    written.append("app/layout.tsx")

    # components/AskAI.tsx — placeholder for the embedded model (Chapter 20)
    mk("components/AskAI.tsx",
        '"use client";\n'
        'import { useState } from "react";\n\n'
        '// Placeholder for the embedded Ask-AI loop (Chapter 20).\n'
        '// Wire this to your model endpoint; keep it a human+AI loop, not a\n'
        '// one-shot answer box. The system prompt spec lives in Appendix 97.\n'
        'export default function AskAI({ chapter }: { chapter: string }) {\n'
        '  const [q, setQ] = useState("");\n'
        '  return (\n'
        '    <aside className="ask-ai" data-chapter={chapter}>\n'
        '      <label>Ask about this chapter</label>\n'
        '      <input value={q} onChange={(e) => setQ(e.target.value)} />\n'
        '    </aside>\n'
        '  );\n'
        '}\n')
    written.append("components/AskAI.tsx")

    # mdx-components.tsx (required by @next/mdx app router)
    mk("mdx-components.tsx",
        'import type { MDXComponents } from "mdx/types";\n\n'
        'export function useMDXComponents(components: MDXComponents): MDXComponents {\n'
        '  return { ...components };\n'
        '}\n')
    written.append("mdx-components.tsx")

    # next.config.mjs
    mk("next.config.mjs",
        'import createMDX from "@next/mdx";\n\n'
        'const withMDX = createMDX({});\n\n'
        '/** @type {import("next").NextConfig} */\n'
        'const nextConfig = { pageExtensions: ["ts", "tsx", "md", "mdx"] };\n\n'
        'export default withMDX(nextConfig);\n')
    written.append("next.config.mjs")

    # tsconfig.json
    mk("tsconfig.json", json.dumps({
        "compilerOptions": {
            "target": "ES2020", "lib": ["dom", "dom.iterable", "ES2020"],
            "allowJs": True, "skipLibCheck": True, "strict": True,
            "noEmit": True, "esModuleInterop": True, "module": "esnext",
            "moduleResolution": "bundler", "resolveJsonModule": True,
            "isolatedModules": True, "jsx": "preserve", "incremental": True,
            "paths": {"@/*": ["./*"]}},
        "include": ["**/*.ts", "**/*.tsx", "**/*.mdx", "next-env.d.ts"],
        "exclude": ["node_modules"]}, indent=2) + "\n")
    written.append("tsconfig.json")

    # package.json
    mk("package.json", json.dumps({
        "name": re.sub(r'[^a-z0-9-]+', '-', book.lower()).strip("-") or "book-site",
        "private": True, "version": "0.1.0",
        "scripts": {"dev": "next dev", "build": "next build", "start": "next start"},
        "dependencies": {
            "next": "^14.2.0", "react": "^18.3.0", "react-dom": "^18.3.0",
            "@next/mdx": "^14.2.0", "@mdx-js/loader": "^3.0.0",
            "@mdx-js/react": "^3.0.0", "@types/mdx": "^2.0.0"},
        "devDependencies": {
            "typescript": "^5.4.0", "@types/node": "^20.0.0",
            "@types/react": "^18.3.0", "@types/react-dom": "^18.3.0"}},
        indent=2) + "\n")
    written.append("package.json")

    print(f"Scaffolded: {out_dir}")
    print(f"  book        : {book}")
    print(f"  chapters    : {len(chapters)}")
    print(f"  files       : {len(written)}")
    print(f"  next steps  : cd {out_dir} && npm install && npm run dev  (developer's step)")
    return written


def main():
    ap = argparse.ArgumentParser(description="Scaffold a Next.js site from book markdown.")
    ap.add_argument("--source-dir", default=".")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    out = args.out or os.path.join(args.source_dir, "site")
    build(args.source_dir, out)


if __name__ == "__main__":
    main()
