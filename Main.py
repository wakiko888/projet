import pyxel
import World
import Class

class App:
    def __init__(self):
        self.screen_x = 256 #defini la taille de l'ecran
        self.screen_y = 256
        
        self.collider = Class.collider() #cree une instance de la classe collider pour utiliser le collider
        self.Cam = Class.camera(0, 0, 256, 256, 2)
        self.Mc = Class.character(60, 60, 7, 12, self.Cam) #cree une instance de la classe character (qui sera notre Main character (Mc))
        self.Mbloc = Class.blocs_managing(self.Cam) #cree une instance du manager de bloc pour gerer les blocs
        self.world = Class.world(2, 3, 3, 7) #cree une instance du monde pour importer toute les règles et fonctions
        self.rule = World.rules()
        self.Mbloc.set_block(12, 70, 50, 1) #crée en appellant l'instance de manager de bloc un bloc x = 12, y = 70, width = 15, Height = 1 (une ligne de longeur 15)
        self.Mbloc.set_block(50, 85, 15, 10)

        pyxel.init(self.screen_x, self.screen_y, title="LF") #initie la fenetre
        pyxel.load("LF.pyxres") #Charge le fichiers avec les sprites et les sons
        pyxel.run(self.update, self.draw)


    def update(self): #fonction update
        if pyxel.btn(pyxel.KEY_LEFT): #rajout de vitesse pour chaque flèche
            self.Mc.x_speed = -10
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.Mc.x_speed = 10
        if pyxel.btnp(pyxel.KEY_UP):
            self.Mc.y_speed = -15
        if pyxel.btn(pyxel.KEY_DOWN):
            self.Mc.y_speed = +15

        if pyxel.btn(pyxel.KEY_Q): #controle de taille et de position de la camera
            self.Cam.zoom += 0.1
        if pyxel.btn(pyxel.KEY_E):
            self.Cam.zoom += -0.1
        if pyxel.btn(pyxel.KEY_A):
            self.Cam.x += -5
        if pyxel.btn(pyxel.KEY_D):
            self.Cam.x += 5
        if pyxel.btn(pyxel.KEY_W):
            self.Cam.y += -5
        if pyxel.btn(pyxel.KEY_S):
            self.Cam.y += 5

        if self.Mc.Is_on_top == True: #si le perso est sur un bloc, mettre la friction a la friction du sol et non de l'air
            friction = self.rule.Ground_Friction
        else:
            friction = self.rule.Air_friction

        if self.Mc.y_speed < self.rule.Fall_MaxSpeed: #apliquer la gravité que si le personnage ne tombe pas plus vite que la limite max
            self.Mc.y_speed += self.rule.Gravity

        if self.Mc.x_speed > friction: #apliquer la friction pour reduire la vitesse horizontale quimporte le sens
            self.Mc.x_speed -= friction

        elif self.Mc.x_speed < -friction:
            self.Mc.x_speed += friction
        
        else: #si la vitesse est entre friction et -friction, elle est "arrondie" a zero
            self.Mc.x_speed = 0

        self.Mc.y += self.Mc.y_speed #aplique les vitesses verticales

        self.Mc.Is_colliding = False #reinitialisation de toutes les variables de collision
        self.Mc.who_collide = "none"
        self.Mc.Is_on_top = False

        for bloc in self.Mbloc.blocs: #boucle qui verifie chaque bloc si il est a proximité puis si il est en collision avec le personnage
                if self.collider.Is_close_to_collide(self.Mc.x, self.Mc.y, self.Mc.HitBox_width, self.Mc.HitBox_height, bloc.x, bloc.y, bloc.width, bloc.height):
                    if self.collider.Rect_to_rect(self.Mc.x, self.Mc.y, self.Mc.HitBox_width, self.Mc.HitBox_height, bloc.x, bloc.y, bloc.width, bloc.height):
                        #met les variables qui indique que il y a collision et avec qui est la collision
                        self.Mc.Is_colliding = True
                        self.Mc.who_collide = bloc
                        self.Mc.Is_on_top = self.Mc.y_speed > 0
                        break

        if self.Mc.Is_colliding == True and self.Mc.y_speed > 0: #si il y a collision et que le perso tombe vers le bas, le replacer sur le bloc et reinitialiser sa vitesse
            self.Mc.y = self.Mc.who_collide.y - self.Mc.HitBox_height
            self.Mc.y_speed = 0

        if self.Mc.Is_colliding == True and self.Mc.y_speed < 0: #si il y a collision et que le perso monte vers le haut, le replacer sous le bloc et reinitialiser sa vitesse
            self.Mc.y = self.Mc.who_collide.y + self.Mc.who_collide.height
            self.Mc.y_speed = 0

        self.Mc.x += self.Mc.x_speed #aplique les vitesses horizontales

        self.Mc.Is_colliding = False #reinitialisation de toutes les variables de collision
        self.Mc.who_collide = "none"

        for bloc in self.Mbloc.blocs: #boucle qui verifie chaque bloc si il est a proximité puis si il est en collision avec le personnage
                if self.collider.Is_close_to_collide(self.Mc.x, self.Mc.y, self.Mc.HitBox_width, self.Mc.HitBox_height, bloc.x, bloc.y, bloc.width, bloc.height):
                    if self.collider.Rect_to_rect(self.Mc.x, self.Mc.y, self.Mc.HitBox_width, self.Mc.HitBox_height, bloc.x, bloc.y, bloc.width, bloc.height):
                        #met les variables qui indique que il y a collision et avec qui est la collision
                        self.Mc.Is_colliding = True
                        self.Mc.who_collide = bloc
                        break

        if self.Mc.Is_colliding == True and self.Mc.x_speed > 0: #si il y a collision et que le perso va vers le coté droit, le replacer sur le coté du bloc et reinitialiser sa vitesse
            self.Mc.x = self.Mc.who_collide.x - self.Mc.HitBox_width
            self.Mc.x_speed = 0

        if self.Mc.Is_colliding == True and self.Mc.x_speed < 0: #si il y a collision et que le perso va vers le coté gauche, le replacer sur le coté du bloc et reinitialiser sa vitesse
            self.Mc.x = self.Mc.who_collide.x + self.Mc.who_collide.width
            self.Mc.x_speed = 0

    def draw(self):
        pyxel.cls(0) #efface l'ecran
        pyxel.camera(self.Cam.x, self.Cam.y)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT): #fais dire au mc le texte quand on clic gauche
            self.Mc.speak("je suis moi et uniquement moi mais appel moi par mon nom", "fr")
        pyxel.rectb(self.Mc.x * self.Cam.zoom, self.Mc.y * self.Cam.zoom, self.Mc.HitBox_width * self.Cam.zoom, self.Mc.HitBox_height * self.Cam.zoom, 5)#dessinne le personnage
        #pyxel.rectb(Mc.x + 3, Mc.y, Mc.HitBox_width+3, Mc.HitBox_height+4, 8) #hitbox
        self.Mbloc.draw_all_blocs() #dessinne tout les blocs dans la liste de blocs (blocs[])
        pyxel.circb((self.Mc.x + 3.5) * self.Cam.zoom, (self.Mc.y + 6) * self.Cam.zoom, 50 * self.Cam.zoom, 5) #dessinne le rayon dans lequels les collsions seront chargées

App()
