import pyxel
class character: #classe pour tout les personnages
    def __init__(self, x, y, HitBox_width, HitBox_height): 
        #aplique tout les paramètre a des variables dans la classe et pas dans la fonction
        self.x = x
        self.y = y
        self.HitBox_width = HitBox_width
        self.HitBox_height = HitBox_height
        self.x_speed = 0
        self.y_speed = 0
        self.Is_jumping = False
        self.Is_colliding = False
        self.Is_on_top = False
        self.who_collide = "none"
        self.Load_collision_box_width = 45
        self.Load_collision_box_height = 60

class bloc: #classe pour faire chaque instance de bloc (on crée une instance ca crée un bloc)
    def __init__(self, x, y, width, height):
        #aplique tout les paramètre a des variables dans la classe et pas dans la fonction
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        #dessine l'instance de bloc actuelle
        pyxel.rect(self.x, self.y, self.width, self.height, 5)

class blocs_managing:
    def __init__(self):
        #crée la liste de blocs a dessiner
        self.blocs = []

    def set_block(self, x, y, width, height):
        #crée une instance de bloc (un bloc) et le rajoute a la liste des blocs a dessinner
        nouveau_bloc = bloc(x, y, width, height)
        self.blocs.append(nouveau_bloc)

    def draw_all_blocs(self):
        #boucle qui appelle la fonction "draw" sur chaque instance de bloc dans la liste
        for bloc_actuel in self.blocs:
            bloc_actuel.draw()


class collider:
    def Is_close_to_collide(self, Obj_1_x, Obj_1_y, Obj_1_width, Obj_1_height, Obj_2_x, Obj_2_y, Obj_2_width, Obj_2_height): #Fonction qui determine si 2 objets sont assez proche pour calculer la collision (sert a réduire le cout en performance en ne calculant que les collisions proche)
        if (abs(Obj_2_x + Obj_2_width/2 - (Obj_1_x + Obj_1_width/2)) < 50) and (abs(Obj_2_y + Obj_2_height/2 - (Obj_1_y + Obj_1_height/2)) < 50): # "abs(Obj_2_x - Obj_1_x)" retourne la valeur absolue de la difference de position entre les 2 x des 2 objets, (donc leur distance l'un  a l'autre, et si elle a moins de 50 ca "vaut le cout" de tester une collsion)
            return True
        else:
            return False

    def Rect_up_line(self, Obj_1_x, Obj_1_y, Obj_1_width, Obj_1_height, Obj_2_x, Obj_2_y, Obj_2_length):
        #va verfier si un rectangle (objet 1) est dans ou dessus une ligne horizontal (objet 2) (pas sur que ca va rester longtemps ca)
        if (Obj_1_y + Obj_1_height > Obj_2_y - 16) and ((Obj_1_x > Obj_2_x and Obj_1_x < Obj_2_x + Obj_2_length) or (Obj_1_x + Obj_1_width > Obj_2_x and Obj_1_x + Obj_1_width < Obj_2_x + Obj_2_length)):
            return True
        else:
            return False
    
    def Rect_to_rect(self, Obj_1_x, Obj_1_y, Obj_1_width, Obj_1_height, Obj_2_x, Obj_2_y, Obj_2_width, Obj_2_height):
        #verifie par 4 conditions si 2 rectangle sont superposés
        cond1 = Obj_1_x + Obj_1_width > Obj_2_x
        cond2 = Obj_1_x < Obj_2_x + Obj_2_width
        cond3 = Obj_1_y + Obj_1_height > Obj_2_y
        cond4 = Obj_1_y < Obj_2_y + Obj_2_height
        if (cond1 and cond2 and cond3 and cond4): # si toute les conditions sont vrai return true pour dire que oui il y a collision
            #print(cond1, cond2, cond3, cond4) #print pour voir quand les collisions bug (optionnel)
            return True
        else : # si une des conditions est fausses return false pour dire que non il n'y a pas collision
            #print(cond1, cond2, cond3, cond4) #print pour voir quand les collisions bug (optionnel)
            return False
    
    def Point_to_rect(self, Obj_1_x, Obj_1_y, Obj_2_x, Obj_2_y, Obj_2_width, Obj_2_height):
        #verifie si un point est dans un rectangle par 4 conditions
        cond1 = Obj_1_x > Obj_2_x
        cond2 = Obj_1_y > Obj_2_y
        cond3 = Obj_1_x < Obj_2_x + Obj_2_width
        cond4 = Obj_1_y < Obj_2_y + Obj_2_height
        if (cond1 and cond2 and cond3 and cond4): # si toute les conditions sont vrai return true pour dire que oui il y a collision
            #print(cond1, cond2, cond3, cond4) #print pour voir quand les collisions bug (optionnel)
            return True
        else : # si une des conditions est fausses return false pour dire que non il n'y a pas collision
            #print(cond1, cond2, cond3, cond4) #print pour voir quand les collisions bug (optionnel)
            return False

class world:
    def __init__(self, Gravity, Ground_Friction, Air_friction, Fall_MaxSpeed):
        self.Gravity = Gravity
        self.Ground_Friction = Ground_Friction
        self.Air_friction = Air_friction
        self.Fall_MaxSpeed = Fall_MaxSpeed
    