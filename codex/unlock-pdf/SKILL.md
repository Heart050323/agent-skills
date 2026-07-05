---
name: unlock-pdf
description: パスワード付きPDFのロックを解除する。PDFの鍵を外す、PDFのパスワードを解除する、と言われたときに使う。
argument-hint: "[PDFファイルパス] [パスワード(任意)]"
metadata:
  short-description: PDF password removal
---

# PDF パスワード解除スキル

## 手順

1. **入力の確認**: 引数からPDFファイルパスとパスワード（任意）を取得する。引数がなければユーザーにPDFファイルパスを確認する。

2. **ファイル存在確認**: 指定されたPDFファイルが存在するか確認する。存在しなければエラーを報告する。

3. **出力ファイル名の決定**: 元のファイル名の拡張子の前に `_unlocked` を付与する。
   - 例: `document.pdf` → `document_unlocked.pdf`

4. **パスワードなしで `gs` を試行**（オーナーパスワードのみの場合はこれで解除できる）:
   ```bash
   gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=<output> <input>
   ```

5. **失敗した場合、パスワード付きで再試行**:
   - 引数でパスワードが渡されていればそれを使う
   - パスワードがなければデフォルトパスワード `EcoEE2026` を試す
   - デフォルトパスワードも失敗した場合はユーザーにパスワードを確認する
   ```bash
   gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sPDFPassword=<password> -sOutputFile=<output> <input>
   ```

6. **`gs` が利用できない場合のフォールバック**:
   - `qpdf` を試す:
     ```bash
     qpdf --decrypt --password=<password> <input> <output>
     ```
   - `qpdf` もなければ `pikepdf`（Python）を試す:
     ```python
     import pikepdf
     pdf = pikepdf.open("<input>", password="<password>")
     pdf.save("<output>")
     ```

7. **結果報告**: 成功した場合は出力ファイルパスを報告。失敗した場合はエラー内容を報告する。

## Codex 向けメモ

- ファイル探索は `rg --files` を優先する。
- コマンド実行前に対象パスを確認し、出力先が既存ファイルを上書きしないよう注意する。
- `gs`、`qpdf`、`pikepdf` の順で試し、どこで失敗したかを簡潔に共有する。
