# Importación de módulos

import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def escenario():
    
    piso()
    
    #glMatrixMode(GL_MODELVIEW)
    #glPushMatrix()
    #glTranslatef(1.5, 2, -1)
    #cuboMulticolor()
    #glPopMatrix()

    #glMatrixMode(GL_MODELVIEW)
    #glPushMatrix()
    #glTranslatef(-1.5, -2, 1)
    #colorPurple = [0.5, 0, 0.5]
    #cuboMonocolor(colorPurple)
    #glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()    
    glScalef(0.1, 0.1, 0.1) ## hace 10 veces más pequeño en ejes x, y, z
    #dibujarComposicionMesaSillas()
    dibujarComposicionMesaGrandeConSillas()
    glPopMatrix()


def dibujarComposicionMesaGrandeConSillas():
    glMatrixMode(GL_MODELVIEW)

    # Dibujar la mesa grande en el centro
    glPushMatrix()
    dibujarMesaGrande()  # La mesa se dibuja centrada en el origen
    glPopMatrix()

    # Dimensiones y posición para las sillas
    distancia_lado_ancho = 25  # Distancia desde el centro de la mesa hasta las sillas en los lados anchos
    distancia_lado_estrecho = 12  # Distancia desde el centro hasta las sillas en los lados estrechos
    separacion_sillas = 15  # Separación entre las dos sillas en los lados anchos

    # Posiciones de las sillas (incluyendo las rotaciones)
    posiciones_sillas = [
        # Sillas en los lados anchos (dos por lado)
        [distancia_lado_ancho/2, 0, distancia_lado_estrecho, 180],
        [distancia_lado_ancho/2, 0, -distancia_lado_estrecho, 0],
        [-distancia_lado_ancho/2, 0, distancia_lado_estrecho, 180],
        [-distancia_lado_ancho/2, 0, -distancia_lado_estrecho, 0],        

        # Sillas en los lados estrechos (una por lado)
        [distancia_lado_ancho, 0, 0, -90],  # Atrás
        [-distancia_lado_ancho, 0, 0, 90]   # Adelante

    ]

    # Dibujar cada silla
    for posicion in posiciones_sillas:
        glPushMatrix()
        glTranslatef(posicion[0], posicion[1], posicion[2])  # Colocar la silla alrededor de la mesa
        glRotatef(posicion[3], 0, 1, 0)  # Rotación en el eje Y de la silla
        dibujarSilla()  # Dibujar la silla
        glPopMatrix()



def dibujarComposicionMesaSillas():
    glMatrixMode(GL_MODELVIEW)
    
    # Dibujar la mesa en el centro
    glPushMatrix()
    dibujarMesa()  # Asumimos que la mesa está centrada en el origen
    glPopMatrix()

    # Dimensiones y posición para las sillas
    distancia_sillas = 15  # Distancia entre el centro de la mesa y las sillas
    posiciones_sillas = [
        [0, 0, distancia_sillas, 180],   # Frente
        [0, 0, -distancia_sillas, 0],  # Detrás
        [-distancia_sillas, 0, 0, 90],  # Izquierda
        [distancia_sillas, 0, 0, -90]    # Derecha
    ]

    # Dibujar cada silla
    for posicion in posiciones_sillas:
        glPushMatrix()
        glTranslatef(posicion[0], posicion[1], posicion[2])  # Colocar la silla alrededor de la mesa
        glRotatef(posicion[3], 0, 1, 0)
        dibujarSilla()  # Dibujar la silla
        glPopMatrix()

def dibujarMesaGrande():
    glMatrixMode(GL_MODELVIEW)

    # Color para las patas de la mesa
    color_marron = [0.65, 0.32, 0.17]

    altura = 15  # Altura de la mesa
    largo_mesa = 50  # Largo de la mesa
    ancho_mesa = 20  # Ancho de la mesa

    # Dibujar las patas en y = 0, desplazadas en altura/2 para que queden en el piso
    glPushMatrix()
    glTranslatef(0, altura / 2, 0)

    # Coordenadas de las 4 patas (en las esquinas)
    posiciones_patas = [
        [-largo_mesa / 2 + 2, 0, ancho_mesa / 2 - 2],  # Esquina inferior izquierda
        [largo_mesa / 2 - 2, 0, ancho_mesa / 2 - 2],   # Esquina inferior derecha
        [-largo_mesa / 2 + 2, 0, -ancho_mesa / 2 + 2], # Esquina superior izquierda
        [largo_mesa / 2 - 2, 0, -ancho_mesa / 2 + 2]   # Esquina superior derecha
    ]

    # Dibujar cada pata
    for posicion in posiciones_patas:
        glPushMatrix()
        glTranslatef(posicion[0], posicion[1], posicion[2])  # Posicionar la pata
        apilarCubosColorRand(color_marron, 0.1, 1, 15, 1)  # Dibujar una columna de cubos
        glPopMatrix()

    glPopMatrix()  # Fin del desplazamiento de las patas en altura / 2

    # Dibujar la tabla de la mesa
    glPushMatrix()
    glTranslatef(0, altura - 0.5, 0)  # Elevar la tabla para que quede encima de las patas
    apilarCubosColorRand(color_marron, 0.1, largo_mesa, 1, ancho_mesa)  # Dibujar la tabla con un plano de cubos
    glPopMatrix()


