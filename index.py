import sys, os, sip, sqlite3, time
import qtawesome as qta
from components import create, gameLoop
from PyQt5 import QtGui, QtCore, QtWidgets, Qt

#This is the MAIN file of the app. Its used for handeling hte diffrent scripts within this programm.
#Debug prints are as formatted like this: FILE; CLASS; METHOD: MESSAGE

#Variables
app = None

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        #Set the windows porperties
        self.setGeometry(50,50,1920,1080)
        self.setWindowTitle("Cadent")

        create.CreateUI.create(self)

        #Center and maximize the window.
        self.center()
        self.showMaximized()
        self.show()

        print("Qt version:", QtCore.QT_VERSION_STR)
        print("PyQt version:", Qt.PYQT_VERSION_STR)
        print("SIP version:", sip.SIP_VERSION_STR)
        print("Sqlite3 module version;", sqlite3.version)
        print("Sqlite3 version:", sqlite3.sqlite_version)

    #Center the window on the monitor where the mouse cursor is
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    #Minimize and maximize methods for the new window action buttons
    def minimize(self):
        self.showMinimized()

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == '__main__':
    #Creating the QApplication
    app = QtWidgets.QApplication(sys.argv)

    #Set the main styling of the app
    #Yes its all canned in this file!
    with open("./resources/stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)

    #Set the app icon
    app_icon = QtGui.QIcon()
    app_icon.addFile('resources/icons/16x16.png', QtCore.QSize(16,16))
    app_icon.addFile('resources/icons/32x32.png', QtCore.QSize(32,32))
    app_icon.addFile('resources/icons/64x64.png', QtCore.QSize(64,64))
    app_icon.addFile('resources/icons/128x128.png', QtCore.QSize(128,128))
    app_icon.addFile('resources/icons/256x256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)
    
    #Misc stuff
    window = Window()
    sys.exit(app.exec_())