# セットアップ手順

このリポジトリは Claude Code(`claude/`)と Codex(`codex/`)のスキルを1つのソースとして管理する。
各デバイスでは clone して、エージェントが読む実際のパスにリンクを張る。

リポジトリは public なので clone に認証は不要。push できるのはオーナーのみ。
オーナー以外の人へ: そのまま clone すれば読み取り専用で使える。
自分流に改造したい場合は Fork して、Fork 先を clone すること。

## macOS / Linux

Claude Code しか使わないマシン(Linux サーバーなど)では、`.codex` の行を省略してよい。

```bash
git clone https://github.com/Heart050323/agent-skills.git ~/agent-skills

# 既存の skills ディレクトリがあれば退避
[ -e ~/.claude/skills ] && mv ~/.claude/skills ~/.claude/skills.bak
[ -e ~/.codex/skills ]  && mv ~/.codex/skills  ~/.codex/skills.bak

ln -s ~/agent-skills/claude ~/.claude/skills
ln -s ~/agent-skills/codex  ~/.codex/skills

# Codex 内部ディレクトリ(.system)は git 管理外なので、退避分から戻す
[ -d ~/.codex/skills.bak/.system ] && cp -R ~/.codex/skills.bak/.system ~/agent-skills/codex/
```

## Windows

コマンドプロンプト(cmd)で実行。ジャンクション(`mklink /J`)は管理者権限不要。

```bat
git clone https://github.com/Heart050323/agent-skills.git %USERPROFILE%\agent-skills

rem 既存の skills ディレクトリがあれば退避
if exist %USERPROFILE%\.claude\skills ren %USERPROFILE%\.claude\skills skills.bak
if exist %USERPROFILE%\.codex\skills  ren %USERPROFILE%\.codex\skills  skills.bak

mklink /J %USERPROFILE%\.claude\skills %USERPROFILE%\agent-skills\claude
mklink /J %USERPROFILE%\.codex\skills  %USERPROFILE%\agent-skills\codex

rem Codex の .system を退避分から戻す(存在する場合)
if exist %USERPROFILE%\.codex\skills.bak\.system xcopy /E /I %USERPROFILE%\.codex\skills.bak\.system %USERPROFILE%\agent-skills\codex\.system
```

改行コードは `.gitattributes` で LF に固定済み。`core.autocrlf` の設定は不要。

## 日々の運用

- 最新を取り込む: `git -C ~/agent-skills pull`
- スキルを作成・編集したら: `skill-sync` で必要な変更を両ホストへ移植し検証する。公開を依頼済みの場合だけ、対象パスを明示してステージし、差分を確認して commit / push する。無関係な変更を含めない。
- `codex/.system/` は Codex 内部用で git 管理外(.gitignore 済み)。リポジトリには含まれない
- スキルを1個だけ試したい場合は `npx skills add Heart050323/agent-skills@<スキル名>` でも入れられる

## 重複インストールの整理

`~/.agents/skills` に同名の旧コピーがある場合は、内容とリンク先を比較する。このリポジトリを正本にするなら、独自変更を保存・統合したうえで旧コピーを探索対象外へ退避する。同名のスキルは自動で内容が統合されない。標準の `.system/` は移動・削除しない。

## yomiyasu の検査記録（各デバイスで1回）

yomiyasu は推敲のたびに、原文・最終稿・資料の全文の写しを含む検査記録を書く。既定ではリポジトリの最上位（Gitの外では作業フォルダ）の `.yomiyasu/` に書くため、置き場所が散らばり、Google Drive などの同期フォルダにも乗る。次の運用にそろえる。

- 置き場所: `~/.local/state/yomiyasu`（内蔵ディスク、同期の外、権限700）に1か所にまとめる。
- 保存期間: 記録が要るのは推敲から提出前の照合（verify）まで。30日を過ぎた記録と、どの記録からも参照されない写しを週1回消す。
- `.yomiyasu-words/`（プロジェクトの「直さない語・見直す語」）は記録とは別物。各プロジェクトのGitに入れて残す。
- 残したくない文章は「記録なしで」と頼む（`--no-record`。この場合、提出前の照合はできない）。

```bash
mkdir -p ~/.local/state/yomiyasu && chmod 700 ~/.local/state/yomiyasu
```

Claude Code: `~/.claude/settings.json` の `env` に足す。

```json
"env": { "YOMIYASU_STATE_DIR": "/Users/<ユーザー名>/.local/state/yomiyasu" }
```

Codex: `~/.codex/config.toml` の `[shell_environment_policy.set]` に足す。

```toml
YOMIYASU_STATE_DIR = "/Users/<ユーザー名>/.local/state/yomiyasu"
```

30日で消す処理: [tools/yomiyasu-prune.py](tools/yomiyasu-prune.py) をmacOSのlaunchdで週1回（月曜10時）動かす。`~/Library/LaunchAgents/local.agent-skills.yomiyasu-prune.plist` に、`/usr/bin/python3 -I ~/agent-skills/tools/yomiyasu-prune.py ~/.local/state/yomiyasu --days 30` を `StartCalendarInterval`（Weekday 1, Hour 10）で登録し、`launchctl bootstrap gui/$(id -u) <plist>` で読み込む。ログは `~/.local/state/yomiyasu-prune.log`。消す前の確認は `--dry-run`。