def dibujarMesa():

    glMatrixMode(GL_MODELVIEW)
    
    # Color para las patas de la mesa
    color_marron = [0.65, 0.32, 0.17]

    altura = 15  # Altura de la mesa

    # Dibujar las patas en y = 0, como se dibujan centradas en el origen, se desplazan en altura/2 para que queden en el piso
    glPushMatrix()
    glTranslatef(0, altura / 2, 0)

    # Coordenadas de las 4 patas (en las esquinas)
    posiciones_patas = [
        [-8, 0, 5],  # Esquina inferior izquierda
        [8, 0, 5],   # Esquina inferior derecha
        [-8, 0, -5], # Esquina superior izquierda
        [8, 0, -5]   # Esquina superior derecha
    ]

    # Dibujar cada pata
    for posicion in posiciones_patas:
        glPushMatrix()
        glTranslatef(posicion[0], posicion[1], posicion[2])  # Posicionar la pata
        apilarCubosColorRand(color_marron, 0.1, 1, 15, 1)  # Dibujar una columna de cubos
        glPopMatrix()

    glPopMatrix() # del desplazamiento de las patas en altura/2

    # Dibujar la tabla de la mesa
    glPushMatrix()
    glTranslatef(0, altura-0.5, 0)  # Elevar la tabla para que quede encima de las patas
    apilarCubosColorRand(color_marron, 0.1, 25, 1, 15)  # Dibujar la tabla con un plano de cubos
    glPopMatrix()

def dibujarSilla():
    glMatrixMode(GL_MODELVIEW)
    
    # Color para las patas y la estructura de la silla
    color_marron = [0.65, 0.32, 0.17]
    color_gris_oscuro = [0.2, 0.2, 0.2]
    color_gris = [0.4, 0.4, 0.4]

    altura_asiento = 10  # Altura del asiento de la silla
    altura_respaldo = 15  # Altura adicional para el respaldo
    ancho_silla = 10  # Ancho de la silla
    profundidad_silla = 10  # Profundidad de la silla

    # Dibujar las patas (en y = 0), desplazadas en altura_asiento/2 para que queden en el piso
    glPushMatrix()
    glTranslatef(0, altura_asiento / 2, 0)

    # Coordenadas de las 4 patas (en las esquinas)
    posiciones_patas = [
        [-ancho_silla / 2 + 1, 0, profundidad_silla / 2 - 1],  # Esquina inferior izquierda
        [ancho_silla / 2 - 1, 0, profundidad_silla / 2 - 1],   # Esquina inferior derecha
        [-ancho_silla / 2 + 1, 0, -profundidad_silla / 2 + 1], # Esquina superior izquierda
        [ancho_silla / 2 - 1, 0, -profundidad_silla / 2 + 1]   # Esquina superior derecha
    ]

    # Dibujar cada pata
    for posicion in posiciones_patas:
        glPushMatrix()
        glTranslatef(posicion[0], posicion[1], posicion[2])  # Posicionar la pata
        apilarCubosColorRand(color_marron, 0.1, 1, altura_asiento, 1)  # Dibujar una columna de cubos
        glPopMatrix()

    glPopMatrix()  # Fin del desplazamiento de las patas en altura_asiento / 2

    # Dibujar el asiento de la silla
    glPushMatrix()
    glTranslatef(0, altura_asiento - 0.5, 0)  # Elevar el asiento para que quede encima de las patas
    apilarCubosColorRand(color_gris_oscuro, 0.1, ancho_silla, 1, profundidad_silla)  # Dibujar el asiento como un plano
    glPopMatrix()

    # Dibujar el respaldo de la silla
    glPushMatrix()
    glTranslatef(0, altura_asiento + altura_respaldo / 2 - 0.5, -profundidad_silla / 2 + 0.5)  # Posicionar el respaldo
    apilarCubosColorRand(color_gris, 0.1, ancho_silla, altura_respaldo, 1)  # Dibujar el respaldo como un plano vertical
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

def apilarCubosColorRand(color_base=[0.65, 0.32, 0.17], variabilidad=0.1, x=0, y=10, z=0):
    """
    Dibuja una estructura de cubos centrada en el eje de coordenadas.
    :param color_base: Color base para los cubos en formato RGB.
    :param variabilidad: Variabilidad en el color base (como porcentaje).
    :param x: Número de cubos en el eje X (columnas).
    :param y: Número de cubos en el eje Y (filas).
    :param z: Número de cubos en el eje Z (profundidad).
    """
    # Calcular el desplazamiento inicial para centrar la estructura
    offset_x = -(x - 1) * 0.5 if x > 0 else 0  # Centrar en X
    offset_y = -(y - 1) * 0.5 if y > 0 else 0  # Centrar en Y
    offset_z = -(z - 1) * 0.5 if z > 0 else 0  # Centrar en Z

    for i in range(y):
        for j in range(x if x > 0 else 1):  # Si x > 0 genera filas en el plano
            for k in range(z if z > 0 else 1):  # Si z > 0 genera profundidad
                # Si z=10, generamos un cubo hueco dejando vacío el interior
                if z == 10 and x == 10 and y == 10:
                    if not (i == 0 or i == y - 1 or j == 0 or j == x - 1 or k == 0 or k == z - 1):
                        continue  # Ignorar los cubos internos

                # Generar color aleatorio dentro del rango ±variabilidad% del color base
                color_variado = [
                    max(0.0, min(1.0, color_base[0] * (1 + random.uniform(-variabilidad, variabilidad)))),  # R
                    max(0.0, min(1.0, color_base[1] * (1 + random.uniform(-variabilidad, variabilidad)))),  # G
                    max(0.0, min(1.0, color_base[2] * (1 + random.uniform(-variabilidad, variabilidad))))   # B
                ]

                glPushMatrix()  # Guardar el estado actual de la matriz
                # Desplazar los cubos considerando el offset para centrarlos
                glTranslatef(offset_x + j * 1.0, offset_y + i * 1.0, offset_z + k * 1.0)
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
