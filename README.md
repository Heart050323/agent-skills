# agent-skills

Claude / Codex 用の個人スキル集。`claude/` と `codex/` に各ホスト向けの20種類を管理しています。導入と同期は [SETUP.md](SETUP.md) を参照してください。標準の skill-creator などは同梱しません。

## 整理後の使い方

| 以前のスキル | 現在の扱い |
| --- | --- |
| adaptive-effort | token-efficiency のモデル・労力比較リファレンスへ統合 |
| output-check-fix-loop | output-checker の修正モードへ統合 |
| citation-verification | verify-citations に一本化。BibTeX形式検査は導入済みの latex-paper-en の補助を利用 |
| full-output-enforcement | 削除。依頼された成果物の完了条件で判断 |
| writing-great-skills | 削除。各ホストの標準creatorを利用 |

デザイン系のスキルは用途別の選択肢です。すべてを同時に適用したり、好みを一般的な品質要件として強制したりしません。削除前の内容はGit履歴から復元できます。
