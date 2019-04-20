import qtawesome as qta
from components.Menu import menuSeperator
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class MenuEdit(QtWidgets.QWidget):
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

        fileText = QtWidgets.QLabel("Edit")
        fileText.setObjectName("menuTitle")
        vMenu.addWidget(fileText)

        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(scrollLayWid)
        scroll.setWidgetResizable(True)
        vMenu.addWidget(scroll)

        #Add icons later!
        undo = QtWidgets.QPushButton("Undo")
        undo.setMaximumHeight(50)
        undo.setObjectName("scrollMenuItem")
        scrollLay.addWidget(undo)

        redo = QtWidgets.QPushButton("Redo")
        redo.setMaximumHeight(50)
        redo.setObjectName("scrollMenuItem")
        scrollLay.addWidget(redo)

        sep = menuSeperator.MenuSeperator()
        sep.setup()
        scrollLay.addWidget(sep)

        cut = QtWidgets.QPushButton("Cut")
        cut.setMaximumHeight(50)
        cut.setObjectName("scrollMenuItem")
        scrollLay.addWidget(cut)

        copy = QtWidgets.QPushButton("Copy")
        copy.setMaximumHeight(50)
        copy.setObjectName("scrollMenuItem")
        scrollLay.addWidget(copy)

        paste = QtWidgets.QPushButton("Paste")
        paste.setMaximumHeight(50)
        paste.setObjectName("scrollMenuItem")
        scrollLay.addWidget(paste)

        sep2 = menuSeperator.MenuSeperator()
        sep2.setup()
        scrollLay.addWidget(sep2)

        search = QtWidgets.QLineEdit("")
        search.setPlaceholderText("Search")
        search.setMinimumHeight(50)
        search.setObjectName("menuSearch")
        scrollLay.addWidget(search)

        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self.setLayout(vMenu)