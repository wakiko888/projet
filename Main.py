import pyxel
import World

pyxel.init(128, 128, title="LF") #initie la fenetre
pyxel.load("LF.pyxres") #Charge le fichiers avec les sprites et les sons

x_MainCharacter = 60
y_MainCharacter = 60
x_speed_MainCharacter = 0
y_speed_MainCharacter = 0

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""
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
    

    x_MainCharacter += x_speed_MainCharacter
    y_MainCharacter += y_speed_MainCharacter

    



# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    # vide la fenetre
    pyxel.cls(0)
    pyxel.blt(x_MainCharacter, y_MainCharacter, 0, 0, 0, 16, 16, 0)
pyxel.run(update, draw)