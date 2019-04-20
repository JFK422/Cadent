import qtawesome as qta
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class MenuSeperator(QtWidgets.QWidget):
    def setup(self):
        vMenu = QtWidgets.QVBoxLayout()
        vMenu.setContentsMargins(QtCore.QMargins(0,0,0,0))

        
        wid = QtWidgets.QWidget()
        wid.setObjectName("seperator")
        wid.setMinimumHeight(3)
        vMenu.addWidget(wid)

        self.setLayout(vMenu)

"""
            __
        .__( .)<  (Meow)
         \____)
~~~~~~~~~~~~~~~~~~~~~~~
"""