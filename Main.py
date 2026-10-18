import pyxel
import World
import Class
screen_x = 256 #defini la taille de l'ecran
screen_y = 256
pyxel.init(screen_x, screen_y, title="LF") #initie la fenetre
pyxel.load("LF.pyxres") #Charge le fichiers avec les sprites et les sons

Mc = Class.character(60, 60, 7, 12) #cree une instance de la classe character (qui sera notre Main character (Mc))
collider = Class.collider() #cree une instance de la classe collider pour utiliser le collider
Mbloc = Class.blocs_managing() #cree une instance du manager de bloc pour gerer les blocs
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

    if Mc.Is_on_top == True: #si le perso est sur un bloc, mettre la friction a la friction du sol et non de l'air
        friction = World.Ground_Friction
    else:
        friction = World.Air_friction

    if Mc.y_speed < World.Fall_MaxSpeed: #apliquer la gravité que si le personnage ne tombe pas plus vite que la limite max
        Mc.y_speed += World.Gravity

    if Mc.x_speed > friction: #apliquer la friction pour reduire la vitesse horizontale quimporte le sens
        Mc.x_speed -= friction

    elif Mc.x_speed < -friction:
        Mc.x_speed += friction
    
    else: #si la vitesse est entre friction et -friction, elle est "arrondie" a zero
        Mc.x_speed = 0

    Mc.y += Mc.y_speed #aplique les vitesses verticales

    Mc.Is_colliding = False #reinitialisation de toutes les variables de collision
    Mc.who_collide = "none"
    Mc.Is_on_top = False

    for bloc in Mbloc.blocs: #boucle qui verifie chaque bloc si il est a proximité puis si il est en collision avec le personnage
            if collider.Is_close_to_collide(Mc.x, Mc.y, Mc.HitBox_width, Mc.HitBox_height, bloc.x, bloc.y, bloc.width, bloc.height):
                if collider.Rect_to_rect(Mc.x, Mc.y, Mc.HitBox_width, Mc.HitBox_height, bloc.x, bloc.y, bloc.width, bloc.height):
                    #met les variables qui indique que il y a collision et avec qui est la collision
                    Mc.Is_colliding = True
                    Mc.who_collide = bloc
                    Mc.Is_on_top = True
                    break

    if Mc.Is_colliding == True and Mc.y_speed > 0: #si il y a collision et que le perso tombe vers le bas, le replacer sur le bloc et reinitialiser sa vitesse
        Mc.y = Mc.who_collide.y - Mc.HitBox_height
        Mc.y_speed = 0

    if Mc.Is_colliding == True and Mc.y_speed < 0: #si il y a collision et que le perso monte vers le haut, le replacer sous le bloc et reinitialiser sa vitesse
        Mc.y = Mc.who_collide.y + Mc.who_collide.height
        Mc.y_speed = 0

    Mc.x += Mc.x_speed #aplique les vitesses horizontales

    Mc.Is_colliding = False #reinitialisation de toutes les variables de collision
    Mc.who_collide = "none"
    Mc.Is_on_top = False

    for bloc in Mbloc.blocs: #boucle qui verifie chaque bloc si il est a proximité puis si il est en collision avec le personnage
            if collider.Is_close_to_collide(Mc.x, Mc.y, Mc.HitBox_width, Mc.HitBox_height, bloc.x, bloc.y, bloc.width, bloc.height):
                if collider.Rect_to_rect(Mc.x, Mc.y, Mc.HitBox_width, Mc.HitBox_height, bloc.x, bloc.y, bloc.width, bloc.height):
                    #met les variables qui indique que il y a collision et avec qui est la collision
                    Mc.Is_colliding = True
                    Mc.who_collide = bloc
                    Mc.Is_on_top = True
                    break

    if Mc.Is_colliding == True and Mc.x_speed > 0: #si il y a collision et que le perso va vers le coté droit, le replacer sur le coté du bloc et reinitialiser sa vitesse
        Mc.x = Mc.who_collide.x - Mc.HitBox_width
        Mc.x_speed = 0

    if Mc.Is_colliding == True and Mc.x_speed < 0: #si il y a collision et que le perso va vers le coté gauche, le replacer sur le coté du bloc et reinitialiser sa vitesse
        Mc.x = Mc.who_collide.x + Mc.who_collide.width
        Mc.x_speed = 0

def draw():
    pyxel.cls(0) #efface l'ecran
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT): #fais dire au mc le texte quand on clic gauche
        Mc.speak("je suis moi et uniquement moi mais appel moi par mon nom", "fr")
    pyxel.rectb(Mc.x, Mc.y, Mc.HitBox_width, Mc.HitBox_height, 5)#dessinne le personnage
    #pyxel.rectb(Mc.x + 3, Mc.y, Mc.HitBox_width+3, Mc.HitBox_height+4, 8) #hitbox
    Mbloc.draw_all_blocs() #dessinne tout les blocs dans la liste de blocs (blocs[])
    pyxel.circb(Mc.x + 3.5, Mc.y + 6, 50, 5) #dessinne le rayon dans lequels les collsions seront chargées

pyxel.run(update, draw) #run les 2 boucles du jeux 30x par seconde
