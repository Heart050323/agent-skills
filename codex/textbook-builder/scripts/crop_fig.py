#!/usr/bin/env python3
"""PDF のページ(の一部)を図として PNG に切り出す。PIL 不要(pdftoppm を使う)。

使い方:
  crop_fig.py <pdf> <page> <out.png> [x0 y0 x1 y1] [--dpi 200]
    x0..y1 はページ幅・高さに対する割合 (0〜1)。左上が (0,0)。省略時はページ全体。
例:
  crop_fig.py レジュメ/5.pdf 12 figures/ch05-btree.png 0.05 0.2 0.95 0.9
切り出したら必ず PNG を画像として開いて確認し、余白・見切れを調整すること。
画像の埋め込み写真だけを取り出したい場合は pdfimages -png -f P -l P <pdf> <prefix> も使える。
"""
import os, re, subprocess, sys, tempfile, shutil


def page_size_pts(pdf, page):
    out = subprocess.run(["pdfinfo", "-f", str(page), "-l", str(page), pdf],
                         capture_output=True, text=True).stdout
    m = re.search(r"Page\s+%d size:\s+([\d.]+) x ([\d.]+)" % page, out) or \
        re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", out)
    if not m:
        sys.exit("ページサイズが取得できません: %s" % pdf)
    # 回転ページ対応
    rot = re.search(r"Page\s+%d rot:\s+(\d+)" % page, out)
    w, h = float(m.group(1)), float(m.group(2))
    if rot and int(rot.group(1)) in (90, 270):
        w, h = h, w
    return w, h


def main():
    args = sys.argv[1:]
    dpi = 200
    if "--dpi" in args:
        i = args.index("--dpi"); dpi = int(args[i + 1]); del args[i:i + 2]
    if len(args) not in (3, 7):
        sys.exit(__doc__)
    pdf, page, out = args[0], int(args[1]), args[2]
    box = [float(v) for v in args[3:7]] if len(args) == 7 else [0, 0, 1, 1]
    w, h = page_size_pts(pdf, page)
    W, H = w * dpi / 72.0, h * dpi / 72.0
    x, y = int(box[0] * W), int(box[1] * H)
    cw, ch = int((box[2] - box[0]) * W), int((box[3] - box[1]) * H)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    tmp = tempfile.mkdtemp()
    try:
        prefix = os.path.join(tmp, "c")
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi), "-png",
                        "-x", str(x), "-y", str(y), "-W", str(cw), "-H", str(ch),
                        "-singlefile", pdf, prefix], check=True)
        shutil.move(prefix + ".png", out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"wrote {out} ({cw}x{ch}px @ {dpi}dpi)")


if __name__ == "__main__":
    main()
