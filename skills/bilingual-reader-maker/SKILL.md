---
name: bilingual-reader-maker
description: Use when the user asks to make bilingual reading materials, bilingual PDFs, Chinese-English study editions, mobile-readable HTML/PDF readers, or to turn an English PDF/article into a polished bilingual reader.
license: CC-BY-NC-SA-4.0
---

<!-- workbuddy-install: pending; slug: bilingual-reader-maker -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`bilingual-reader-maker`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `bilingual-reader-maker`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/bilingual-reader-maker/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `bilingual-reader-maker` 后安装；界面文字可能随 WorkBuddy 版本变化。

# Bilingual Reader Maker

Produce polished bilingual reading materials from English source PDFs or long articles.

Default output:

- Real-text HTML for editing, copying, searching, parsing, and mobile reading.
- PDF exported from that HTML for sharing.
- English source paragraph first, Simplified Chinese translation immediately below.

## Workspace

Create one project folder per source:

```text
<workspace>/<semantic-slug>/
├── source/          # source PDF/article/assets, preserve originals
├── intermediate/    # extracted text, translation cache, page samples
├── output/          # final HTML/PDF and copied assets
├── qa/              # screenshots/thumbnails/render checks
└── scripts/         # project-specific generation scripts
```

If the user already has a project folder, work inside it. Do not create duplicates.

## Production Standard

- Preserve the source's visual identity where appropriate: cover, chapter art, color palette, logos, icons, and typographic mood.
- Do not force the original layout if it hurts learning. For phone-friendly reading, prefer normal single-column flow.
- Structure each reading unit as:
  1. English source paragraph
  2. Chinese translation
  3. Light divider
- Use real text HTML, not a screenshot-only artifact.
- Export PDF from the HTML using Chrome headless when available.
- Add attribution only if the user wants it. Keep it subtle and place it in a final colophon, not on the cover.

Suggested colophon pattern:

```text
This bilingual study edition was prepared for learning, reading, and discussion.
Prepared by: <name or organization>
```

For Chinese-facing editions:

```text
本中英双语学习版基于原英文材料整理制作，仅用于学习、阅读与交流。
整理制作：<name or organization>
```

Avoid aggressive calls to follow, QR codes, sales language, or cover branding unless explicitly requested.

## Workflow

1. Bootstrap:
   - Locate source file(s) and project folder.
   - Preserve the original source file.
   - Check for local project instructions such as `AGENTS.md` or `CLAUDE.md`.

2. Extract and inspect:
   - Extract text with `pypdf` first.
   - If text extraction is poor, render pages and consider OCR.
   - Render representative original pages into `qa/original/` to inspect real colors, cover, chapter art, icons, and layout.

3. Translate:
   - Translate by coherent paragraph/segment, not whole-page blobs.
   - Preserve the English source text.
   - Keep a translation cache in `intermediate/translation_cache.json`.
   - Verify there are no missing translations, empty translations, or placeholder strings.

4. Design HTML:
   - Use original visual assets for cover/chapter pages when possible and legally appropriate.
   - Use single-column mobile-readable body layout by default.
   - Use calm editorial typography: serif for English headings/body when it fits; readable Chinese fonts for translation.
   - Keep the HTML source clear enough to modify later.

5. Export and QA:
   - Export PDF from HTML.
   - Capture screenshots for cover, table of contents, a chapter/section page, a body page, and one narrow mobile viewport.
   - Check for horizontal overflow, clipped text, missing assets, old copy, missing translations, and unreadable density.
   - Open/reveal final artifacts or provide direct paths/links.

## Useful Commands

Chrome PDF export:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-sandbox \
  --print-to-pdf="$PDF" --print-to-pdf-no-header "$HTML_URL"
```

Phone-width screenshot:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-sandbox \
  --window-size=430,1200 --screenshot="$SHOT" "$HTML_URL"
```

## Naming

Use descriptive output names:

- `<source>_bilingual-mobile-reader.html`
- `<source>_bilingual-mobile-reader.pdf`

For Chinese-facing editions:

- `<source>_中英双语移动阅读版.html`
- `<source>_中英双语移动阅读版.pdf`
