from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 

random_points = []
speed_constant = 0.1
freeze_constant = 0 
horizontal_x_speed = random.uniform(0.2, 0.9)
vertical_y_speed = random.uniform(0.2, 0.9)

point_blink = False
freeze_point = False
freeze_handler = []

def draw_points(x, y, color):
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(x, y)
    glEnd()

def point_with_speed():
    global speed_constant, freeze_constant

    for i in random_points:
        if not freeze_point: 
            i['x'] += (speed_constant * horizontal_x_speed)
            i['y'] += (speed_constant * vertical_y_speed)
        else:
            i['x'] += (freeze_constant * horizontal_x_speed)
            i['y'] += (freeze_constant * vertical_y_speed)

def new_points():
    x = random.uniform(100, 450)
    y = random.uniform(100, 450)
    return x, y

def new_color():
    return [random.random(), random.random(), random.random()]

def mouseListener(button, state, x, y):
    global point_blink, freeze_point

    if not freeze_point:
        if (button == GLUT_RIGHT_BUTTON) and (state == GLUT_DOWN):
            point_blink = False 
            print("New point in random coordinate")
            new_x, new_y = new_points()
            color = new_color()
            random_points.append({'x': new_x, 'y': new_y, 'color': color})
        
        if (button == GLUT_LEFT_BUTTON) and (state == GLUT_DOWN):
            point_blink = True 
            print("Point is Blinking")
        
        glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed_constant

    if not freeze_point:
        if key == GLUT_KEY_UP:
            speed_constant *= 1.5
            print("Increased Speed By", speed_constant)
            
        if key == GLUT_KEY_DOWN:
            speed_constant /= 1.5
            print("Decreased Speed By", speed_constant)
    
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global freeze_point, freeze_handler

    if key == b' ':
        freeze_handler.append("Freezing the point")
    
    if len(freeze_handler) == 1:
        print("Freeze!!!")
        freeze_point = True 
    else:
        print("UnFreeze Points")
        freeze_point = False 
        freeze_handler.clear()
    
    glutPostRedisplay()

def animate():
    if not freeze_point:
        point_with_speed()

    glutPostRedisplay()

def continious():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    continious()

    for point in random_points:
        x, y = point['x'], point['y']
        color = point['color'] if not point_blink else [0.0, 0.0, 0.0]
        draw_points(x, y, color)

    glutSwapBuffers()

glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE) 

wind = glutCreateWindow(b"Lab Assignment 1 Task 2: Building the Amazing Box")
glutDisplayFunc(display)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutIdleFunc(animate)
glutMainLoop()
