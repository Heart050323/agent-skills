# デバイスセットアップ手順

このリポジトリは Claude Code(`claude/`)と Codex(`codex/`)のスキルを1つのソースとして管理する。
各デバイスでは clone して、エージェントが読む実際のパスにリンクを張る。

## macOS

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

- 他のデバイスでの変更を取り込む: `git -C ~/agent-skills pull`
- スキルを作成・編集したら: `skill-sync` スキルが Claude/Codex 両方言への移植と commit & push まで行う(手動なら `git add -A && git commit && git push`)
- `codex/.system/` は Codex 内部用で git 管理外(.gitignore 済み)。リポジトリには含まれない
