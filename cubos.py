# Importación de módulos

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def escenario():
    
    piso()
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glTranslatef(1.5, 2, -1)
    cuboMulticolor()
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glTranslatef(-1.5, -2, 1)
    colorPurple = [0.5, 0, 0.5]
    cuboMonocolor(colorPurple)
    glPopMatrix()


def piso():

    y = -0.5
    half_edge = 2.5
    # PISO
    glColor3f(0.5, 0.5, 0.5) # Gris
    glBegin(GL_QUADS)
    glVertex3f(-half_edge, y, -half_edge)
    glVertex3f(-half_edge, y, half_edge)
    glVertex3f(half_edge, y, half_edge)
    glVertex3f(half_edge, y, -half_edge)
    glEnd()


def cuboMonocolor( color):

    he = 0.5   # semilado del cubo (half-edge)
    
    v1 = [-he, -he, he]
    v2 = [-he, he, he]
    v3 = [he, -he, he]
    v4 = [he, he, he]
    v5 = [he, -he, -he]
    v6 = [he, he,-he]
    v7 = [-he, he, -he]
    v8 = [-he, -he, -he]
    
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON);
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v4)
    glVertex3fv(v3)
    glEnd()
    
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    glVertex3fv(v5)
    glVertex3fv(v6)
    glVertex3fv(v7)
    glVertex3fv(v8)
    glEnd()
    
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    glVertex3fv(v3)
    glVertex3fv(v4)
    glVertex3fv(v6)
    glVertex3fv(v5)
    glEnd()
    
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v7)
    glVertex3fv(v8)
    glEnd()
    
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    glVertex3fv(v2)
    glVertex3fv(v4)
    glVertex3fv(v6)
    glVertex3fv(v7)
    glEnd()
    
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    glVertex3fv(v1)
    glVertex3fv(v3)
    glVertex3fv(v5)
    glVertex3fv(v8)
    glEnd()

def cuboMulticolor():

    he = 0.5   # semilado del cubo (half-edge)
    
    v1 = [-he, -he, he]
    v2 = [-he, he, he]
    v3 = [he, -he, he]
    v4 = [he, he, he]
    v5 = [he, -he, -he]
    v6 = [he, he,-he]
    v7 = [-he, he, -he]
    v8 = [-he, -he, -he]
    
    # CARA FRONTAL: NARANJA
    glColor3f(255/255, 165/255, 0/255)
    glBegin(GL_POLYGON);
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v4)
    glVertex3fv(v3)
    glEnd()
    
    # CARA POSTERIOR: ROJA
    glColor3f(255/255, 0/255, 0/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v5)
    glVertex3fv(v6)
    glVertex3fv(v7)
    glVertex3fv(v8)
    glEnd()
    
    # CARA DERECHA: VERDE
    glColor3f(0/255, 255/255, 0/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v3)
    glVertex3fv(v4)
    glVertex3fv(v6)
    glVertex3fv(v5)
    glEnd()
    
    # CARA IZQUIERDA: AZUL
    glColor3f(0/255, 0/255, 255/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v7)
    glVertex3fv(v8)
    glEnd()
    
    # CARA SUPERIOR: AMARILLO
    glColor3f(255/255, 255/255, 0/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v2)
    glVertex3fv(v4)
    glVertex3fv(v6)
    glVertex3fv(v7)
    glEnd()
    
    # CARA INFERIOR: ROSA
    glColor3f(255/255, 0/255, 255/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v1)
    glVertex3fv(v3)
    glVertex3fv(v5)
    glVertex3fv(v8)
    glEnd()

