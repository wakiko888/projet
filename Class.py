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
        self.Load_collision_box_width = 45
        self.Load_collision_box_height = 60

class line:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

class collider:

    def Rect_up_line(self, Obj_1_x, Obj_1_y, Obj_1_width, Obj_1_height, Obj_2_x, Obj_2_y, Obj_2_lentgh):
        #va verfier si un rectangle (objet 1) est dans ou dessus une ligne (objet 2)
        if (Obj_1_y + Obj_1_height > Obj_2_y - 16) and ((Obj_1_x > Obj_2_x and Obj_1_x < Obj_2_x + Obj_2_lentgh) or (Obj_1_x + Obj_1_width > Obj_2_x and Obj_1_x + Obj_1_width < Obj_2_x + Obj_2_lentgh)):
            return True
        else:
            return False