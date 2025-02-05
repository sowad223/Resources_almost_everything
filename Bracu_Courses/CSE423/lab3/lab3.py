from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

W_Width, W_Height = 500, 700

zones = []
score = 0
counter = 0
shooter_pos_x , shooter_pos_y = 250, 20
p_pos_x, p_pos_y = 250, 675
return_pos_x, return_pos_y = 0, 675
exit_pos_x, exit_pos_y = 450, 700
fire_pos_x, fire_pos_y = shooter_pos_x, 2*shooter_pos_y+5
missed_shots_counter = 0
missed_fire_counter = 0
Check_shoot = False
game_play = True
endgame = False
balls = []
x = random.uniform(50, 450)
y = random.randint(625, 640)
balls.append([x, y, 650-y])


def OpenGL_cordinate(x,y):
    global W_Width, W_Height
    openGL_Cordinate_X = x 
    openGL_Cordinate_Y = (W_Height) - y 
    return openGL_Cordinate_X , openGL_Cordinate_Y
    
    
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
    
    
def draw_line_raw(x1, y1, x2, y2, color):
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
    glColor3f(color[0], color[1], color[2])
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
    while x < x2:
        if d <= 0:
            d += dE
            x += 1
        else:
            d += dNE
            x += 1
            y += 1
        original_x , original_y = originalZone(x, y, zone)
        glVertex2f(original_x, original_y)
    glEnd()
    
    
def draw_exit_button(x, y, color):
    draw_line_raw(x, y, x+50, y-50, color)
    draw_line_raw(x, y-50, x+50, y, color)


def draw_return_button(x, y, color):
    draw_line_raw(x, y, x+50, y, color)
    draw_line_raw(x, y, x+20, y+25, color)
    draw_line_raw(x, y, x+20, y-25, color) 
    
    
def draw_pause_play_button(x, y, color):
    if not game_play:
        draw_line_raw(x-25, y+25, x-25, y-25, color)
        draw_line_raw(x-25, y+25, x+25, y, color)
        draw_line_raw(x-25, y-25, x+25, y, color)
    if game_play:
        draw_line_raw(x-20, y+25, x-20, y-25, color)
        draw_line_raw(x+20, y+25, x+20, y-25, color)


def convert_center(x,y,c):
    global W_Width, W_Height
    center_x,center_y = c[0], c[1]
    x = x + center_x
    y = y + center_y
    return x, y


def draw_points(c):
    glBegin(GL_POINTS)
    for i in (zones):
        x, y = convert_center(i[0], i[1], c)
        glVertex2f(x, y)
    glEnd()


def convertToZones(x,y):
    global zones
    zones.append((x,y))
    zones.append((y,x))
    zones.append((y,-x))
    zones.append((x,-y))
    zones.append((-x,-y))
    zones.append((-y,-x))
    zones.append((-y,x))
    zones.append((-x,y))
    
    
def draw_circle(center_x,center_y,r):
    global zones
    x = 0
    y = r
    zones = []
    convertToZones(x, y)
    d = 1-r
    dE = 2*x + 3
    dSE = 2*x - 2*y + 5
    while x < y:
        dE = 2*x + 3
        dSE = 2*x - 2*y + 5
        if d < 0:
            d += dE
            x += 1
        else:
            d += dSE
            x += 1
            y -= 1
        convertToZones(x, y)
    draw_points((center_x,center_y))
    
    
def keyboardListener(key, x, y):
    global game_play, shooter_pos_x, fire_pos_x, Check_shoot
    if not endgame and game_play:
        if key==b'd':
            if shooter_pos_x + shooter_pos_y != 500:
                shooter_pos_x = shooter_pos_x + 30
        if key==b'a':
            if shooter_pos_x - shooter_pos_y != 0:
                shooter_pos_x = shooter_pos_x - 30
        if key==b' ' and Check_shoot == False:
            fire_pos_x = shooter_pos_x
            Check_shoot = True
    glutPostRedisplay()
    
    
