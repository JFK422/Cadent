import qtawesome as qta
from components.Menu import menuSeperator
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class MenuWindow(QtWidgets.QWidget):
    def setup(self):
        vMenu = QtWidgets.QVBoxLayout()
        vMenu.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        vMenu.setContentsMargins(QtCore.QMargins(20,20,20,20))

        scrollLay = QtWidgets.QVBoxLayout()
        scrollLay.setContentsMargins(QtCore.QMargins(10,10,10,10))
        scrollLay.setAlignment(QtCore.Qt.AlignTop)

        scrollLayWid = QtWidgets.QWidget()
        scrollLayWid.setObjectName("scrollMenuLay")
        scrollLayWid.setLayout(scrollLay)

        fileText = QtWidgets.QLabel("Window")
        fileText.setObjectName("menuTitle")
        vMenu.addWidget(fileText)

        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(scrollLayWid)
        scroll.setWidgetResizable(True)
        vMenu.addWidget(scroll)

        #Add icons later! Also further additions may needed
        fileExplorer = QtWidgets.QPushButton("File Explorer")
        fileExplorer.setMaximumHeight(50)
        fileExplorer.setObjectName("scrollMenuItem")
        scrollLay.addWidget(fileExplorer)

        closeAllEditors = QtWidgets.QPushButton("Close all Editors")
        closeAllEditors.setMaximumHeight(50)
        closeAllEditors.setObjectName("scrollMenuItem")
        scrollLay.addWidget(closeAllEditors)

        console = QtWidgets.QPushButton("Show Console")
        console.setMaximumHeight(50)
        console.setObjectName("scrollMenuItem")
        scrollLay.addWidget(console)

        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self.setLayout(vMenu)