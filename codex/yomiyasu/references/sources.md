# 出典と導入の記録

このファイルと `agents/openai.yaml` は個人スキル集で足したもの。ほかのファイルは上流の版をそのまま置いている（改変なし）。

- 発見元: https://x.com/oga_aiichiro/status/2125567241550987395
- 上流: https://github.com/nanaism/yomiyasu （`skills/yomiyasu/`）
- 版: 3.4.1、参照コミット `3979c750b5e1fe9892bd47bb354f0fb51d534ff2`（確認日: 2026-11-26）
- ライセンス: [LICENSE](../LICENSE)（MIT）、[UNICODE-LICENSE.txt](../UNICODE-LICENSE.txt)

## 中身の確認

- 検査スクリプトはPython標準ライブラリだけで動き、ネットワークに接続しない。`yomiyasu_check.py` は自分の lint / diff を子プロセスで呼ぶだけ。
- 検査の記録を、作業フォルダのgitの最上位（gitの外では作業フォルダ）の `.yomiyasu/` に書く。
- `scripts/yomiyasu_hook.py` は任意のフック。設定ファイルに自分で登録したときだけ動く。この導入では登録していない。

## 更新のしかた

上流は更新が速い。新しい版にするときは、`claude/yomiyasu` と `codex/yomiyasu` をいったん消し、上流の `skills/yomiyasu/` を両方にコピーしてから、このファイルと `agents/openai.yaml` を戻し、版とコミットを書き換える（前の版にしかないファイルを残さないため、上書きコピーはしない）。

## 既存スキルとの関係

`rewrite-human` は、日本語の文章の推敲をこのスキルに回し、日本語以外と、学術文の文体だけを自分で扱う。
