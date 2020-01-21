import pyocr
import pyocr.builders
import cv2
from PIL import Image
import sys
import os

#インストール済みのTesseractのパスを通す
#64bit版のパスを一時的に通す
path_tesseract = "C:\\Program Files\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

#利用可能なOCRツールを取得
tools = pyocr.get_available_tools()
 
if len(tools) == 0:
    print("OCRツールが見つかりませんでした。")
    sys.exit(1)
 
#利用可能なOCRツールはtesseractしか導入していないため、0番目のツールを利用
tool = tools[0]

#画像から文字列を取得
currentpath = os.getcwd()
res = tool.image_to_string(Image.open(currentpath + "\pic\sample.png"),
                            lang="jpn",
                            builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6))
 
#取得した文字列を表示
print(res)
 
#以下は画像のどの部分を検出し、どう認識したかを分析
out = cv2.imread(currentpath + "\pic\sample.png")
 
for d in res:
    print(d.content) #どの文字として認識したか
    print(d.position) #どの位置を検出したか
    cv2.rectangle(out, d.position[0], d.position[1], (0, 0, 255), 2) #検出した箇所を赤枠で囲む
 
#検出結果の画像を表示
cv2.imshow("img",out)
cv2.waitKey(0)
cv2.destroyAllWindows()