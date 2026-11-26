#!/bin/bash
# 教科書をビルドして品質指標を表示する。
# 使い方: build.sh <教科書フォルダ> [--clean]
#   成功時: ページ数・未定義参照・Overfull 件数・欠落図を表示
#   失敗時: ログのエラー箇所(file:line)を表示
set -u
dir="$1"; cd "$dir" || exit 1
[ "${2:-}" = "--clean" ] && latexmk -C >/dev/null 2>&1
[ -f .latexmkrc ] || cp ~/.codex/skills/textbook-builder/templates/.latexmkrc .
# 失敗したビルドで既存の main.pdf が消えないよう、退避してから実行する
[ -f main.pdf ] && cp -p main.pdf main.pdf.prev
latexmk main.tex > build.out 2>&1
rc=$?
if [ $rc -ne 0 ] || [ ! -f main.pdf ]; then
  echo "BUILD FAILED (rc=$rc)"
  if [ -f main.pdf.prev ]; then mv -f main.pdf.prev main.pdf; echo "(前回の main.pdf を戻した)"; fi
  grep -n -E '^\./.*:[0-9]+:|^!|Error' main.log 2>/dev/null | head -30
  tail -20 build.out
  exit 1
fi
rm -f main.pdf.prev
echo "BUILD OK: $(pdfinfo main.pdf | awk '/^Pages:/{print $2}') pages"
echo "undefined refs/cites: $(grep -c -E 'undefined' main.log)"
grep -E "Reference .* undefined|Citation .* undefined" main.log | sort -u | head -20
echo "overfull hbox (>5pt): $(grep -E 'Overfull \\hbox \(([5-9]|[0-9]{2,})' main.log | wc -l | tr -d ' ')"
grep -E "File .* not found" main.log | sort -u | head
grep -E "^LaTeX Warning: (Label|There were)" main.log | sort -u | head
