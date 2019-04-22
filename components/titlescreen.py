import qtawesome as qta
import colorama as clr
import random, sys, os
from projectHandling import startupData
from components.Misc import projectItem
from components.Menu import menuActions
from components.carousel import carousel
from components.carousel import carouselItem
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu shown on startup used to select a project

class Introduction(QtWidgets.QWidget):
    #Variables for some recursion, idk how to do it otherwise!
    vLastProjects = None
    prjSelectTabOpen = True
    createBtn = None
    nameEdit = None
    
    #Init the window
    def __init__(self):
        super(Introduction, self).__init__()
        #Add your own motd here!
        motdList = ["Hello Old Friend", 
                            "M' Lady", 
                            "Copy pasted Pseudocode", 
                            "Written in the language of snakes", 
                            "Has hidden ASCII art in the code",
                            "This is my jam!",
                            "Digital Hug ༼つ ◕_◕ ༽つ",
                            "Full of stale memes",
                            "ಠ_ಠ",
                            "Insert cool phrase about programming here!",
                            "Falling into limbo"]

        #Create the layouts and their backbone widgets
        mainLay = QtWidgets.QVBoxLayout()
        mainLay.setAlignment(QtCore.Qt.AlignTop)
        mainLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        mainLay.setSpacing(0)

        motd = QtWidgets.QLabel(random(motdList))

        self.setLayout(mainLay)


#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    #Set the main styling of dis window aswell
    with open("../appearance/style/stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)
    gui = Introduction()
    gui.show()
    app.exec_()