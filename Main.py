import pyxel
import World

pyxel.init(128, 128, title="LF") #initie la fenetre
pyxel.load("LF.pyxres") #Charge le fichiers avec les sprites et les sons

x_MainCharacter = 60
y_MainCharacter = 60
x_speed_MainCharacter = 0
y_speed_MainCharacter = 0
HitBox_MainCharacter_width = 7
HitBox_MainCharacter_height = 12
Ligne_x = 12
Ligne_y = 70
Ligne_length = 15

    
def update():
    global x_MainCharacter, y_MainCharacter, x_speed_MainCharacter, y_speed_MainCharacter

    if pyxel.btn(pyxel.KEY_LEFT):
        x_speed_MainCharacter = -10
    if pyxel.btn(pyxel.KEY_RIGHT):
        x_speed_MainCharacter = 10
    if pyxel.btnp(pyxel.KEY_UP):
        y_speed_MainCharacter = -15

    if x_speed_MainCharacter > 0:
        if x_speed_MainCharacter-World.Air_friction < 0:
            x_speed_MainCharacter = 0
        else:
            x_speed_MainCharacter -= World.Air_friction
    if x_speed_MainCharacter < 0:
        if x_speed_MainCharacter+World.Air_friction > 0:
            x_speed_MainCharacter = 0
        else:
            x_speed_MainCharacter += World.Air_friction

    if y_speed_MainCharacter < World.Fall_MaxSpeed:
        y_speed_MainCharacter += World.Gravity
    else:
        y_speed_MainCharacter = World.Fall_MaxSpeed 
    Is_colliding = (y_MainCharacter + HitBox_MainCharacter_height > Ligne_y) and ((x_MainCharacter > Ligne_x and x_MainCharacter < Ligne_x + Ligne_length) or (x_MainCharacter + HitBox_MainCharacter_width > Ligne_x and x_MainCharacter + HitBox_MainCharacter_width < Ligne_x + Ligne_length))

    if Is_colliding == True:
        y_MainCharacter = Ligne_y
        y_speed_MainCharacter = 0
        Is_colliding = False


    x_MainCharacter += x_speed_MainCharacter        
    if Is_colliding == False:
        y_MainCharacter += y_speed_MainCharacter

    

def draw():
    pyxel.cls(0)
    pyxel.blt(x_MainCharacter, y_MainCharacter, 0, 0, 0, 16, 16, 0)
    pyxel.blt(x_MainCharacter, y_MainCharacter, 1, 0, 0, 16, 16, 0)
    pyxel.blt(Ligne_x, Ligne_y, 1, 16, 7, 15, 1, 0)

pyxel.run(update, draw)
