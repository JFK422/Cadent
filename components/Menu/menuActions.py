from PyQt5 import QtGui, QtCore, QtWidgets
from components import introductionWindow
from components.Misc import directoryItem
from projectHandling import startupData
from components import create
import colorama as clr
import os

class MenuAction:
    #Menu file tab
    def newFile(self):
        print("new file")

    def openFile(self):
        print("open file")

    #Open a file selector in oder to open a project. Afterwards add it to the list, requires launch to be clicked afterwards
    def openProjectFromFile(self):
        print("menuActions; MenuAction; openProjectFromFile: open project from file")
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(self, "Open Project From File")
        if not(self.filePath[0] == ""):
            introductionWindow.Introduction.setProjectInfo(self, "fromFile", self.filePath[0])

    #Select the folder in which the project should be created
    def selectProjectFolder(self):
        print("menuActions; MenuAction; selectProjectFolder: selecting project folder")
        self.selectFilePath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder"))
        print(self.selectFilePath)
        if not(self.selectFilePath == ""):
            self.selectFilePath += "/"
            introductionWindow.Introduction.setProjectInfo(self, "fromCreate", self.selectFilePath)


    #Launch Button: Causes the project to be launched!
    def launchProject(self, prjSelectTabOpen, currentPos, prjPathList, prjNotFoundIndexList):
        print("menuActions; MenuAction; launchProject: Launching Project")
        intro = introductionWindow.Introduction
        #Check which tab was open and open the path.
        #Open one of the latest projects
        if prjSelectTabOpen:
            for i in range(len(prjNotFoundIndexList)):
                if currentPos == prjNotFoundIndexList[i]:
                    print(clr.Fore.RED + "menuActions; MenuAction; launchProject: Error launching project! No project defined!" + clr.Style.RESET_ALL)
                    MenuAction.showErrorDialog(self, "Error, no project found at location:\n{0}".format(prjPathList[currentPos]), "Undefined Project")
                    #figure the break out here!
                
                else:
                    #Open the project file and catch it if it cant be found in the designated path
                    #try:
                    print("sdf"+prjPathList[currentPos])
                    project = open(prjPathList[currentPos], "r+")
                    name = os.path.splitext(os.path.basename(prjPathList[currentPos]))[0]
                    startupData.Data.insert(self, name, prjPathList[currentPos])
                    project.close()
                    create.CreateUI.openProject = prjPathList[currentPos]
                    create.CreateUI.openProjectInEditor(self, "refresh")
                    self.hide()
                    break
                
                    """
                    except:
                        create.CreateUI.dial.setText("Selected file not found!")
                        create.CreateUI.dial.setIcon(QtWidgets.QMessageBox.Information)
                        create.CreateUI.dial.setWindowTitle("File Error")
                        create.CreateUI.dial.show()

                        print(clr.Fore.RED + "menuActions; MenuAction; launchProject: Project file not found!" + clr.Style.RESET_ALL)
                    """

        #Create a new project and open it
        else:
            name = intro.nameEdit.text()
            file = intro.pathEdit.text()
            if name != "" and file != "":
                #Add the new projet to the list of the latest projects
                try:
                    project = open(file + name + "/" + name + ".hthp", "w+")
                    os.makedirs(file + name + "/Assets")
                    mainFile = open(file + name + "/Assets/main" + ".hth", "w+")
                except:
                    os.makedirs(file + name + "/")
                    project = open(file + name + "/" + name + ".hthp", "w+")
                    os.makedirs(file + name + "/Assets")
                    mainFile = open(file + name + "/Assets/main" + ".hth", "w+")
                mainFile.close()
                os.makedirs(file + name + "/Resources")
                startupData.Data.insert(self, name, file + name + "/" + name + ".hthp")
                create.CreateUI.openProject = file + name + "/" + name + ".hthp"
                create.CreateUI.mainProjectFile = file + name + "/Assets/main" + ".hth"
                project.write("name={0}\n".format(name))
                project.write("assets={0}\n".format(file + name + "/Assets/"))
                project.write("mainFile={0}\n".format(file + name + "/Assets/main.hth"))
                project.write("projImg={0}".format(file + name + "/Resources/titleImg.jpg"))
                project.close()
                create.CreateUI.openProjectInEditor(self, "refresh")
                self.hide()

            else:
                print(clr.Fore.RED + "menuActions; MenuAction; launchProject: Error launching project! No name or path defined!" + clr.Style.RESET_ALL)
                MenuAction.showErrorDialog(self, "Error, no name or path defined!", "No name or path defined!")

    def showErrorDialog(self, message, title):
        infoDialog = QtWidgets.QMessageBox()
        infoDialog.setWindowTitle(title)
        infoDialog.setText(message)
        infoDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        dial = infoDialog.exec_()

    def saveFile(self, path):
        print("saving file @{0}".format(path))

    def saveAllFiles(self):
        print("save all files")

    def projectSettings(self):
        print("project settings")

    def editorSettings(self):
        print("editor settings")

    def switchProject(self):
        print("switch project")

    def createNewFile(self):
        print("menuActions; MenuAction; createnewFile: Creating new file!")
        create.CreateUI.openProjectInEditor(self, "create")
        #create.CreateUI.vFileExplorer.addWidget(item, Create.CreateUI.row, Create.CreateUI.index)