def mouseListener(button, state, x, y):	
    global game_play,  endgame,  score, balls, counter, missed_shots_counter, missed_fire_counter, fire_pos_x, fire_pos_y, shooter_pos_x, shooter_pos_y, Check_shoot, zones
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            x, y = OpenGL_cordinate(x,y)
            if return_pos_x <= x <= return_pos_x+50 and return_pos_y-25 <= y <= return_pos_y+25:
                if endgame:
                    game_play = True
                    endgame = False
                    print("Starting Over!")
                    shooter_pos_x , shooter_pos_y = 250, 20
                    fire_pos_x, fire_pos_y = shooter_pos_x, 2*shooter_pos_y+5
                    zones = []
                    Check_shoot = False
                    balls = []
                    score = 0
                    counter = 0
                    missed_shots_counter = 0
                    missed_fire_counter = 0
                else:
                    game_play = True
                    print("Starting Over!")
                    shooter_pos_x , shooter_pos_y = 250, 20
                    fire_pos_x, fire_pos_y = shooter_pos_x, 2*shooter_pos_y+5
                    zones = []
                    Check_shoot = False
                    balls = []
                    score = 0
                    counter = 0
                    missed_shots_counter = 0
                    missed_fire_counter = 0
            if p_pos_x-25 <= x <= p_pos_x+25 and p_pos_y-25 <= y <= p_pos_y+25:
                if not endgame:
                    if game_play:
                        game_play = False
                    else:
                        game_play = True
            if exit_pos_x <= x <= exit_pos_x+50 and exit_pos_y-50 <= y <= exit_pos_y:
                print("Goodbye! Your Total Score:", score)
                glutLeaveMainLoop()  
    glutPostRedisplay()
    
    
def fallingBalls():
    global balls, counter, missed_shots_counter, endgame, game_play
    speed = 0.5  
    if game_play and not endgame:
        if len(balls) < 5:
            if counter == 0:
                counter += speed
            elif math.floor(counter) == 50:
                x = random.uniform(50, 450)
                y = random.randint(625, 640)
                balls.append([x, y, 650-y])
                for i in range(len(balls)):
                    balls[i][1] = balls[i][1] - speed
                counter = 0
            else:
                for i in range(len(balls)):
                    balls[i][1] = balls[i][1] - speed
                counter += speed
        else:
            for i in range(len(balls)):
                balls[i][1] = balls[i][1] - speed
                if math.floor(balls[i][1]) <= 0:
                    missed_shots_counter += 1
                    balls.pop(i)
                    break
            if missed_shots_counter == 3:
                balls = []
                missed_shots_counter = 0
                game_play = False
                endgame = True
            if endgame:
                print("Game Over!")
                print("Your Total Score:", score)

                
def Check_shootingBalls():
    global game_play, endgame, Check_shoot, fire_pos_x, fire_pos_y, shooter_pos_x, shooter_pos_y, balls, missed_fire_counter, score 
    hit = -1
    if not endgame and game_play and Check_shoot:
        if math.floor(fire_pos_y) < 650:
            fire_pos_y += 1
        else:
            Check_shoot = False
            fire_pos_y = 2*shooter_pos_y+5
            missed_fire_counter += 1
    if not endgame and game_play and Check_shoot:
        for i in range(len(balls)):
            x = (fire_pos_x - balls[i][0])**2
            y = (fire_pos_y - balls[i][1])**2
            r = (balls[i][2]+5)**2
            if (x + y) <= r:
                hit = i
                score += 1
                print("Score:", score)
    if not endgame and game_play:
        for i in range(len(balls)):
            x = (shooter_pos_x - balls[i][0])**2
            y = (shooter_pos_y - balls[i][1])**2
            r = (balls[i][2]+20)**2
            if (x + y) <= r:
                fire_pos_y = 2*shooter_pos_y+5
                balls = []
                game_play = False
                endgame = True
                break
        if endgame:
            print("Game Over!")
            print("Total Score:", score)
    if hit != -1:
        balls.pop(hit)
        Check_shoot = False
        fire_pos_y = 2*shooter_pos_y+5
    if not endgame and missed_fire_counter == 3:
        balls = []
        missed_fire_counter = 0
        game_play = False
        endgame = True
        print("Game Over!")
        print("Total Score:", score)
        
    
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
    global shooter_pos_x, shooter_pos_y, fire_pos_x, fire_pos_y, p_pos_x, p_pos_y, return_pos_x, return_pos_y, exit_pos_x, exit_pos_y, counter,  Check_shoot, balls

    if not endgame and Check_shoot:
        draw_circle(fire_pos_x, fire_pos_y, 5)
    draw_circle(shooter_pos_x, shooter_pos_y, 20)
    
    for i in range(len(balls)):
        draw_circle(balls[i][0], balls[i][1], balls[i][2])
    
    draw_exit_button(exit_pos_x, exit_pos_y, [1, 0, 0])
    draw_return_button(return_pos_x, return_pos_y, [0, 0, 1])
    draw_pause_play_button(p_pos_x, p_pos_y, [1, 0.7, 0.02])
    
    glutSwapBuffers()
    

def animation():
    glutPostRedisplay()
    global game_play, endgame, Check_shoot, fire_pos_x, fire_pos_y, shooter_pos_x, shooter_pos_y, balls
    fallingBalls()
    Check_shootingBalls()


def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,	1,	1,	1000.0)


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) 

wind = glutCreateWindow(b"Ball Shooting Game")
init()

glutDisplayFunc(display)	
glutIdleFunc(animation)	

glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)

glutMainLoop()		
