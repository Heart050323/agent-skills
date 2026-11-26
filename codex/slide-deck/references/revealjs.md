# reveal.js

ブラウザーで発表するHTMLスライド。コードの段階表示、発表者ノート、順番を見せる動きが必要なときに使う。確認した版: reveal.js 6.0.2（2026-11-26）。

## 雛形

CDNを使う場合は版を固定する。v6でプラグインの場所が `dist/plugin/<名前>.js` に変わったので、古い記事の `plugin/notes/notes.js` は使わない。

```html
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>資料名</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@6.0.2/dist/reset.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@6.0.2/dist/reveal.css">
  <link rel="stylesheet" href="deck.css">
</head>
<body>
  <div class="reveal"><div class="slides">

    <section>
      <p class="chapter">1｜現状</p>
      <h1>社員の46%が、会社の認めていないAIツールを業務で使ったことがある</h1>
      <img src="charts/unapproved-use.svg" alt="未承認AIツールの利用経験の内訳">
      <p class="source">出典: 社内アンケート（2026年10月、n=842）</p>
      <aside class="notes">回答者の部門内訳は【要確認】</aside>
    </section>

  </div></div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@6.0.2/dist/reveal.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@6.0.2/dist/plugin/notes.js"></script>
  <script>
    Reveal.initialize({
      width: 1920, height: 1080, margin: 0,
      center: false, hash: true, slideNumber: 'c/t',
      transition: 'none', backgroundTransition: 'none',
      plugins: [RevealNotes]
    });
  </script>
</body>
</html>
```

- 組み込みテーマ（black / moon / sky など）は使わず、`deck.css` に色の役割と書体を変数で定義する（[marp.md](marp.md)のテーマ例と同じ考え方で、セレクターを `.reveal` 配下にする）。
- ページの切り替え効果は `none` を基本にする。
- 手元で開くときは `file://` ではなく簡易サーバー（`python3 -m http.server`）で配信する。外部ネットワークなしで発表する場合は、npmで入れた reveal.js をプロジェクト内に置いて相対パスで読む。

## 機能は理由があるときだけ

- **段階表示（fragment）**: 論理の順番（前提→問題→結論）や、図の要素を1つずつ足して説明するときだけ。全ページの箇条書きを1行ずつ出す使い方はしない。

  ```html
  <li class="fragment">前提</li>
  ```

- **コードの行ハイライト**: highlightプラグイン（`dist/plugin/highlight.js` と `dist/plugin/highlight/monokai.css` など）を読み込み、`plugins: [RevealNotes, RevealHighlight]` に加える。

  ```html
  <pre><code class="language-python" data-trim data-line-numbers="1|3-4">...</code></pre>
  ```

- **発表者ノート**: `<aside class="notes">`。Sキーで発表者画面。
- **縦方向のページ（入れ子のsection）**: 補足資料を本筋から外して置くときだけ。PDFでは順に並ぶので、配布時の順番を確かめる。
- **背景**: `data-background-color` は、表紙・章の扉・締めなど背景を変える理由があるページだけ。グラデーション背景は使わない。

## PDF化と点検

1. 簡易サーバーで開いたURLに `?print-pdf` を付けてChromeで開き、印刷→PDFに保存（横向き、余白なし、背景のグラフィックを有効）。発表者ノートも印刷するなら `showNotes: true`（別ページなら `'separate-page'`）。
2. ヘッドレスで自動化する場合は、ヘッドレスブラウザー（Playwright等）で `?print-pdf` のページをPDF化する。
3. PDFをPNGにして、SKILL.mdの点検に回す。段階表示のページは、PDFでは最終状態になることを確かめる。
