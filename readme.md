# pythonで始めるopenCV4

---

## Install
- pythonのインストーラーが必要です

https://www.python.org/downloads/windows/

## Usage
- コマンドプロンプト or PowerShellを起動して、以下コマンドで環境構築

1. venv環境の構築
> python -m venv venv

2. venvアクティベート
>.\venv\Scripts\activate

3. pipでopencv4をインストール
> pip install opencv-python

4. https://github.com/UB-Mannheim/tesseract/wiki から64bitインストーラーをダウンロードし、インストール。https://itport.cloud/?p=8326 を参考に必要項目にチェックをいれてください。

5. Pathに「C:\Program Files\Tesseract-OCR」を追加する。
環境変数項目(ユーザー環境変数)としてTESSDATA_PREFIXを作成して、「C:\Program Files\Tesseract-OCR\tessdata」を追加する(bat化したい)

6. 日本語の教師データファイルを横書き用と縦書きの2種類ダウンロードする
https://github.com/tesseract-ocr/tesseract/wiki/Data-Files

7. > pip install pyocr

## memo

- pyファイルと同一ディレクトリのパス等は次のように取得
```python
currentpath = os.getcwd()
res = tool.image_to_string(Image.open(currentpath + "\pic\sample.png"),
```

## Version

python : 3.8.1
opencv : 4.1.2
chainer : 7.1.0

## Reference URL
https://itport.cloud/?p=8326

https://gammasoft.jp/blog/ocr-by-python/

## Author
pisa