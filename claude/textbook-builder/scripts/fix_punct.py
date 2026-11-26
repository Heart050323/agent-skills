#!/usr/bin/env python3
"""章本文の和文の句読点を「、。」に統一する(ASCII の , . が和文の直後にある場合のみ。コード環境とコメント行は除く)。
使い方: python3 fix_punct.py <教科書フォルダ>
"""
import re, glob, os, sys
jp = r'[\u3040-\u30ff\u4e00-\u9fff）」』〕】]'
for p in sorted(glob.glob(os.path.join(sys.argv[1], 'chapters', '*.tex'))):
    lines = open(p).read().split('\n'); out = []; incode = False; cnt = 0
    for L in lines:
        if re.search(r'\\begin\{(code|lstlisting|verbatim)\}', L): incode = True
        if not incode and not L.lstrip().startswith('%'):
            L2 = re.sub('(' + jp + r'),', r'\1、', L)
            L2 = re.sub('(' + jp + r')\.(?=\s|$|\\\\|\})', r'\1。', L2)
            L2 = L2.replace('，', '、').replace('．', '。')
            cnt += (L2 != L); L = L2
        if re.search(r'\\end\{(code|lstlisting|verbatim)\}', L): incode = False
        out.append(L)
    if cnt:
        open(p, 'w').write('\n'.join(out)); print(f'{os.path.basename(p)}: {cnt} lines')
