import pytest

from game_objects import Camera, Character


@pytest.fixture
def create_character():
    return Character(0, 0, 10, 20, None)


def test_character_init(create_character):
    assert create_character.x == 0
    assert create_character.y == 0
    assert create_character.hitbox_width == 10
    assert create_character.hitbox_height == 20
    assert create_character.x_speed == 0
    assert create_character.y_speed == 0
    assert not create_character.is_jumping
    assert not create_character.is_colliding
    assert not create_character.is_on_top
    assert create_character.who_collide == "none"
    assert create_character.load_collision_box_width == 45
    assert create_character.load_collision_box_height == 60
    assert create_character.camera is None


def test_speak(monkeypatch):
    calls = []
    monkeypatch.setattr(
        "game_objects.pyxel.text",
        lambda x, y, text, color: calls.append((x, y, text, color)),
    )
    perso = Character(10, 100, 10, 20, Camera(zoom=2))
    perso.speak("The test passed", "fr")
    assert calls == [
        (20, 172, "The test", 8),
        (20, 186, "passed", 8),
    ]
