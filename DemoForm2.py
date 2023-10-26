#DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys
import typing 
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일 로딩(파일명 변경)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼 클래스 정의(QmainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯 메서드
    def firstClick(self) :
        self.label.setText("첫번째 버튼")
    def secondClick(self) :
        self.label.setText("두번째 버튼~~")
    def thirdClick(self) :
        self.label.setText("세번째 버튼 클릭~~")
            
#직접 실행했는지 여부(진입점 체크)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()