from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

display_background = (0.0, 0.0, 0.0, 0.0)
rain_drop_angle = 0.0
raindrops_coordinates = []

def raindrop_design(x1, y1):
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    glEnd()


def all_raindrops():
    global rain_drop_angle
    for i in range(len(raindrops_coordinates)):
        x, y = raindrops_coordinates[i]
        x += rain_drop_angle
        y -= 5 

        
        if y < 0 or (120 < x < 380 and 100 < y < 300):
            x = random.uniform(0, 500)
            y = random.uniform(400, 600) 

        raindrops_coordinates[i] = (x, y)




def build_house():
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5)
    glLineWidth(5)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)

    # Roof
    glVertex2f(400, 300)
    glVertex2f(100, 300)
    glVertex2f(400, 300)
    glVertex2f(250, 400)
    glVertex2f(100, 300)
    glVertex2f(250, 400)

    # Walls
    glVertex2f(380, 300)
    glVertex2f(380, 100)
    glVertex2f(120, 300)
    glVertex2f(120, 100)
    glVertex2f(120, 100)
    glVertex2f(380, 100)
    glEnd()

    glPointSize(5)
    glLineWidth(2)
    glBegin(GL_LINES)

    # Door
    glVertex2f(140, 100)
    glVertex2f(140, 200)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(140, 200)
    glVertex2f(200, 200)

    # Window
    glVertex2f(350, 200)
    glVertex2f(350, 250)
    glVertex2f(300, 200)
    glVertex2f(300, 250)
    glVertex2f(350, 250)
    glVertex2f(300, 250)
    glVertex2f(350, 200)
    glVertex2f(300, 200)
    glVertex2f(300, 225)
    glVertex2f(350, 225)
    glVertex2f(325, 250)
    glVertex2f(325, 200)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
   
    # Door knob
    glVertex2f(190, 120)
    glEnd()

def specialKeyListener(key, x, y):
    global rain_drop_angle
    if key == GLUT_KEY_RIGHT:
        rain_drop_angle += 1
        print("Slightly bending the rainfall to the right")
    if key == GLUT_KEY_LEFT:
        rain_drop_angle -= 1
        print("Slightly bending the rainfall to the left")

    glutPostRedisplay()

def keyboardListener(key, x, y):
    global display_background
    if key == b"b":
        display_background = (0.0, 0.0, 0.0, 0.0)
    if key == b"w":
        display_background = (1.0, 1.0, 1.0, 0.0)
    glutPostRedisplay()

def animate():
    all_raindrops()
    glutPostRedisplay()

def continious():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClearColor(*display_background)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    continious()
    build_house()
    for drops in raindrops_coordinates:
        raindrop_design(drops[0], drops[1])
    glutSwapBuffers()

glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE) 

wind = glutCreateWindow(b"Lab Assignment 1 Task 1: House with Rain Drop")

glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

for cordinates in range(100):
    x2 = random.uniform(100, 400)
    y2 = random.uniform(200, 500)
    raindrops_coordinates.append((x2, y2))

glutMainLoop()
