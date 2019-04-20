import sys, os
from appearance import style
from PyQt5 import QtGui, QtCore, QtWidgets, QtOpenGL
from OpenGL import GL, GLU

#This is used to create the grid of the workarea for the scripting and some main functions
#Variables


class createArea(QtWidgets.QOpenGLWidget):
    def paintGL(self):
        GL.glColor3f(0.0, 0.0, 1.0)
        GL.glRectf(-5, -5, 5, 5)
        GL.glColor3f(1.0, 0.0, 0.0)
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(20, 20, 0)
        GL.glEnd()

    def resizeGL(self, w, h):
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        GL.glViewport(0, 0, w, h)

    def initializeGL(self):
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

class editorActions:
    def switchFile(self, filepath):
        print("createWorkarea; editorActions; switchFile: Switching to file: {0}".format(filepath))
        
    def closeFile(self, filepath):
        print("createWorkarea; editorActions; closeFile: Closing file: {0}".format(filepath))

"""
if __name__ == '__main__':
    app = QtWidgets.QApplication(["Winfred's PyQt OpenGL"])
    widget = createArea()
    widget.show()
    app.exec_()
"""