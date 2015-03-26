# This plugin requires OpenCV to be installed, and returns a PIL Image object

import os
import sys

import cv2
from PIL import Image

from PyQt4.QtCore import QTimer, QRect
from PyQt4.QtGui import QDialog, QApplication, QPainter, QWidget, QImage, QVBoxLayout
from PyQt4.uic import loadUi


UI_MAIN = os.path.join(os.path.dirname(__file__), 'hdu_select.ui')
UI_HDU = os.path.join(os.path.dirname(__file__), 'hdu.ui')


class HDUListSelector(QDialog):

    def __init__(self):

        super(HDUListSelector, self).__init__()
        self.ui = loadUi(UI_MAIN, self)
        self.vertical_layout = QVBoxLayout(self.scroll.widget())
        self.vertical_layout.setSpacing(0)

        for i in range(20):
            hdu_wi = loadUi(UI_HDU, None)
            self.vertical_layout.addWidget(hdu_wi)

        self.scroll.setMinimumWidth(hdu_wi.width())


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create an application object
    wi = HDUListSelector()
    wi.show()
    app.exec_()
