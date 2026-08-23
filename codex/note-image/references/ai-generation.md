# Route B: AI生成 — バックエンドとプロンプト規則

## バックエンド選択（上から順に確認）

1. **Gemini API**（`GEMINI_API_KEY` があるとき）— Nano Banana系。速く、指示追従が良い。
   ```bash
   # モデル例: gemini-3-pro-image / nano-banana系の最新を使う
   curl -s "https://generativelanguage.googleapis.com/v1beta/models/<model>:generateContent?key=$GEMINI_API_KEY" \
     -H 'Content-Type: application/json' \
     -d '{"contents":[{"parts":[{"text":"<プロンプト>"}]}],"generationConfig":{"responseModalities":["IMAGE"]}}'
   # レスポンスの inlineData.data (base64) をデコードしてPNG保存
   ```
2. **RunComfy CLI**（`runcomfy --version` が通るとき）— 複数モデルへの統一入口。
   ```bash
   runcomfy run <vendor>/<model>/<endpoint> --input '{"prompt":"..."}' --output-dir ./out
   ```
3. どちらも無ければユーザーに報告し、Route A（HTML）で代替できないか先に検討する。勝手に新サービスへ登録しない。

## モデルの使い分け（RunComfy経由のとき）

| 用途 | モデル | 補足 |
|---|---|---|
| 既定・写実全般 | `blackforestlabs/flux-2-klein/9b/text-to-image` | steps 4–8で試作、25で仕上げ |
| 画像内に正確な文字 | `openai/gpt-image-2/text-to-image` | 日本語可。文字は必ず `"…"` で引用。size は 1536_1024 / 1024_1024 / 1024_1536 のみ |
| 人物の肌・自然光 | `bytedance/seedream-5/lite/text-to-image` | 東アジア圏の顔立ちに強い |
| イラスト・画風 | `bytedance/dreamina-4-0/text-to-image` | 写実には使わない |
| 既存画像の部分修正 | `google/nano-banana-2/edit` | 位置語（「右上の〜」）が通る。同一性保持 |

見出し画像は 1280×670 に近い比率（16:9系）で生成し、後で切り抜く。

## プロンプト規則 — AI味は生成前に殺す

AI味の大半はプロンプト側の癖が原因。以下を守る:

1. **被写体→場面→光・質感の順で、具体に書く。** 「A weathered wooden desk by a north-facing window, morning light, a single teacup」のように、名詞は数えられるものにする。
2. **形容詞だけのプロンプトを書かない。** 「modern, clean, professional, vibrant, high quality」は生成モデルにとっての「いつもの」を呼び出す呪文であり、出てくるのがまさにAI味。禁止。
3. **光と時間を1つ決める。**「golden hour」「overcast noon」「単一光源の室内」など。全方位から照らされた画像がAI味の主因。
4. **パレットを制限する。**「muted palette, off-white background, one accent color (deep teal)」のように地と差し色を指定する。紫・シアン・ネオンは指定しない。
5. **質感の逃げ道を与える。**「film grain」「matte paper texture」「slight imperfections」— 完璧すぎる表面がAI味になる。
6. **文字は描かせない。** 日本語コピーはRoute Aの手法でHTML合成する。例外はGPT Image 2で、その場合も文字列を `"…"` で正確に引用する。
7. **ストック比喩を書かない。** AI・テクノロジーの記事でも、脳・回路・ロボット・光る地球を描かせず、記事の中の具体物（手元、道具、紙、街）を描く。

生成後は必ず開いて視認し、SKILL.mdのAI味チェックを通す。通らなければプロンプトの違反箇所（上記1–7のどれを破ったか）を特定してから再生成する。闇雲なガチャ再生成はしない。
