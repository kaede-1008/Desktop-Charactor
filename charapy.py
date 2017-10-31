# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import(QApplication, QWidget, 
                            QLabel, QFrame, 
                            QHBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import ctypes

def getMonitorSize():
    x = ctypes.windll.user32.GetSystemMetrics(0)
    y = ctypes.windll.user32.GetSystemMetrics(1)
    return x, y

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowFlags(Qt.WindowStaysOnTopHint |Qt.FramelessWindowHint )
    x, y = getMonitorSize()
    window.setGeometry(x - 166, y - 203, 160, 160)
    pixmap = QPixmap("altina_02.png")
    label = QLabel('Label', window)
    label.setPixmap(pixmap)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()