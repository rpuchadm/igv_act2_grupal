# Importación de módulos

import random
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

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glTranslatef(-0.5, -1, 2)
    # Color marrón en formato RGB
    color_marron = [0.65, 0.32, 0.17]
    apilarCubosColorRand(color_marron)
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

def apilarCubosColorRand(color_base = [0.65, 0.32, 0.17]):

    variabilidad = 0.1  # ±10% de variabilidad en cada componente RGB
    
    # Iterar para apilar 10 cubos
    for i in range(10):
        # Generar un color aleatorio dentro del rango ±variabilidad% del color base
        color_variado = [
            max(0.0, min(1.0, color_base[0] * (1 + random.uniform(-variabilidad, variabilidad)))),  # R
            max(0.0, min(1.0, color_base[1] * (1 + random.uniform(-variabilidad, variabilidad)))),  # G
            max(0.0, min(1.0, color_base[2] * (1 + random.uniform(-variabilidad, variabilidad))))   # B
        ]
        
        glPushMatrix()  # Guardar el estado actual de la matriz
        glTranslatef(0.0, i * 1.0, 0.0)  # Desplazar cada cubo hacia arriba (en Y) con un espacio de 1.0 entre ellos
        cuboMonocolor(color_variado)  # Dibujar el cubo con el color variado
        glPopMatrix()  # Restaurar el estado de la matriz    

def apilarCubos():
    # Color marrón en formato RGB
    color_marron = [0.65, 0.32, 0.17]
    
    # Iterar para apilar 10 cubos
    for i in range(10):
        glPushMatrix()  # Guardar el estado actual de la matriz
        glTranslatef(0.0, i * 1.0, 0.0)  # Desplazar cada cubo hacia arriba (en Y) con un espacio de 1.0 entre ellos
        cuboMonocolor(color_marron)  # Dibujar el cubo
        glPopMatrix()  # Restaurar el estado de la matriz


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

