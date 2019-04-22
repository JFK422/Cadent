import sys, os
from PyQt5 import QtGui, QtCore, QtWidgets, QtOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#This is used to create the grid of the workarea for the scripting and some main functions
#Variables


class CreateArea(QtWidgets.QOpenGLWidget):
    def paintGL(self):
        CreateArea.Pyramid(self)
        """
        glTranslatef(0,0,-5)
        glColor3f(0.0, 0.0, 1.0)
        glRectf(-5, -5, 5, 5)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(20, 20, 0)
        glEnd()
        """


    def Pyramid(self):
        vertices=(
            (1,-1,-1),
            (1,1,-1),
            (-1,1,-1),
            (-1,-1,-1),
            (0,0,1))
        edges = (
            (0,1),
            (0,3),
            (0,4),
            (1,4),
            (1,2),
            (2,4),
            (2,3),
            (3,4))

        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
                glColor3f(0,1,0)
        glEnd()

    def updateGL(self):
        #glRotatef(2, 1, 1, 3)
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #CreateArea.Pyramid(self)
        print("PENIS!")

    #If the window gets resized the GLWidgets contents gets resized too
    def resizeGL(self, w, h):
        if min(w, h) < 0:
            return

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        glViewport(0, 0, w, h)
        gluPerspective(90, (w/h), 0.1, 50)

    #Create the GL workspace with a completely black background
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glShadeModel(GL_FLAT)
        glEnable(GL_DEPTH_TEST) #Objects at depth are rendered correctly
        glEnable(GL_CULL_FACE) #Backside of faces are transparent
        gluPerspective(90, (1920/1080), 0.1, 50) #FOV, Aspect Ratio (Convert to dynamic later), Z-Near, Z-Far (Clipping planes, objects disappear at diffrent distances)