from PyQt5 import QtGui, QtCore, QtWidgets
from components.carousel import carouselItem
import colorama as clr
import qtawesome as qta
import sys

class Carousel(QtWidgets.QWidget):
    itemsLay = None
    globalPos = 0

    def setup(self, carouselWidgets, startPos = 0, elemAsButtons = False):
        self.cWidgets = carouselWidgets
        self.pos = startPos
        globalPos = startPos

        print(len(carouselWidgets))

        frameWidget = QtWidgets.QWidget()
        frameWidget.setObjectName("carouselFrame")

        left = qta.icon("fa.caret-left", color="#f9f9f9")
        right = qta.icon("fa.caret-right", color="#f9f9f9")

        goLeft = QtWidgets.QPushButton(left, "")
        goLeft.setObjectName("carouselSideButtons")
        goLeft.setIconSize(QtCore.QSize(64, 64))
        goLeft.setMaximumWidth(70)
        goLeft.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        goLeft.clicked.connect(lambda:Carousel.prevItem(self))

        goRight = QtWidgets.QPushButton(right, "")
        goRight.setObjectName("carouselSideButtons")
        goRight.setIconSize(QtCore.QSize(64, 64))
        goRight.setMaximumWidth(70)
        goRight.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        goRight.clicked.connect(lambda:Carousel.nextItem(self))

        backLay = QtWidgets.QHBoxLayout()
        backLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        backLay.addWidget(frameWidget)

        cLay = QtWidgets.QGridLayout()
        cLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        cLay.addWidget(goLeft, 0, 0)

        centerItem = QtWidgets.QWidget()
        Carousel.itemsLay = QtWidgets.QStackedLayout()
        Carousel.itemsLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        centerItem.setLayout(Carousel.itemsLay)
        cLay.addWidget(centerItem, 0, 1)

        for i in range(len(self.cWidgets)):
            if elemAsButtons:
                itmBtn = QtWidgets.QPushButton(self.cWidgets[i])
                Carousel.itemsLay.addWidget(itmBtn)
            else:
                Carousel.itemsLay.addWidget(self.cWidgets[i])

        cLay.addWidget(goRight, 0, 2)
        cLay.setSpacing(10)
        frameWidget.setLayout(cLay)

        self.setLayout(backLay)

    def nextItem(self):
        Carousel.globalPos += 1
        if(Carousel.globalPos >= len(self.cWidgets)):
            Carousel.globalPos = 0
        Carousel.itemsLay.setCurrentIndex(Carousel.globalPos)
        self.pos = Carousel.globalPos

    def prevItem(self):
        Carousel.globalPos -= 1
        if(Carousel.globalPos < 0):
            Carousel.globalPos = len(self.cWidgets)-1
        Carousel.itemsLay.setCurrentIndex(Carousel.globalPos)
        self.pos = Carousel.globalPos
    
    def getCurrentPos(self):
        return Carousel.globalPos

#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    #Set the main styling of dis window aswell
    with open("../appearance/style/stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)
    gui = Carousel()
    gui.show()
    app.exec_()