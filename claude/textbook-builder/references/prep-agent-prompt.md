# 準備エージェントへの共通依頼文

各科目の依頼では「このファイルを読んで従え + 科目名・資料フォルダ・出力先・科目固有の注意」だけを渡す。

---

あなたは大学の科目の教科書(LuaLaTeX、出版水準、100 ページ超)を作るための**準備作業**だけを担当する。**本文(chapters/*.tex)は書かない**。

## 読むもの
- スキル: `~/.claude/skills/textbook-builder/SKILL.md`(手順 1〜2、「資料が少ない科目」「効率化のパターン」)、`templates/STYLE.md`、`scripts/`
- 形式の手本(完成例): `/Volumes/ESD-EPB/EEIC Drive/ナレッジまとめ/電力システム工学第二/` の outline.md・notes/notes-sources.md・notes/notes-exams.md・work/agent-prompt-common.txt・STYLE.md §7・PROGRESS.md

## やること
1. `python3 ~/.claude/skills/textbook-builder/scripts/inventory.py "<資料>" "<出力>/work/inventory.md"`、`bash ~/.claude/skills/textbook-builder/scripts/extract.sh "<出力>/work/extracted" <全PDF>`。zip は `<出力>/work/src-zip/<zip名>/` に展開して読む(中のスクリプトは実行しない)。文字の少ない・式が崩れる・手書きのページは `pdftoppm -r 60` で work/pages/ に画像化して Read(式は必要に応じて 150 dpi で取り直す)。同じ資料の重複コピー(「〜のコピー」フォルダなど)は md5 で確かめて読み飛ばす。別科目の資料が紛れ込んでいたら使わず、返答で報告する
2. `notes/notes-sources.md`: 全資料の「ページ → 話題」対応表(★ = 図にする候補)。年度で範囲が違えば最新年度を軸にし、差を表にする。資料の誤り・疑わしい数値は末尾の節に
3. `notes/notes-exams.md`: 過去問・レポート・小テストを自分で全部読み、全設問(要約でなく設問ごと)・出典(年度)・関連章・解答の要点(解答があれば照合、なければ自分で解く。計算は python3 で検算。numpy は `/usr/bin/python3` にある。scipy はない)。出題傾向の表。学生の氏名・学籍番号は書かない
4. 講義が市販教科書に沿っていれば WebSearch で書名を特定し、書誌を確認する(WebSearch が見えなければ ToolSearch で "select:WebSearch,WebFetch")
5. `outline.md`: 話題で 12〜16 章(各 12〜20 ページ想定)。各章にタイトル / 対応資料とページ範囲 / 主な内容(講義の内容 + 補うべき標準的な導出・数値例)/ 関連する過去問。\part でまとめる。付録: 過去問(または課題)の全問解答・解説、用語の和英対照と数表
6. `STYLE.md`(templates からコピーし §7 科目固有: 記号の統一、図の方針(回路は circuitikz など)、数値は python で検算、本文に教員の連絡先・資料のパスワード・学生の個人情報を出さない、参考書と書誌の確認状況)。`.latexmkrc`(templates からコピー)
7. `work/agent-prompt-common.txt`(冒頭に STYLE.md §0 の本文の方針 — 本文に講義・資料・試験・過去問・年度・出典を書かない、問題の見出しは「演習: 内容」— を入れる。手本と同じ形式。教科書フォルダのパスを差し替え、「資料と方針」をこの科目に合わせる)
8. `PROGRESS.md`: 手順、章ごとのチェックボックス、末尾に「割り当て案」(章エージェント 4〜5 本に 2〜3 章ずつ。過去問付録と用語集の担当も明記。章どうしの申し送りは notes-chNN.md の先頭に書く方式)

## 返答(短く)
章立ての一覧(章番号・タイトル・想定ページ)、過去問・課題の数(年度・設問数)、資料の気になる点(欠けている回、紛れ込み、年度差、誤り)。
