#!/usr/bin/env python3
"""refs/*.bib の日本人著者名を {{姓名} and {姓名}} 形式に統一する(biblatex で姓名が崩れるのを防ぐ)。
使い方: python3 fix_bib_names.py <教科書フォルダ>
"""
import re, glob, os, sys
cjk = re.compile(r'[぀-ヿ一-鿿]')
def fix(m):
    pre, val = m.group(1), m.group(2)
    if not cjk.search(val):
        return m.group(0)
    v = val.strip().strip('{}')
    names = re.split(r'\s+and\s+|・', v)
    names = [n.strip().strip('{}').replace(', ', '').replace(',', '') for n in names if n.strip()]
    return pre + '{' + ' and '.join('{%s}' % n for n in names) + '},'
for f in glob.glob(os.path.join(sys.argv[1], 'refs', '*.bib')):
    s = open(f).read()
    s2 = re.sub(r'((?:author|editor)\s*=\s*)(\{.*\}),', fix, s)
    if s2 != s:
        open(f, 'w').write(s2); print('fixed', f)
