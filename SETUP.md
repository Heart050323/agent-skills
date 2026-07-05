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
- スキルを作成・編集したら(オーナーのみ): `skill-sync` スキルが Claude/Codex 両方言への移植と commit & push まで行う(手動なら `git add -A && git commit && git push`)
- `codex/.system/` は Codex 内部用で git 管理外(.gitignore 済み)。リポジトリには含まれない
- スキルを1個だけ試したい場合は `npx skills add Heart050323/agent-skills@<スキル名>` でも入れられる
