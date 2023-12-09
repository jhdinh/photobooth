import sys
import time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

def count_down(displayNum):
    app = QApplication(sys.argv)

    window = QMainWindow()

    window.setAttribute(Qt.WA_TranslucentBackground, True)
    window.setAttribute(Qt.WA_NoSystemBackground, True)
    window.setWindowFlags(Qt.FramelessWindowHint)

    label = QLabel(window)
    if displayNum == 3:
        pixmap = QPixmap('assets/three.png')
    elif displayNum == 2:
        pixmap = QPixmap('assets/two.png')
    elif displayNum == 1:
        pixmap = QPixmap('assets/one.png')
    else:
        print("Oh no, countDown problem")
    label.setPixmap(pixmap)
    label.setScaledContents(True)
    label.setFixedSize(200, 200)

    window.label = label

    window.setGeometry(900, 390, 200, 200)

    window.show()
    QTimer.singleShot(750, window.close)
    app.exec_()
