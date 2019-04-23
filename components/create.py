import sys, os, index
import qtawesome as qta
from PyQt5 import QtGui, QtCore, QtWidgets
from components import dab, gameLoop
from components.GL import glView

#This is the main file which is used for creating the window.

class CreateUI:
    def create(self):
        #Layouts
        vMain = QtWidgets.QVBoxLayout() #Backbone lay, important because of the titlebar

        #Alignment
        #vMain.setAlignment(QtCore.Qt.AlignTop)

        #Margin
        vMain.setContentsMargins(QtCore.QMargins(0,0,0,0))

        #Add the main glView
        global wWorkarea
        wWorkarea = glView.CreateArea()

        btn = QtWidgets.QPushButton("Start")
        btn.clicked.connect(lambda:CreateUI.initGameLoop(self))
        vMain.addWidget(btn)

        vMain.addWidget(wWorkarea)

        dab.DatabaseActions.connect(self)

        self.setLayout(vMain)
    
    def initGameLoop(self):
        self.loop = gameLoop.Loop(1, "gameLoopThread")
        self.loop.updateSig.connect(lambda:glView.CreateArea.update(wWorkarea))
        self.loop.start()

    def stopGameLoop(self):
        gameLoop.Loop.exitFlag = True