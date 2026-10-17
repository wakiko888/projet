import pyxel
import World
import Class

pyxel.init(128, 128, title="LF") #initie la fenetre
pyxel.load("LF.pyxres") #Charge le fichiers avec les sprites et les sons
'''
Mc.x = 60
Mc.y = 60
Mc.x_speed = 0
Mc.y_speed = 0
Mc.HitBox_width = 7
Mc.HitBox_height = 12
Ligne1.x = 12
Ligne1.y = 70
Ligne1.length = 15
'''

Mc = Class.character(60, 60, 7, 12)

Ligne1 = Class.line(12, 70, 15)
def update():
    Mc.Is_jumping = False
    Mc.Is_colliding = False
    if pyxel.btn(pyxel.KEY_LEFT):
        Mc.x_speed = -10
    if pyxel.btn(pyxel.KEY_RIGHT):
        Mc.x_speed = 10
    if pyxel.btnp(pyxel.KEY_UP):
        Mc.Is_jumping = True
        Mc.y_speed = -15

    Mc.Is_colliding = (Mc.y + Mc.HitBox_height > Ligne1.y - 16) and ((Mc.x > Ligne1.x and Mc.x < Ligne1.x + Ligne1.length) or (Mc.x + Mc.HitBox_width > Ligne1.x and Mc.x + Mc.HitBox_width < Ligne1.x + Ligne1.length))
    if Mc.Is_colliding == False:
        if Mc.x_speed > 0:
            if Mc.x_speed-World.Air_friction < 0:
                Mc.x_speed = 0
            else:
                Mc.x_speed -= World.Air_friction
        if Mc.x_speed < 0:
            if Mc.x_speed+World.Air_friction > 0:
                Mc.x_speed = 0
            else:
                Mc.x_speed += World.Air_friction

        if Mc.y_speed < World.Fall_MaxSpeed:
            Mc.y_speed += World.Gravity
        else:
            Mc.y_speed = World.Fall_MaxSpeed 

    else:
        if Mc.x_speed > 0:
            if Mc.x_speed-World.Ground_Friction < 0:
                Mc.x_speed = 0
            else:
                Mc.x_speed -= World.Ground_Friction
        if Mc.x_speed < 0:
            if Mc.x_speed+World.Ground_Friction > 0:
                Mc.x_speed = 0
            else:
                Mc.x_speed += World.Ground_Friction

    if Mc.Is_colliding == True:
        Mc.y = Ligne1.y - 16
        if Mc.Is_jumping == False:
            Mc.y_speed = 0
        Mc.Is_colliding = False

    Mc.x += Mc.x_speed        
    if Mc.Is_colliding == False:
        Mc.y += Mc.y_speed
    elif Mc.Is_jumping == True:
        Mc.y += Mc.y_speed

    

def draw():
    pyxel.cls(0)
    pyxel.blt(Mc.x, Mc.y, 0, 0, 0, 16, 16, 0)
    pyxel.blt(Mc.x, Mc.y, 1, 0, 0, 16, 16, 0)
    pyxel.blt(Ligne1.x, Ligne1.y, 1, 16, 7, 15, 1, 0)

pyxel.run(update, draw)
