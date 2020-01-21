import pyocr
import pyocr.builders
import cv2
from PIL import Image
import sys
import os

def main():
    
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

    # カメラから映像を取得
    capture = cv2.VideoCapture(0)
    if capture.isOpened() is False:
        raise("IO Error")

    # Qが押されるまで無限ループ
    while(True):
        ret, frame = capture.read()
        if ret == False:
            print("カメラから映像を接続できません")
            continue
        
        #画像から文字列を取得
        orgHeight, orgWidth = frame.shape[:2]
        #size = (int(orgWidth/4), int(orgHeight/4))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(gray ,(orgWidth,orgHeight))

        res = tool.image_to_string(
                Image.fromarray(image),
                lang="jpn",
                builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6))

        #取得した文字列を表示
        print(res)
 
        #以下は画像のどの部分を検出し、どう認識したかを分析
        for d in res:
            print(d.content) #どの文字として認識したか
            print(d.position) #どの位置を検出したか
            cv2.rectangle(image, d.position[0], d.position[1], (0, 0, 255), 2) #検出した箇所を赤枠で囲む

        cv2.imshow("capture", image)
        # waitKeyの引数は10~30程度に設定
        k = cv2.waitKey(30)

        # qを押すとカメラ映像の表示を終了する
        if k == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()