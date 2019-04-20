import qtawesome as qta
from components.Menu import menuSeperator
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class MenuRun(QtWidgets.QWidget):
    def setup(self):
        vMenu = QtWidgets.QVBoxLayout()
        vMenu.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        vMenu.setContentsMargins(QtCore.QMargins(20,20,20,20))

        hSettings = QtWidgets.QHBoxLayout()
        hSettings.setContentsMargins(QtCore.QMargins(0,0,0,0))

        self.scrollLay = QtWidgets.QVBoxLayout()
        self.scrollLay.setContentsMargins(QtCore.QMargins(10,10,10,10))
        self.scrollLay.setAlignment(QtCore.Qt.AlignTop)

        self.scrollLayWid = QtWidgets.QWidget()
        self.scrollLayWid.setObjectName("console")
        self.scrollLayWid.setLayout(self.scrollLay)

        wSettings = QtWidgets.QWidget()
        wSettings.setLayout(hSettings)

        fileText = QtWidgets.QLabel("Run File")
        fileText.setObjectName("menuTitle")
        vMenu.addWidget(fileText)
        vMenu.addWidget(wSettings)

        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(self.scrollLayWid)
        scroll.setWidgetResizable(True)
        vMenu.addWidget(scroll)

        #Add icons later!
        chooser = QtWidgets.QComboBox()
        chooser.setMaximumHeight(40)
        chooser.addItem("Test")
        chooser.addItem("Test2")
        chooser.setObjectName("menuRunChooser")
        hSettings.addWidget(chooser)

        runBtn = QtWidgets.QPushButton("Run File")
        runBtn.setMaximumHeight(40)
        runBtn.setObjectName("scrollMenuItem")
        hSettings.addWidget(runBtn)

        for i in range (100):
            testText = QtWidgets.QLabel("Play of the Game: JFK422")
            testText.setObjectName("consoleText")
            self.scrollLay.addWidget(testText)

        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self.setLayout(vMenu)