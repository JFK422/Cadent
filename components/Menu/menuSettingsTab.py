import qtawesome as qta
from components.Menu import menuSeperator
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class MenuSettings(QtWidgets.QWidget):
    selectedTab = "0"
    def setup(self):
        vMenu = QtWidgets.QVBoxLayout()
        vMenu.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        vMenu.setContentsMargins(QtCore.QMargins(20,20,20,20))

        hTabs = QtWidgets.QHBoxLayout()
        hTabs.setContentsMargins(QtCore.QMargins(0,0,0,0))

        vProject = QtWidgets.QVBoxLayout()
        vProject.setAlignment(QtCore.Qt.AlignTop)
        vProject.setContentsMargins(QtCore.QMargins(10,10,10,10))

        vEditor = QtWidgets.QVBoxLayout()
        vEditor.setAlignment(QtCore.Qt.AlignTop)
        vEditor.setContentsMargins(QtCore.QMargins(10,10,10,10))

        self.scrollLay = QtWidgets.QStackedLayout()
        self.scrollLay.setContentsMargins(QtCore.QMargins(10,10,10,10))
        self.scrollLay.setAlignment(QtCore.Qt.AlignTop)

        scrollLayWid = QtWidgets.QWidget()
        scrollLayWid.setObjectName("scrollMenuLay")
        scrollLayWid.setLayout(self.scrollLay)

        wProject = QtWidgets.QWidget()
        wProject.setLayout(vProject)
        self.scrollLay.addWidget(wProject)

        wEditor = QtWidgets.QWidget()
        wEditor.setLayout(vEditor)
        self.scrollLay.addWidget(wEditor)

        wTabs = QtWidgets.QWidget()
        wTabs.setObjectName("menuTabs")
        wTabs.setLayout(hTabs)

        fileText = QtWidgets.QLabel("Settings")
        fileText.setObjectName("menuTitle")
        vMenu.addWidget(fileText)

        self.projTab = QtWidgets.QPushButton("Project")
        self.projTab.setObjectName("openTab")
        self.projTab.setMaximumHeight(40)
        self.projTab.clicked.connect(lambda:MenuSettings.switchTab(self, "proj"))
        hTabs.addWidget(self.projTab)

        self.editTab = QtWidgets.QPushButton("Editor")
        self.editTab.setObjectName("normalTab")
        self.editTab.setMaximumHeight(40)
        self.editTab.clicked.connect(lambda:MenuSettings.switchTab(self, "edit"))
        hTabs.addWidget(self.editTab)
        vMenu.addWidget(wTabs)

        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(scrollLayWid)
        scroll.setWidgetResizable(True)
        vMenu.addWidget(scroll)

        #Add icons later! Also further additions may needed
        fileExplorer = QtWidgets.QPushButton("File Explorer")
        fileExplorer.setMaximumHeight(50)
        fileExplorer.setObjectName("scrollMenuItem")
        vEditor.addWidget(fileExplorer)

        closeAllEditors = QtWidgets.QPushButton("Close all Editors")
        closeAllEditors.setMaximumHeight(50)
        closeAllEditors.setObjectName("scrollMenuItem")
        vEditor.addWidget(closeAllEditors)

        console = QtWidgets.QPushButton("Show Console")
        console.setMaximumHeight(50)
        console.setObjectName("scrollMenuItem")
        vEditor.addWidget(console)

        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self.setLayout(vMenu)

    def switchTab(self, tab):
        MenuSettings.selectedTab = tab
        if tab == "proj":
            self.projTab.setStyleSheet("background-color: #e54f39; border-radius: 8px;")
            self.editTab.setStyleSheet("background-color: #ff634d; border-radius: 8px;")
            self.scrollLay.setCurrentIndex(0)
        elif tab == "edit":
            self.projTab.setStyleSheet("background-color: #ff634d; border-radius: 8px;")
            self.editTab.setStyleSheet("background-color: #e54f39; border-radius: 8px;")
            self.scrollLay.setCurrentIndex(1)
        else:
            print("menuSettingsTab; MenuSettings; switchTab: Error switching tab")