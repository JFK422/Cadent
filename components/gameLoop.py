import time
from components import glView, create
from PyQt5 import QtCore

#The Holy code of a threaded game loop.
#One shall not make any changes to the thread part of this file.
#N° of hours wasted on debugging/research: 11
class Loop(QtCore.QThread):
    exitFlag = False

    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def __del__(self):
        self.wait()

    def run(self):
        print("Starting game loop on thread: ", self.threadID, self.name)
        lastFrameTime = 0
        
        while True:
            if Loop.exitFlag:
                break

            # dt = time delta in seconds (float).
            currentTime = time.time()
            global dt
            dt = currentTime - lastFrameTime
            lastFrameTime = currentTime

            #Limit the framerate to the one set in the config
            #If the framerate setting is set to 0, there is no framerate limit
            fpsLimit = 0
            if fpsLimit != 0:
                sleepTime = 1/fpsLimit - dt
                if sleepTime > 0: time.sleep(sleepTime)

            print("FPS: ", 1/dt)

            glView.CreateArea.updateGL(self)