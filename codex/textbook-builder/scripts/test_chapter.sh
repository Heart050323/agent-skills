#!/bin/bash
# 1章だけを入れた一時文書をビルドする(章執筆エージェントの確認用)。
# 使い方: test_chapter.sh <教科書フォルダ> <chNN>
# 出力: <教科書フォルダ>/work/test-<chNN>/main.pdf
set -u
book="$1"; ch="$2"
w="$book/work/test-$ch"
rm -rf "$w"; mkdir -p "$w/chapters"
cp ~/.codex/skills/textbook-builder/templates/.latexmkrc "$w/"
ln -sfn "$book/figures" "$w/figures"
cp "$book/chapters/$ch.tex" "$w/chapters/"
echo "(test)" > "$w/chapters/preface.tex"
[ -f "$book/refs/$ch.bib" ] && cp "$book/refs/$ch.bib" "$w/refs.bib"
# 本の main.tex のプリアンブルを流用(なければテンプレート)
src="$book/main.tex"; [ -f "$src" ] || src=~/.codex/skills/textbook-builder/templates/main.tex
python3 - "$src" "$w/main.tex" "$ch" <<'EOF'
import sys,re
src,dst,ch=sys.argv[1:]
s=open(src).read()
pre=s.split('\\begin{document}')[0]
body=('\\begin{document}\n\\mainmatter\n\\input{chapters/%s}\n'
      '\\IfFileExists{refs.bib}{\\printbibliography[title=参考文献]}{}\n\\end{document}\n') % ch
pre=pre.replace('{{SUBJECT}}','test').replace('{{SUBTITLE}}','').replace('{{AUTHOR_LINE}}','').replace('{{DATE}}','')
open(dst,'w').write(pre+body)
EOF
bash ~/.codex/skills/textbook-builder/scripts/build.sh "$w"
