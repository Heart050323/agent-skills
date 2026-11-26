# agent-skills

Claude / Codex 用の個人スキル集。`claude/` と `codex/` に各ホスト向けの24種類を管理しています。導入と同期は [SETUP.md](SETUP.md) を参照してください。標準の skill-creator などは同梱しません。

## 整理後の使い方

| 以前のスキル | 現在の扱い |
| --- | --- |
| adaptive-effort | token-efficiency のモデル・労力比較リファレンスへ統合 |
| output-check-fix-loop | output-checker の修正モードへ統合 |
| citation-verification | verify-citations に一本化。BibTeX形式検査は導入済みの latex-paper-en の補助を利用 |
| full-output-enforcement | 削除。依頼された成果物の完了条件で判断 |
| writing-great-skills | 削除。各ホストの標準creatorを利用 |

デザイン系のスキルは用途別の選択肢です。すべてを同時に適用したり、好みを一般的な品質要件として強制したりしません。削除前の内容はGit履歴から復元できます。

## 参考例からのUI実装

`reference-driven-ui` はLucian UX/UIのカタログやTakayu Motion Referenceから、用途に合う参考例を選び、既存の配色・状態・操作へ移植するスキルです。例: 「$reference-driven-ui で、商品一覧の並び替えに合う動きを探して実装して」。参照先は必要時に読み、外部のインストーラーを実行する前提にはしません。


## 資料・Web実装・原典調査

以下は上流のライセンスを保持して目的を絞った改変版です。第三者のCLIやスクリプトは同梱せず、必要な資料を参照する構成にしています。出典・参照コミット・変更点は各スキルの`references/sources.md`に記録しています。

| スキル | 使いどころ | 既存スキルとの分担 |
| --- | --- | --- |
| `natural-slides` | 太線・図解・大きな数字を使う日本語の営業資料・提案書 | デザイン方針を担当。reveal.jsは`html-slides`、Marpは`md-slides` |
| `modern-web-guidance` | Web標準、フォームのIME、dialog、コンテナークエリ、互換性の確認 | UIの作風ではなく、実装と対応ブラウザーの判断 |
| `imozuru` | 用語・人・引用から原典へたどる分野調査 | 探索を担当。既存文献の書誌・引用形式の点検は`verify-citations` |

例: 「$natural-slidesでこの提案を図解中心に」「$modern-web-guidanceで日本語入力時の誤送信を直して」「$imozuruでこの分野の原典を調べて」。この登録では定期監視は開始されません。

## デザインの方向づけ・仕上げ・テスト（2026-11-26追加）

X投稿で紹介されたスキルを既存のデザイン系と比較し、役割が重ならないものだけを入れました。出典・参照コミット・変更点は各スキルの`references/sources.md`にあります。

| スキル | 使いどころ | 既存スキルとの分担 |
| --- | --- | --- |
| `frontend-design` | 新しい画面・ページの見た目の方針を決める（Anthropic公式、原文＋日本語組版の補足） | LPの作風は`design-taste-frontend`、既存画面の改修は`redesign-existing-projects` |
| `make-interfaces-feel-better` | 角丸・影・数字・アイコン・出入りの動きなど細部の仕上げ | ジェスチャーとスプリングは`apple-design` |
| `canvas-design` | ポスター・告知画像・アート作品のPNG/PDF（Anthropic公式を日本語の告知物向けに改変） | note画像は`note-image`、スライドは`natural-slides`など |
| `test-techniques` | 「ちゃんとテストして」を境界値分析・状態遷移など技法名に分解して実施 | 成果物のレビューは`output-checker` |

例: 「$frontend-designでこのページの方針を決めて」「$make-interfaces-feel-betterでこの画面を仕上げて」「$canvas-designでセミナー告知を作って」「$test-techniquesで公開前のテストを計画して」。
