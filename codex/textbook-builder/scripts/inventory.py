#!/usr/bin/env python3
"""科目フォルダの資料一覧を作る。

使い方: python3 inventory.py <科目フォルダ> [出力md]
各 PDF のページ数・テキスト抽出量(文字/ページ)・推定種別を表にする。
テキストが少ない PDF はスキャン画像なので、画像として開いて読む必要がある。
"""
import os, re, subprocess, sys

KIND_RULES = [
    (r"解答|answer|ans|kaitou|solution", "解答"),
    (r"過去問|期末|中間|exam|test|試験|pastexam|shikepuri|シケプリ", "過去問"),
    (r"report|レポート|kadai|課題|homework|hw|演習", "課題/レポート"),
    (r"note|ノート|notebook|板書", "ノート"),
    (r"handson|ハンズオン|lab|実習", "ハンズオン"),
    (r"syllabus|シラバス|about|outline|内容", "概要"),
]


def kind_of(path):
    low = path.lower()
    for pat, k in KIND_RULES:
        if re.search(pat, low):
            return k
    return "講義資料"


def pdf_info(path):
    try:
        out = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=60).stdout
        m = re.search(r"Pages:\s+(\d+)", out)
        pages = int(m.group(1)) if m else 0
    except Exception:
        pages = 0
    try:
        txt = subprocess.run(["pdftotext", "-l", "5", path, "-"], capture_output=True,
                             text=True, timeout=120).stdout
        chars = len(re.sub(r"\s", "", txt))
        per = chars // max(1, min(pages, 5))
    except Exception:
        per = 0
    return pages, per


def main():
    root = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    rows, others = [], []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if not d.startswith(".") and ".sb-" not in d]
        for fn in sorted(fns):
            if fn.startswith("."):
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root)
            if fn.lower().endswith(".pdf"):
                if "のコピー" in fn:
                    continue
                pages, per = pdf_info(p)
                rows.append((rel, pages, per, kind_of(rel)))
            else:
                others.append(rel)
    rows.sort()
    lines = ["| ファイル | ページ | 文字/頁 | 種別 | 読み方 |", "|---|---:|---:|---|---|"]
    total = 0
    for rel, pages, per, k in rows:
        total += pages
        how = "テキスト+視覚" if per > 150 else "視覚(スキャン)"
        lines.append(f"| {rel} | {pages} | {per} | {k} | {how} |")
    lines.append(f"\nPDF {len(rows)} 件 / 合計 {total} ページ")
    exts = {}
    for o in others:
        e = os.path.splitext(o)[1].lower() or "(なし)"
        exts[e] = exts.get(e, 0) + 1
    lines.append("\nPDF 以外: " + ", ".join(f"{e}×{n}" for e, n in sorted(exts.items(), key=lambda x: -x[1])))
    small = [o for o in others if os.path.splitext(o)[1].lower() in
             (".jpg", ".jpeg", ".png", ".heic", ".pptx", ".docx", ".txt", ".md", ".tex", ".ipynb", ".py", ".c")]
    if small:
        lines.append("\n利用候補(画像・文書・コード、先頭80件):")
        lines += [f"- {o}" for o in small[:80]]
    text = "\n".join(lines)
    if out:
        open(out, "w").write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
