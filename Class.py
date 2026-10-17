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

class line:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length