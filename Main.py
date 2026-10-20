import pyxel
import World
import Class
screen_x = 256 #defini la taille de l'ecran
screen_y = 256
pyxel.init(screen_x, screen_y, title="LF") #initie la fenetre
pyxel.load("LF.pyxres") #Charge le fichiers avec les sprites et les sons
collider = Class.collider() #cree une instance de la classe collider pour utiliser le collider
Cam = Class.camera(0, 0, 256, 256, 2)
Mc = Class.character(60, 60, 7, 12, 5, Cam) #cree une instance de la classe character (qui sera notre Main character (Mc))
Eh = Class.character(20, 60, 7, 12, 8, Cam)
Liste_Draw_Character = [Mc, Eh] #liste de chaque character qui va etre draw
Mbloc = Class.blocs_managing(Cam) #cree une instance du manager de bloc pour gerer les blocs
World = Class.world(2.0, 3.0, 3, 7.0) #cree une instance du monde pour importer toute les règles et fonctions

Mbloc.set_block(12, 70, 50, 1) #crée en appellant l'instance de manager de bloc un bloc x = 12, y = 70, width = 15, Height = 1 (une ligne de longeur 15)
Mbloc.set_block(50, 85, 15, 10)


def update(): #fonction update
    if pyxel.btn(pyxel.KEY_LEFT): #rajout de vitesse pour chaque flèche
        Mc.x_speed = -10
    if pyxel.btn(pyxel.KEY_RIGHT):
        Mc.x_speed = 10
    if pyxel.btnp(pyxel.KEY_UP):
        Mc.y_speed = -15
    if pyxel.btn(pyxel.KEY_DOWN):
        Mc.y_speed = +15

    if pyxel.btn(pyxel.KEY_Q): #controle de taille et de position de la camera
        Cam.zoom += 0.1
    if pyxel.btn(pyxel.KEY_E):
        Cam.zoom += -0.1
    if pyxel.btn(pyxel.KEY_A):
        Cam.x += -5
    if pyxel.btn(pyxel.KEY_D):
        Cam.x += 5
    if pyxel.btn(pyxel.KEY_W):
        Cam.y += -5
    if pyxel.btn(pyxel.KEY_S):
        Cam.y += 5

    Mc.collide(World, Mbloc.blocs, collider) #fonction pour calculer si il y a des collisions et réagir en conséquence
    Eh.collide(World, Mbloc.blocs, collider)

def draw():
    pyxel.cls(0) #efface l'ecran
    pyxel.camera(Cam.x, Cam.y)

    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT): #fais dire au mc le texte quand on clic gauche
        Mc.speak("je suis moi et uniquement moi mais appel moi par mon nom", "fr")

    for character in Liste_Draw_Character: #boucle qui dessinne chaque character
        pyxel.rectb(character.x * Cam.zoom, character.y * Cam.zoom, character.HitBox_width * Cam.zoom, character.HitBox_height * Cam.zoom, character.color)

    Mbloc.draw_all_blocs() #dessinne tout les blocs dans la liste de blocs (blocs[])

    pyxel.circb((Mc.x + 3.5) * Cam.zoom, (Mc.y + 6) * Cam.zoom, 50 * Cam.zoom, 5) #dessinne le rayon dans lequels les collsions seront chargées

pyxel.run(update, draw) #run les 2 boucles du jeux 30x par seconde