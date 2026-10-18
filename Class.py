class character:
    def __init__(self, x, y, HitBox_width, HitBox_height):
        self.x = x
        self.y = y
        self.HitBox_width = HitBox_width
        self.HitBox_height = HitBox_height
        self.x_speed = 0
        self.y_speed = 0
        self.Is_jumping = False
        self.Is_colliding = False
        self.Is_on_top = False
        self.Load_collision_box_width = 45
        self.Load_collision_box_height = 60

class bloc:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, 5)

class blocs_managing:
    def __init__(self):
        self.blocs = []

    def set_block(self, x, y, width, height):
        Bloc = bloc(x, y, width, height)
        self.blocs.append(bloc)

    def draw_all_blocs(self):
        for bloc in self.blocs:
            bloc.draw()


class collider:

    def Rect_up_line(self, Obj_1_x, Obj_1_y, Obj_1_width, Obj_1_height, Obj_2_x, Obj_2_y, Obj_2_length):
        #va verfier si un rectangle (objet 1) est dans ou dessus une ligne horizontal (objet 2)
        if (Obj_1_y + Obj_1_height > Obj_2_y - 16) and ((Obj_1_x > Obj_2_x and Obj_1_x < Obj_2_x + Obj_2_length) or (Obj_1_x + Obj_1_width > Obj_2_x and Obj_1_x + Obj_1_width < Obj_2_x + Obj_2_length)):
            return True
        else:
            return False
    
    def Rect_to_rect(self, Obj_1_x, Obj_1_y, Obj_1_width, Obj_1_height, Obj_2_x, Obj_2_y, Obj_2_width, Obj_2_height):
        cond1 = Obj_1_x + Obj_1_width > Obj_2_x
        cond2 = Obj_1_x < Obj_2_x + Obj_2_width
        cond3 = Obj_1_y + Obj_1_height > Obj_2_y
        cond4 = Obj_1_y < Obj_2_y + Obj_2_height
        if (cond1 and cond2 and cond3 and cond4):
            print(
                cond1, cond2, cond3, cond4
            )
            return True
        else :
            print(
                cond1, cond2, cond3, cond4
            )
            return False
    
    def Point_to_rect(self, Obj_1_x, Obj_1_y, Obj_2_x, Obj_2_y, Obj_2_width, Obj_2_height):
        cond1 = Obj_1_x > Obj_2_x
        cond2 = Obj_1_y > Obj_2_y
        cond3 = Obj_1_x < Obj_2_x + Obj_2_width
        cond4 = Obj_1_y < Obj_2_y + Obj_2_height
        if (cond1 and cond2 and cond3 and cond4):
            print(
                cond1, cond2, cond3, cond4
            )
            return True
        else :
            print(
                cond1, cond2, cond3, cond4
            )
            return False
    