import pyxel
import World
import Class

pyxel.init(128, 128, title="LF") #initie la fenetre
pyxel.load("LF.pyxres") #Charge le fichiers avec les sprites et les sons

Mc = Class.character(60, 60, 7, 12)
collider = Class.collider()
#block1 = Class.block(12, 70, 15, 1)
Mbloc = Class.blocs_managing()

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

    Mbloc.set_block(12, 70, 15, 1)
    Mbloc.set_block(50, 85, 15, 10)

    Mc.x += Mc.x_speed
    Mc.y += Mc.y_speed

    '''
    Mc.Is_colliding = collider.Rect_to_rect(Mc.x, Mc.y, Mc.HitBox_width, Mc.HitBox_height, block1.x, block1.y, block1.width, block1.height)
    Mc.Is_on_top = collider.Rect_to_rect(Mc.x, Mc.y-1, Mc.HitBox_width, Mc.HitBox_height, block1.x, block1.y, block1.width, block1.height)
    print(Mc.Is_on_top)
    if Mc.Is_colliding == False and Mc.Is_on_top == False:
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
        Mc.y = block1.y - 16
        if Mc.Is_jumping == False:
            Mc.y_speed = 0
        Mc.Is_colliding = False

    Mc.x += Mc.x_speed        
    if Mc.Is_colliding == False and Mc.Is_on_top == False:
        Mc.y += Mc.y_speed
    elif Mc.Is_jumping == True:
        Mc.y += Mc.y_speed
    else :
        Mc.y_speed = 0
    '''

    

def draw():
    pyxel.cls(0)
    pyxel.blt(Mc.x, Mc.y, 0, 0, 0, 16, 16, 0)
    pyxel.rectb(Mc.x + 3, Mc.y, Mc.HitBox_width+3, Mc.HitBox_height+4, 8) #hitbox
    pyxel.rectb(Mc.x - 15, Mc.y-15, Mc.Load_collision_box_width, Mc.Load_collision_box_height, 8) #Load_collision_box (sert a load quel collision detecter)
    #pyxel.blt(block1.x, block1.y, 1, 16, 7, block1.width, block1.height, 0)#block
    Mbloc.draw_all_blocs()

pyxel.run(update, draw)
