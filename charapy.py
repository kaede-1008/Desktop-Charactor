import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
import ctypes


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint |Qt.FramelessWindowHint )
        self.getmonitorsize()
        self.initUI()

    def initUI(self):
        
        # QPixmap�I�u�W�F�N�g�쐬
        pixmap = QPixmap("altina_02.png")

        # ���x��������Ă��̒��ɉ摜��u��
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        self.show()

    def getmonitorsize(self):

        x = ctypes.windll.user32.GetSystemMetrics(0)
        y = ctypes.windll.user32.GetSystemMetrics(1)

        self.setGeometry(x - 166, y - 203, 160, 160)
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())