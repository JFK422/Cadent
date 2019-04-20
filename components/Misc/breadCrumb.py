import createWorkarea
import qtawesome as qta
from components import introductionWindow
from PyQt5 import QtGui, QtCore, QtWidgets

#Tabwidget for the open files ontop of the editor

class Breadcrumb(QtWidgets.QWidget):
    bc = None
    def setup(self, name, path, itemIndex, bcType = ""):
        lay = QtWidgets.QHBoxLayout()
        Breadcrumb.bc = QtWidgets.QPushButton()

        self.path = path
        self.name = name
        self.index = itemIndex
        
        lay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        if bcType == "start":
            icon = qta.icon("fa.caret-right", color="#f9f9f9")
            Breadcrumb.bc.setIcon(icon)
            Breadcrumb.bc.setIconSize(QtCore.QSize(32, 32))
        else:
            Breadcrumb.bc.setText(name)
        Breadcrumb.bc.setMaximumHeight(51)
        Breadcrumb.bc.setMinimumWidth(160)
        Breadcrumb.bc.setObjectName("bcName")
        Breadcrumb.bc.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        #Breadcrumb.bc.clicked.connect(lambda:introductionWindow.Introduction.selectProject(self))

        self.setLayout(lay)
        lay.addWidget(Breadcrumb.bc)
        self.setMaximumWidth(150)