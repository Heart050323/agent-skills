---
name: md-slides
description: Create slide decks from Markdown with Marp, exporting to PDF, PPTX, or HTML. Use when the user wants slides generated from notes, an outline, or existing Markdown, needs a PDF/PPTX deck file, or says Markdownからスライド/ピッチデッキ作って. For interactive web presentations, use html-slides instead.
license: MIT
metadata:
  short-description: Markdown to slides via Marp
  author: claude-office-skills
---

# Markdown Slides Skill

## Overview

This skill enables creation of presentations from pure Markdown using **Marp**. Write slides in familiar Markdown syntax and export to PDF, PPTX, or HTML with professional themes.

## Delivery checks

Use the project’s existing toolchain where available. Verify installed versions and current official documentation before installing dependencies or relying on an export option. Do not assume an office MCP server exists. Follow required approval before downloading or executing a new CLI.

Open the rendered deck or exported PDF to check text overflow, images, fonts, and navigation/page order. A source file alone does not establish that an export succeeded. For PPTX, verify whether the chosen exporter produces editable content or slide images and report that limitation. Preserve an editable source alongside the requested export.

## How to Use

1. Write or provide Markdown content
2. I'll format it for Marp with proper directives
3. Export to your preferred format (PDF/PPTX/HTML)

**Example prompts:**
- "Convert my notes to a presentation"
- "Create slides from this markdown"
- "Build a pitch deck using markdown"
- "Generate PDF slides from this outline"

## Domain Knowledge

### Basic Syntax

```markdown
---
marp: true
---

# First Slide

Content here

---

# Second Slide

- Bullet 1
- Bullet 2
```

### Themes

```markdown
---
marp: true
theme: default  # default, gaia, uncover
---
```

### Directives

```markdown
---
marp: true
theme: gaia
class: lead        # Centered title
paginate: true     # Page numbers
header: 'Header'   # Header text
footer: 'Footer'   # Footer text
backgroundColor: #fff
---
```

### Images

```markdown
![width:500px](image.png)
![bg](background.jpg)
![bg left:40%](sidebar.jpg)
```

### Columns

```markdown
<div class="columns">
<div>

## Left

Content

</div>
<div>

## Right

Content

</div>
</div>
```

## Example

```markdown
---
marp: true
theme: gaia
paginate: true
---

<!-- _class: lead -->

# Project Update

Q4 2024 Review

---

# Highlights

- Revenue: +25%
- Users: +50%
- NPS: 72

---

# Roadmap

| Q1 | Q2 | Q3 | Q4 |
|----|----|----|-----|
| MVP | Beta | Launch | Scale |

---

<!-- _class: lead -->

# Thank You!

questions@company.com
```

## CLI Usage

```bash
# Install
npm install -g @marp-team/marp-cli

# Convert
marp slides.md -o presentation.pdf
marp slides.md -o presentation.pptx
marp slides.md -o presentation.html
```

## Resources

- [Marp Documentation](https://marp.app/)
- [GitHub](https://github.com/marp-team/marp)
