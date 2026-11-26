# 出典

確認日: 2026-11-26（Asia/Tokyo）

- 鈴木奨平「AI資料の『全部盛り』を防ぐプロンプト」 https://x.com/pote_con/status/2124493679280926937
  - 1スライド1メッセージ、結論を示すタイトル、事実・解釈・提案・判断事項の区別、作る前に構成案を示して承認を得る手順、最後に自分で厳しくレビューする手順を参考にした。
- ふじくるり「スライドの『AIっぽさ』を極限まで言語化してみた」 https://x.com/fujikururi/status/2124420544498184356
  - AIっぽさの原因を「見ずに作る・ルールを形だけ満たす・1枚ずつ作る」とする整理、禁止ではなく「代わりに何をするか」を書く方針、資料の種類で大きな数字・写真・1文ページの扱いを変える考え方、作る前に種類・色の役割・ページの強さを宣言させる工程、画像に書き出して点検する工程を参考にした。

## 扱い

両投稿の考え方を参考に、文面はこのスキル用に書き直した。プロンプト本文の転載ではない。記事で有料公開されているプロンプト全文と、近日公開予定とされるスキル（IR-onetone-deck）は参照していない。記事中の企業名を挙げた事例は載せていない。

## 出力形式の資料

旧`md-slides`（Marp）と旧`html-slides`（reveal.js）をこのスキルに統合した（2026-11-26）。旧版の作例は名詞だけのタイトル、箇条書き中心、グラデーション背景、古いreveal.js 4のパスを含んでいたため引き継がず、以下の一次資料を確認して書き直した。旧版はGit履歴から復元できる。

- Marp CLI 4.5.1 のREADME（npm `@marp-team/marp-cli`）: `--images`、`--pptx`、実験機能の`--pptx-editable`（LibreOffice Impressが必要）、`--allow-local-files`、`--notes`、`--pdf-notes`、`--browser-path`
- reveal.js 6.0.2（npm / jsDelivr）と6.0.0のリリースノート: プラグインの場所が`dist/plugin/<名前>.js`に変更、`RevealNotes`・`RevealHighlight`
- https://revealjs.com/pdf-export/ : `?print-pdf`による印刷、`showNotes`
