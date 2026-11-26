#!/bin/bash
# 資料 PDF のテキストを抽出する(ページ区切り付き)。
# 使い方: extract.sh <出力ディレクトリ> <pdf> [<pdf> ...]
# 出力: <出力ディレクトリ>/<pdf名>.txt  各ページの先頭に "===== p.N =====" を入れる
set -u
out="$1"; shift
mkdir -p "$out"
for f in "$@"; do
  base=$(basename "$f"); stem="${base%.*}"
  n=$(pdfinfo "$f" 2>/dev/null | awk '/^Pages:/{print $2}')
  [ -z "$n" ] && { echo "skip (not pdf?): $f"; continue; }
  : > "$out/$stem.txt"
  for ((i=1; i<=n; i++)); do
    echo "===== p.$i =====" >> "$out/$stem.txt"
    pdftotext -layout -f $i -l $i "$f" - 2>/dev/null >> "$out/$stem.txt"
  done
  c=$(tr -d '[:space:]' < "$out/$stem.txt" | wc -c | tr -d ' ')
  echo "$stem: $n pages, $c chars"
done
