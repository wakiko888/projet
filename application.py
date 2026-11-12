import pyxel

import game_objects
import world_rules


class App:
    def __init__(self):
        #initialisation et creation des instances de classes
        self.screen_x = 256
        self.screen_y = 256

        self.collider = game_objects.Collider()
        self.camera = game_objects.Camera(0, 0, 256, 256, 2)
        self.character = game_objects.Character(60, 60, 7, 12, self.camera)
        self.block_manager = game_objects.BlocksManager(self.camera)
        self.world = game_objects.World(2, 3, 3, 7)
        self.rules = world_rules.Rules()
        self.block_manager.set_block(0, 70, 150, 1)
        self.block_manager.set_block(50, 85, 15, 10)
        self.block_manager.set_block(100, 25, 50, 20)
        self.mouse = game_objects.Mouse()

        pyxel.init(self.screen_x, self.screen_y, title="LF")
        pyxel.load("LF.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self): #fonction update
        #Controle joueur
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            self.character.x_speed = -10
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.character.x_speed = 10
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_Z):
            self.character.y_speed = -15
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            self.character.y_speed = +15

        #controle de camera via la souris
        wheel_delta = pyxel.mouse_wheel
        if wheel_delta:
            old_zoom = self.camera.zoom
            self.camera.zoom = max(
                0.5, min(5, self.camera.zoom * (1.1**wheel_delta))
            )
            zoom_ratio = self.camera.zoom / old_zoom
            self.camera.x = (
                self.camera.x + pyxel.mouse_x
            ) * zoom_ratio - pyxel.mouse_x
            self.camera.y = (
                self.camera.y + pyxel.mouse_y
            ) * zoom_ratio - pyxel.mouse_y

        self.mouse.update_position()
        if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            self.camera.x += self.mouse.x - self.mouse.update_x
            self.camera.y += self.mouse.y - self.mouse.update_y
        self.mouse.actual_position()

        #Aplication de gravité, friction, collision etc
        if self.character.is_on_top:
            friction = self.rules.ground_friction
        else:
            friction = self.rules.air_friction

        if self.character.y_speed < self.rules.fall_max_speed:
            self.character.y_speed += self.rules.gravity

        if self.character.x_speed > friction:
            self.character.x_speed -= friction
        elif self.character.x_speed < -friction:
            self.character.x_speed += friction
        else:
            self.character.x_speed = 0

        self.character.y += self.character.y_speed

        self.character.is_colliding = False
        self.character.who_collide = "none"
        self.character.is_on_top = False

        for block in self.block_manager.blocks:
            if self.collider.is_close_to_collide(
                self.character.x,
                self.character.y,
                self.character.hitbox_width,
                self.character.hitbox_height,
                block.x,
                block.y,
                block.width,
                block.height,
            ):
                if self.collider.rect_to_rect(
                    self.character.x,
                    self.character.y,
                    self.character.hitbox_width,
                    self.character.hitbox_height,
                    block.x,
                    block.y,
                    block.width,
                    block.height,
                ):
                    self.character.is_colliding = True
                    self.character.who_collide = block
                    self.character.is_on_top = self.character.y_speed > 0
                    break

        if self.character.is_colliding and self.character.y_speed > 0:
            self.character.y = (
                self.character.who_collide.y - self.character.hitbox_height
            )
            self.character.y_speed = 0

        if self.character.is_colliding and self.character.y_speed < 0:
            self.character.y = (
                self.character.who_collide.y
                + self.character.who_collide.height
            )
            self.character.y_speed = 0

        self.character.x += self.character.x_speed

        self.character.is_colliding = False
        self.character.who_collide = "none"

        for block in self.block_manager.blocks:
            if self.collider.is_close_to_collide(
                self.character.x,
                self.character.y,
                self.character.hitbox_width,
                self.character.hitbox_height,
                block.x,
                block.y,
                block.width,
                block.height,
            ):
                if self.collider.rect_to_rect(
                    self.character.x,
                    self.character.y,
                    self.character.hitbox_width,
                    self.character.hitbox_height,
                    block.x,
                    block.y,
                    block.width,
                    block.height,
                ):
                    self.character.is_colliding = True
                    self.character.who_collide = block
                    break

        if self.character.is_colliding and self.character.x_speed > 0:
            self.character.x = (
                self.character.who_collide.x - self.character.hitbox_width
            )
            self.character.x_speed = 0

        if self.character.is_colliding and self.character.x_speed < 0:
            self.character.x = (
                self.character.who_collide.x + self.character.who_collide.width
            )
            self.character.x_speed = 0

    def draw(self): #fonction draw
        pyxel.cls(0)
        pyxel.mouse(True)
        pyxel.camera(self.camera.x, self.camera.y)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            self.character.speak(
                "je suis moi et uniquement moi mais appel moi par mon nom",
                "fr",
            )
        pyxel.rectb(
            self.character.x * self.camera.zoom,
            self.character.y * self.camera.zoom,
            self.character.hitbox_width * self.camera.zoom,
            self.character.hitbox_height * self.camera.zoom,
            5,
        )
        self.block_manager.draw_all_blocks()
        pyxel.circb(
            (self.character.x + 3.5) * self.camera.zoom,
            (self.character.y + 6) * self.camera.zoom,
            50 * self.camera.zoom,
            5,
        )


if __name__ == "__main__":
    App()
