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
        motdVar = ["Hello Old Friend", 
                            "M' Lady", 
                            "Copy pasted Pseudocode", 
                            "Written in the language of snakes", 
                            "Has hidden ASCII art in the code", 
                            "The stylesheets consists mostly of linebreak } linebreak",
                            "This is my jam!",
                            "Digital Hug ༼つ ◕_◕ ༽つ",
                            "Full of stale memes",
                            "ಠ_ಠ",
                            "Insert cool phrase about programming here!"]
        self.setGeometry(200,200,650,500)
        self.setWindowTitle("Hitch")
        self.setFixedSize(QtCore.QSize(650,500))
        Introduction.center(self)

        #Create the layouts and their backbone widgets
        mainLay = QtWidgets.QVBoxLayout()
        mainLay.setAlignment(QtCore.Qt.AlignTop)
        mainLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        mainLay.setSpacing(0)

        titleLay = QtWidgets.QVBoxLayout()
        titleLay.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        titleLay.setContentsMargins(QtCore.QMargins(0,10,0,15))
        titleLayWid = QtWidgets.QWidget()
        titleLayWid.setObjectName("titlebar")
        titleLayWid.setLayout(titleLay)
        mainLay.addWidget(titleLayWid)

        hBottom = QtWidgets.QHBoxLayout()
        hBottom.setAlignment(QtCore.Qt.AlignTop)
        hBottom.setSpacing(5)
        hBottom.setContentsMargins(QtCore.QMargins(5,5,5,5))
        wBottom = QtWidgets.QWidget()
        wBottom.setLayout(hBottom)

        Introduction.vLastProjects = QtWidgets.QVBoxLayout()
        Introduction.vLastProjects.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        Introduction.vLastProjects.setContentsMargins(QtCore.QMargins(10,10,10,10))
        wLastProjects = QtWidgets.QWidget()
        wLastProjects.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding))
        wLastProjects.setMinimumWidth(170)
        wLastProjects.setObjectName("lastProjects")
        wLastProjects.setLayout(Introduction.vLastProjects)
        #hBottom.addWidget(wLastProjects)

        Introduction.sCenter = QtWidgets.QStackedLayout()
        Introduction.sCenter.setAlignment(QtCore.Qt.AlignTop)
        wCenter = QtWidgets.QWidget()
        wCenter.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))
        wCenter.setObjectName("lastProjects")
        wCenter.setLayout(Introduction.sCenter)

        vInfo = QtWidgets.QVBoxLayout()
        vInfo.setAlignment(QtCore.Qt.AlignTop)
        vInfo.setSpacing(0)
        vInfo.setContentsMargins(QtCore.QMargins(0,0,0,0))
        wInfo = QtWidgets.QWidget()
        wInfo.setLayout(vInfo)
        Introduction.sCenter.addWidget(wInfo)

        #Create the carousel with its items
        projList = Introduction.createCItems(self)[0]
        crl = carousel.Carousel()
        crl.setup(projList)
        vInfo.addWidget(crl)

        hBottom.addWidget(wCenter)

        hLaunch = QtWidgets.QVBoxLayout()
        hLaunch.setContentsMargins(QtCore.QMargins(10,10,10,10))
        wLaunch = QtWidgets.QWidget()
        wLaunch.setLayout(hLaunch)
        wLaunch.setObjectName("lastProjectsLaunch")

        launchBtn = QtWidgets.QPushButton("Launch")
        launchBtn.setObjectName("launchProject")
        launchBtn.clicked.connect(lambda:menuActions.MenuAction.launchProject(self, Introduction.prjSelectTabOpen, crl.getCurrentPos(), Introduction.createCItems(self)[1], Introduction.createCItems(self)[2]))
        hLaunch.addWidget(launchBtn)
        hBottom.addWidget(wLaunch)

        openBtn = QtWidgets.QPushButton("Open")
        openBtn.clicked.connect(lambda:menuActions.MenuAction.openProjectFromFile(self))
        hLaunch.addWidget(openBtn)

        Introduction.createBtn = QtWidgets.QPushButton("Create")
        Introduction.createBtn.clicked.connect(lambda:Introduction.switchTab(self))
        hLaunch.addWidget(Introduction.createBtn)

        gCreate = QtWidgets.QGridLayout()
        gCreate.setAlignment(QtCore.Qt.AlignTop)
        wCreate = QtWidgets.QWidget()
        wCreate.setLayout(gCreate)

        vBackLay = QtWidgets.QVBoxLayout()
        vBackLay.setAlignment(QtCore.Qt.AlignTop)
        vBackLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        wBackLay = QtWidgets.QWidget()
        wBackLay.setLayout(vBackLay)
        vBackLay.addWidget(wCreate)
        Introduction.sCenter.addWidget(wBackLay)

        #Stuff for the tab on creating a new project
        nameLabel = QtWidgets.QLabel("Name: ")
        nameLabel.setObjectName("infoText")

        Introduction.nameEdit = QtWidgets.QLineEdit()
        Introduction.nameEdit.setObjectName("projectTextEdit")
        Introduction.nameEdit.setMaximumWidth(200)

        pathLabel = QtWidgets.QLabel("Path: ")
        pathLabel.setObjectName("infoText")

        Introduction.pathEdit = QtWidgets.QLineEdit()
        Introduction.pathEdit.setObjectName("projectTextEdit")
        
        folder = qta.icon("fa.folder", color="#f9f9f9")
        pathSelect = QtWidgets.QPushButton(folder, "")
        pathSelect.setIconSize(QtCore.QSize(20, 20))
        pathSelect.setMaximumSize(QtCore.QSize(30, 30))
        pathSelect.clicked.connect(lambda:menuActions.MenuAction.selectProjectFolder(self))
        pathSelect.setObjectName("launchProject")

        infoLabel = QtWidgets.QLabel("Press launch to create the Project.")
        infoLabel.setObjectName("infoTextCreate")

        #Stitch everything together
        gCreate.addWidget(nameLabel, 0, 1)
        gCreate.addWidget(Introduction.nameEdit, 1, 1)
        gCreate.addWidget(pathLabel, 0, 0)
        gCreate.addWidget(Introduction.pathEdit, 1, 0)
        gCreate.addWidget(pathSelect, 1, 2)
        gCreate.addWidget(infoLabel, 3, 0)

        title = QtWidgets.QLabel("Hitch")
        title.setObjectName("titleText")
        titleLay.addWidget(title)

        motd = QtWidgets.QHBoxLayout()
        motd.setAlignment(QtCore.Qt.AlignCenter)
        motd.setContentsMargins(QtCore.QMargins(0,0,0,10))
        motdw = QtWidgets.QWidget()
        motdw.setObjectName("titlebar")
        motdw.setLayout(motd)
        mainLay.addWidget(motdw)

        label = QtWidgets.QLabel(motdVar[random.randint(0, len(motdVar) - 1)])
        label.setObjectName("greetText")
        motd.addWidget(label)

        mainLay.addWidget(wBottom)

        self.setLayout(mainLay)

    #Switch betwen the create and open project tabs
    def switchTab(self):
        if Introduction.prjSelectTabOpen:
            Introduction.sCenter.setCurrentIndex(1)
            Introduction.createBtn.setText("Last\nProjects")
            Introduction.prjSelectTabOpen = False
        else:
            Introduction.sCenter.setCurrentIndex(0)
            Introduction.createBtn.setText("Create")
            Introduction.prjSelectTabOpen = True

    #Open a dialog asking if the path to the project should be searched for or if the entry should be deleted
    def projNotFound(self, place):
        rmvDialog = QtWidgets.QMessageBox()
        rmvDialog.setWindowTitle("Remove Project?")
        rmvDialog.setText("This project can't be found anymore at {0}\n should it be removed from the list?".format(place))
        rmvDialog.setStandardButtons(QtWidgets.QMessageBox.Yes)
        rmvDialog.addButton(QtWidgets.QMessageBox.No)
        rmvDialog.setDefaultButton(QtWidgets.QMessageBox.Yes)
        if(rmvDialog.exec() == QtWidgets.QMessageBox.Yes):
            Introduction.removeProject(self, place)
    
    def removeProject(self, path):
        startupData.Data.removeItem(self, path)
        Introduction.addProjects(self)

    #Same function as in the index file which puts this window on the monitor where the mouse cursor is at
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    #Add the last opened projects as items and setup the carousel
    def createCItems(self):
        projList = []
        prjPathList = []
        nonExisting = []
        for i in range(startupData.Data.lengthOfDB(self)):
            try:
                fileTest = open(startupData.Data.readDB(self, i)[2], "r")
                projItem = carouselItem.CarouselItem()
                projItem.setup(name = startupData.Data.readDB(self, i)[1], path = startupData.Data.readDB(self, i)[2], existing = True)
                projList.append(projItem)
                prjPathList.append(startupData.Data.readDB(self, i)[2])
            except:
                projItem = carouselItem.CarouselItem()
                projItem.setup(name = startupData.Data.readDB(self, i)[1], path = startupData.Data.readDB(self, i)[2], existing = False)
                projList.append(projItem)
                prjPathList.append(startupData.Data.readDB(self, i)[2])
                nonExisting.append(i)
                print(clr.Fore.YELLOW + "introductionWindow; Introduction; __init__: Error finding project path!" + clr.Style.RESET_ALL)
        
        return projList, prjPathList, nonExisting


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