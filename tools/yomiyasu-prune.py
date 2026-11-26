#!/usr/bin/env python3
"""yomiyasu の検査記録のうち、古いものを消す。

対象は YOMIYASU_STATE_DIR（引数で指定も可）の runs/、inputs/、index/ だけ。
- runs/<実行ID>/ : 中の最も新しいファイルが --days 日より古ければ、フォルダごと消す。
- index/by-*/<キー>/<実行IDを含む名前> : 消した実行IDを指す索引を消し、空になったキーのフォルダも消す。
- inputs/<sha256>.bin : 残った記録のどれからも参照されず、1日より古い写しを消す（実行中の記録を壊さないため）。
state.json と .gitignore には触らない。--dry-run で消す対象だけを表示する。
"""
import argparse, os, re, shutil, sys, time
from pathlib import Path

HEX = re.compile(r"[0-9a-f]{64}")
RUN_ID = re.compile(r"\d{8}T\d{6}Z-[0-9a-f]{8}")


def newest_mtime(folder: Path) -> float:
    times = [folder.stat().st_mtime] + [p.stat().st_mtime for p in folder.rglob("*") if p.is_file()]
    return max(times)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("state_dir", nargs="?", default=os.environ.get("YOMIYASU_STATE_DIR"))
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not a.state_dir:
        print("状態フォルダが決まっていません（YOMIYASU_STATE_DIR か引数で指定）", file=sys.stderr)
        return 2
    state = Path(os.path.expanduser(a.state_dir))
    # 環境変数で決めたフォルダには state.json が置かれないため、runs/ か inputs/ があれば yomiyasu の状態フォルダとみなす
    looks_like_state = (state / "state.json").is_file() or (state / "runs").is_dir() or (state / "inputs").is_dir()
    if state.resolve() in (Path("/"), Path.home().resolve()) or not looks_like_state:
        print(f"yomiyasu の状態フォルダではないので何もしません: {state}")
        return 0
    now = time.time()
    cutoff = now - a.days * 86400

    def remove(p: Path) -> None:
        if a.dry_run:
            print("消す予定:", p)
        elif p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()

    runs = state / "runs"
    removed_runs, kept_runs = set(), set()
    for run in sorted(runs.iterdir()) if runs.is_dir() else []:
        if not run.is_dir():
            continue
        if newest_mtime(run) < cutoff:
            removed_runs.add(run.name)
            remove(run)
        else:
            kept_runs.add(run.name)

    index = state / "index"
    removed_index = 0
    for entry in index.glob("by-*/*/*") if index.is_dir() else []:
        found = RUN_ID.search(entry.name)  # by-path は「時刻.実行ID.回」、by-final と by-text は「実行ID.回」
        run_id = found.group(0) if found else None
        if run_id and run_id not in kept_runs and entry.stat().st_mtime < now - 86400:
            remove(entry)
            removed_index += 1
    if not a.dry_run and index.is_dir():
        for key in index.glob("by-*/*"):
            if key.is_dir() and not any(key.iterdir()):
                key.rmdir()

    referenced = set()
    for name in kept_runs:
        for f in (runs / name).rglob("*"):
            if f.is_file():
                referenced.update(HEX.findall(f.read_text(encoding="utf-8", errors="ignore")))
    removed_inputs = 0
    for blob in (state / "inputs").glob("*.bin") if (state / "inputs").is_dir() else []:
        if blob.stem not in referenced and blob.stat().st_mtime < now - 86400:
            remove(blob)
            removed_inputs += 1

    print(f"{time.strftime('%Y-%m-%d %H:%M')} 記録 {len(removed_runs)} 件、索引 {removed_index} 件、写し {removed_inputs} 件を"
          f"{'消す予定' if a.dry_run else '消しました'}（残した記録 {len(kept_runs)} 件、{a.days}日より新しいもの）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
