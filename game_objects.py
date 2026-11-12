import pyxel


class Character:
    def __init__(self, x, y, hitbox_width, hitbox_height, camera):
        self.x = x
        self.y = y
        self.hitbox_width = hitbox_width
        self.hitbox_height = hitbox_height
        self.x_speed = 0
        self.y_speed = 0
        self.is_jumping = False
        self.is_colliding = False
        self.is_on_top = False
        self.who_collide = "none"
        self.load_collision_box_width = 45
        self.load_collision_box_height = 60
        self.camera = camera

    def speak(self, text: str, language):
        pixels_per_line = 50
        pixels_on_line = 0
        words = text.split(" ")
        words_on_line = []
        lines = []

        for word in words:
            word_width = len(word) * 4
            if word_width + pixels_on_line <= pixels_per_line:
                words_on_line.append(word)
                pixels_on_line += word_width + 4

            else:
                lines.append(" ".join(words_on_line))
                words_on_line = [word]
                pixels_on_line = word_width + 4

        lines.append(" ".join(words_on_line))

        start_y = self.y - len(lines) * 7

        for i, line_text in enumerate(lines):  # affiche chaque ligne de mots
            pyxel.text(
                self.x * self.camera.zoom,
                (start_y + i * 7) * self.camera.zoom,
                line_text,
                8,
            )


class Block:
    def __init__(self, x, y, width, height, camera):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.camera = camera

    def draw(self):
        pyxel.rect(
            self.x * self.camera.zoom,
            self.y * self.camera.zoom,
            self.width * self.camera.zoom,
            self.height * self.camera.zoom,
            5,
        )


class BlocksManager:
    def __init__(self, camera):
        self.blocks: list[Block] = []
        self.camera = camera

    def set_block(self, x, y, width, height):
        self.blocks.append(Block(x, y, width, height, self.camera))

    def draw_all_blocks(self):
        for block in self.blocks:
            block.draw()


class Collider:
    def is_close_to_collide(
        self,
        object_1_x,
        object_1_y,
        object_1_width,
        object_1_height,
        object_2_x,
        object_2_y,
        object_2_width,
        object_2_height,
    ):
        return (
            abs(
                object_2_x
                + object_2_width / 2
                - (object_1_x + object_1_width / 2)
            )
            < 50
            and abs(
                object_2_y
                + object_2_height / 2
                - (object_1_y + object_1_height / 2)
            )
            < 50
        )

    def rect_to_rect(
        self,
        object_1_x,
        object_1_y,
        object_1_width,
        object_1_height,
        object_2_x,
        object_2_y,
        object_2_width,
        object_2_height,
    ):
        return (
            object_1_x + object_1_width > object_2_x
            and object_1_x < object_2_x + object_2_width
            and object_1_y + object_1_height > object_2_y
            and object_1_y < object_2_y + object_2_height
        )

    def point_to_rect(
        self, point_x, point_y, rect_x, rect_y, rect_width, rect_height
    ):
        return (
            point_x > rect_x
            and point_y > rect_y
            and point_x < rect_x + rect_width
            and point_y < rect_y + rect_height
        )


class World:
    def __init__(self, gravity, ground_friction, air_friction, fall_max_speed):
        self.gravity = gravity
        self.ground_friction = ground_friction
        self.air_friction = air_friction
        self.fall_max_speed = fall_max_speed


class Camera:
    def __init__(self, x=0, y=0, size_x=256, size_y=256, zoom=1):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.zoom = zoom


class Mouse:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.update_x = 0
        self.update_y = 0

    def actual_position(self) -> None:
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y

    def update_position(self) -> None:
        self.update_x = pyxel.mouse_x
        self.update_y = pyxel.mouse_y


class TriggerZone:
    def __init__(self, x, y, width, height, camera, flag):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.camera = camera
        self.flag = flag

    def draw(self):
        pyxel.rectb(
            self.x * self.camera.zoom,
            self.y * self.camera.zoom,
            self.width * self.camera.zoom,
            self.height * self.camera.zoom,
            5,
            )

class TriggerManager:
    def __init__(self, camera):
        self.zones = []
        self.camera = camera
        self.triggers = {
        "Flag1":False,
        "Flag2":False,
        "Flag3":False
        }

    def set_trigger_zones(self, x, y, width, height, flag):
        self.zones.append(TriggerZone(x, y, width, height, self.camera, flag))

    def draw_all_zones(self):
        for zone in self.zones:
            zone.draw()