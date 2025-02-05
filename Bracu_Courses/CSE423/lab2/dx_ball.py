from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

Window_Width, Window_Height = 500, 700

diamond_pos_x, diamond_pos_y = random.uniform(50, 450), 650
basket_pos_x, basket_pos_y = 250, 20
p_button_pos_x, p_button_pos_y = 250, 675
restart_button_pos_x, restart_button_pos_y = 0, 675
exit_button_pos_x, exit_button_pos_y = 450, 700
speed = 0.06
Total_score = 0
random_color = [random.uniform(0.7, 1.0), random.uniform(0.3, 1.0), random.uniform(0.9, 1.0)]
basket_colours_lst = [1, 1, 1]
play = True
Game_over = False
Total_score = 0


def OpenGL_cordinate(x, y):
    global Window_Width, Window_Height
    openGL_Cordinate_X = x
    openGL_Cordinate_Y = (Window_Height) - y
    return openGL_Cordinate_X, openGL_Cordinate_Y


def originalZone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def convertToZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def draw_line_raw(x1, y1, x2, y2, random_color):
    dx = x2 - x1
    dy = y2 - y1
    zone = 0
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy >= 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx >= 0 and dy < 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx < 0 and dy >= 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx >= 0 and dy < 0:
            zone = 6

    glColor3f(random_color[0], random_color[1], random_color[2])
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    x1, y1 = convertToZone0(x1, y1, zone)
    x2, y2 = convertToZone0(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x, y = x1, y1
    while x <= x2:
        if d <= 0:
            d += dE
        else:
            d += dNE
            y += 1
        original_x, original_y = originalZone(x, y, zone)
        glVertex2f(original_x, original_y)
        x += 1
    glEnd()


def diamond(x, y, random_color):
    draw_line_raw(x, y, x - 15, y - 20, random_color)
    draw_line_raw(x - 15, y - 20, x, y - 40, random_color)
    draw_line_raw(x, y - 40, x + 15, y - 20, random_color)
    draw_line_raw(x + 15, y - 20, x, y, random_color)


def basket(x, y, basket_colours_lst):
    draw_line_raw(x - 70, y, x + 70, y, basket_colours_lst)
    draw_line_raw(x - 40, 1, x + 40, 1, basket_colours_lst)
    draw_line_raw(x - 40, 1, x - 70, y, basket_colours_lst)
    draw_line_raw(x + 40, 1, x + 70, y, basket_colours_lst)


def exit(x, y, random_color):
    draw_line_raw(x, y, x + 50, y - 50, random_color)
    draw_line_raw(x, y - 50, x + 50, y, random_color)


def restart(x, y, random_color):
    draw_line_raw(x, y, x + 50, y, random_color)
    draw_line_raw(x, y, x + 20, y + 25, random_color)
    draw_line_raw(x, y, x + 20, y - 25, random_color)


def pause_play(x, y, random_color):
    if not play:
        draw_line_raw(x - 25, y + 25, x - 25, y - 25, random_color)
        draw_line_raw(x - 25, y + 25, x + 25, y, random_color)
        draw_line_raw(x - 25, y + 25, x + 25, y, random_color)
    else:
        draw_line_raw(x - 20, y + 25, x - 20, y - 25, random_color)
        draw_line_raw(x + 20, y + 25, x + 20, y - 25, random_color)


def keyboardListener(key, x, y):
    global play
    if key == b' ':
        play = not play
    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global basket_pos_x, basket_pos_y
    if not Game_over and play:
        if key == GLUT_KEY_RIGHT:
            if basket_pos_x + 70 <= 500:
                basket_pos_x += 10
        if key == GLUT_KEY_LEFT:
            if basket_pos_x - 70 >= 0:
                basket_pos_x -= 10


def mouseListener(button, state, x, y):
    global play, random_color, diamond_pos_x, diamond_pos_y, Game_over, speed, Total_score, basket_colours_lst
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        x, y = OpenGL_cordinate(x, y)
        if restart_button_pos_x <= x <= restart_button_pos_x + 50 and restart_button_pos_y - 25 <= y <= restart_button_pos_y + 25:
            if Game_over:
                play = True
                Game_over = False
                print("Game Starting")
                diamond_pos_x = random.uniform(100, 500)
                diamond_pos_y = 700
                speed = 0.06
                Total_score = 0
                basket_colours_lst = [1, 1, 1]
                random_color = [random.random(), random.random(), random.random()]
            else:
                play = True
                print("Game is restarting!")
                diamond_pos_x = random.uniform(50, 450)
                diamond_pos_y = 650
                speed = 0.06
                Total_score = 0
                random_color = [random.random(), random.random(), random.random()]
        if p_button_pos_x - 25 <= x <= p_button_pos_x + 25 and p_button_pos_y - 25 <= y <= p_button_pos_y + 25:
            if not Game_over:
                play = not play
        if exit_button_pos_x <= x <= exit_button_pos_x + 50 and exit_button_pos_y - 50 <= y <= exit_button_pos_y:
            print("Your Total Score is:", Total_score)
            glutLeaveMainLoop()
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    global diamond_pos_x, diamond_pos_y, basket_pos_x, basket_pos_y, random_color, basket_colours_lst, Game_over
    if not Game_over:
        diamond(diamond_pos_x, diamond_pos_y, random_color)
    basket(basket_pos_x, basket_pos_y, basket_colours_lst)
    exit(exit_button_pos_x, exit_button_pos_y, [1, 0, 0])
    restart(restart_button_pos_x, restart_button_pos_y, [0, 0, 1])
    pause_play(p_button_pos_x, p_button_pos_y, [0, 1, 0])
    glutSwapBuffers()


def animation():
    glutPostRedisplay()
    global diamond_pos_x, diamond_pos_y, speed, Total_score, random_color, basket_colours_lst, play, Game_over
    if play:
        if math.floor(diamond_pos_y - 45) == basket_pos_y and basket_pos_x - 75 < diamond_pos_x < basket_pos_x + 75:
            diamond_pos_x = random.uniform(100, 500)
            diamond_pos_y = 650
            speed += 0.02
            Total_score += 1
            random_color = [random.random(), random.random(), random.random()]
            print("Your Score:", Total_score)
        elif math.floor(diamond_pos_y - 40) > basket_pos_y:
            diamond_pos_y -= speed
        else:
            print("Game is Over! Your Score:", Total_score)
            Total_score = 0
            basket_colours_lst = [1, 0, 0]
            play = False
            Game_over = True


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)


glutInit()
glutInitWindowSize(Window_Width, Window_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"lab2")
init()

glutDisplayFunc(display)
glutIdleFunc(animation)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()
