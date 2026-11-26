# Marp

Markdownから16:9のスライドを作り、PDF・PNG・PPTX・HTMLに書き出す。確認した版: Marp CLI 4.5.1（2026-11-26）。

## 準備

- 手元に `marp` があればそれを使う。なければ `npx @marp-team/marp-cli@4.5.1` で版を固定して実行する（初回にパッケージを取得するので、そのことを伝える）。
- 書き出しにはChrome・Edge・Firefoxのいずれかが必要。見つからないときは `--browser-path` で指定する。

## テーマを1か所で定義する

既定テーマ（default / gaia / uncover）の見た目に頼らず、資料用のテーマCSSを作る。色の役割と書体はここにだけ書く。

```css
/* @theme deck */
@import 'default';

:root {
  --ink: #2b2f36;      /* 本文 */
  --muted: #6b7078;    /* 補助・出典 */
  --accent: #1f4e79;   /* 決めた対象にだけ使う */
  --rule: #d9dce1;
}
section {
  width: 1920px; height: 1080px;   /* スライドの大きさはここで決まる */
  position: relative;
  display: flex; flex-direction: column; justify-content: flex-start;
  padding: 96px 120px;
  background: #fff; color: var(--ink);
  font-family: "Hiragino Sans", "Noto Sans JP", sans-serif;
  font-size: 30px; line-height: 1.6;
}
section .chapter { font-size: 22px; color: var(--muted); margin: 0; }
section h1 { font-size: 46px; line-height: 1.35; margin: 8px 0 40px; }
section .source { position: absolute; left: 120px; bottom: 48px; font-size: 18px; color: var(--muted); }
section .accent { color: var(--accent); font-weight: 700; }
section .split { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; }
section.divider { justify-content: center; }
```

- 大きさはテーマの `section` の `width`/`height` で決める。front-matterの `size:` は使わない（読み込んだ既定テーマの寸法に戻ることがある）。
- 2段組みなどの部品は、使う前にテーマに定義する（未定義のクラス名を書いても効かない）。
- 色の値は例。決めた色の役割に置き換える。
- テーマファイルは `--theme deck.css` で読み込む。1ファイルで済ませたいときはMarkdownのfront-matterの `style:` に書いてもよい。

## ページの書き方

```markdown
---
marp: true
theme: deck
paginate: true
---

<p class="chapter">1｜現状</p>

# 社員の46%が、会社の認めていないAIツールを業務で使ったことがある

![w:1400](charts/unapproved-use.svg)

<p class="source">出典: 社内アンケート（2026年10月、n=842）</p>

<!-- 発表者ノート: 回答者の部門内訳は【要確認】 -->

---

<!-- _class: divider -->

# 問うべきは、生成AIを安全に全社へ広げる方法である
```

- `---` でページを区切る。1ページ1主張。タイトルは章名＋主張の1文。
- `<!-- _class: ... -->` はそのページだけ、`<!-- class: ... -->` は以降すべてに効く。
- 画像は `![w:1200](...)`、背景画像は `![bg right:40%](...)`。写真は自社の実写だけ（SKILL.mdの資料の種類に従う）。
- グラフは別に作ったSVG/PNGを貼る。Marp内でグラフを描かない。強調色はタイトルの主張を示す部分だけ。
- 発表者ノートはHTMLコメントに書く。
- Markdown内でHTMLタグ（上の `<p class>` など）を使うので、書き出し時に `--html` を付ける。

## 書き出し

```bash
marp deck.md --theme deck.css --html --allow-local-files --pdf -o deck.pdf
marp deck.md --theme deck.css --html --allow-local-files --images png   # 点検用
marp deck.md --theme deck.css --html --allow-local-files --pptx -o deck.pptx
```

- `--allow-local-files` は手元の画像を読むため。自分で作ったMarkdownにだけ使う。
- `--pptx` の各ページは画像で、PowerPointで文字を直せない。受け取った人が直す必要があると伝えられていれば、そのことを伝えるか、編集可能なPPTXを別の方法で作る。
- `--pptx --pptx-editable` は実験機能。LibreOffice Impressが必要で、複雑なCSSでは失敗したり崩れたりする。使った場合は必ずPowerPointかLibreOfficeで開いて確かめる。
- 発表者ノートは `--notes` でテキストに、`--pdf-notes` でPDFの注釈にできる。
