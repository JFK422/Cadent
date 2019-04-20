from PyQt5 import QtGui, QtCore, QtWidgets
from PIL import Image
import colorama as clr
import qtawesome as qta
import sys

class CarouselItem(QtWidgets.QWidget):
    
    def setup(self, name = "", path = "", existing = True):
        self.name = name
        self.projPath = path
        projImg = ""

        frameWidget = QtWidgets.QWidget()

        pName = QtWidgets.QLabel(name)
        pName.setObjectName("projectLabel")
        pImg = QtWidgets.QLabel("")
        pImg.setObjectName("projectLabel")
        #pImg.setScaledContents(True)

        #projFile = open(path, "r")
        #print(projFile.read())
        #print(projFile.read().split("\n")[3].split("=")[1])
        #QtGui.QPixmap(projFile.read().split("\n")[3].split("=")[1])

        if existing:
            frameWidget.setObjectName("carouselItemFrame")
            pImg.setPixmap(QtGui.QPixmap("/home/jfk422/Projects/HitchTestProj/Resources/titleImg.png").scaled(256, 256, QtCore.Qt.KeepAspectRatio))
        else:
            frameWidget.setObjectName("carouselItemFrameNonExisting")
            pImg.setPixmap(QtGui.QPixmap("./resources/projectImages/pImgO.png").scaled(256, 256, QtCore.Qt.KeepAspectRatio))


        mainLay = QtWidgets.QVBoxLayout()
        mainLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        mainLay.setSpacing(0)

        titleLay = QtWidgets.QVBoxLayout()
        titleLay.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        titleLay.setContentsMargins(QtCore.QMargins(0,10,0,10))
        titleWidget = QtWidgets.QWidget()
        titleWidget.setLayout(titleLay)

        imgLay = QtWidgets.QVBoxLayout()
        imgLay.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        imgLay.setContentsMargins(QtCore.QMargins(0,0,0,20))

        imgWidget = QtWidgets.QWidget()
        imgWidget.setLayout(imgLay)

        titleLay.addWidget(pName)
        imgLay.addWidget(pImg)

        mainLay.addWidget(titleWidget)
        mainLay.addWidget(imgWidget)
        frameWidget.setLayout(mainLay)

        backLay = QtWidgets.QHBoxLayout()
        backLay.setContentsMargins(QtCore.QMargins(0,10,0,10))
        backLay.addWidget(frameWidget)

        self.setLayout(backLay)