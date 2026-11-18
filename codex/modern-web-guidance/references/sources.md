# 出典と変更点

確認日: 2026-11-19（Asia/Tokyo）

- 発見元: https://x.com/don_tech1/status/2121060480714469728
- 上流: https://github.com/GoogleChrome/modern-web-guidance
- 参照コミット: `64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65`
- 原版SKILL: https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/skills/modern-web-guidance/SKILL.md
- ライセンス: [LICENSE](../LICENSE)（原版の通知を保持）

## この版での変更

上流SKILLと5ガイドから、文書参照で使える軽量版を作成。毎回のCLI実行、npxによる導入、全フロントエンド作業への強制適用、固定の報告形式は採用しない。ガイド間のフォールバック方針の差異を明記し、実プロジェクトの互換性・スクロール要件を優先。上流CLIやガイド全体のインストールではない。

原版そのものや作者の公式配布版ではなく、個人スキル集向けの改変版。投稿の人気、売上、性能の宣伝値を採用理由にはしていない。

## 読んだガイド

- https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/skills/modern-web-guidance/guides/css/size-aware-styling.md
- https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/skills/modern-web-guidance/guides/forms/ime-safe-enter-submit.md
- https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/skills/modern-web-guidance/guides/ui-behaviors/light-dismiss-a-dialog.md
- https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/skills/modern-web-guidance/guides/ui-behaviors/prevent-page-scroll-under-modal-dialog.md
- https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/skills/modern-web-guidance/guides/ui-components/dialog.md

## 追加照合先

- https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/isComposing
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog
- https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries

各APIの存在と基本的な意味を照合。全対象ブラウザーでの実動作を検証した記録ではない。
