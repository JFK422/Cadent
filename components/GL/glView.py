import sys, os
from PyQt5 import QtGui, QtCore, QtWidgets, QtOpenGL
from components.GL import vertexBuffer
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#This is used to create the grid of the workarea for the scripting and some main functions
#Variables


class CreateArea(QtWidgets.QOpenGLWidget):

    vertices = [
        -0.5, 0.5, 0,
        -0.5, -0.5, 0,
        0.5, -0.5, 0,
        0.5, -0.5, 0,
        0.5, 0.5, 0,
        -0.5, 0.5, 0]

    def paintGL(self):
        print("DRAWING")
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        model = vertexBuffer.Buffer.loadToVAO(self, CreateArea.vertices)
        glBindVertexArray(model[0])
        glEnableVertexAttribArray(0)
        glDrawArrays(GL_TRIANGLES, 0, model[1])
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)


    #If the window gets resized the GLWidgets contents gets resized too
    def resizeGL(self, w, h):
        if min(w, h) < 0:
            return

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glViewport(0, 0, w, h)
        gluPerspective(90, (w/h), 0.1, 50) #FOV, Aspect Ratio (Convert to dynamic later), Z-Near, Z-Far (Clipping planes

    #Create the GL workspace with a completely black background
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glShadeModel(GL_FLAT) #Render everthing flat. There is no shading
        glEnable(GL_DEPTH_TEST) #Objects at depth are rendered correctly
        glEnable(GL_CULL_FACE) #Backside of faces are transparent
        gluPerspective(90, (1920/1080), 0.1, 50) #FOV, Aspect Ratio (Convert to dynamic later), Z-Near, Z-Far (Clipping planes)
        glLoadIdentity()
        glTranslatef(0, 0, 0) #Start @ 0,0,0
        glMatrixMode(GL_MODELVIEW)






class Pyramid:
    vertices = [
        [1, -1, -1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, -1, -1],
        [0, 1, 0]
    ]

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (1, 4),
        (1, 2),
        (2, 4),
        (2, 3),
        (3, 4)
    )

    def __init__(self):
        self.edges = Pyramid.edges
        self.vertices = Pyramid.vertices

    def draw(self):
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(0, 1, 0)
        glEnd()