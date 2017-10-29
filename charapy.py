# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import(QApplication, QWidget, 
    QLabel, QFrame, QHBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = QWidget(None, Qt.FramelessWindowHint)
    window.setGeometry(1200, 565, 160, 160)
    pixmap = QPixmap("altina_02.png")

    label = QLabel('Label', window)
    label.setPixmap(pixmap)
    

    window.show()
    sys.exit(app.exec_())