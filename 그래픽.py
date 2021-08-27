import sys
import time
import threading
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
 
class QtGUI(QWidget):
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle('test')
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.move(0, 0)
        self.resize(100, 170)
 
        #라벨 생성
        label1 = QLabel(self)
        label1.move(0,0)

        #이미지 관련 클래스 생성 및 이미지 불러오기 
        red = QPixmap('./image/red.png').scaled(100,170)
        yellow = QPixmap('./image/yellow.png').scaled(100,170)
        blue = QPixmap('./image/blue.png').scaled(100,170)
    
        arr = [red, yellow, blue]

        #이미지 관련 클래스와 라벨 연결
        i = 0
        while(1):
            label1.repaint()
            time.sleep(0.5)
            label1.setPixmap(arr[i])
            i = (i+1)%3
            self.show()
            QApplication.processEvents()


        
 
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)

    t = threading.Thread(target=QtGUI())
    t.start()
    t.join()

    app.exec_()
