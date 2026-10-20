import pytest
from Class import character, camera

@pytest.fixture
def create_character():
    return character(0, 0, 10, 20, None)

def test_character_init(create_character):
    assert create_character.x == 0
    assert create_character.y == 0
    assert create_character.HitBox_width == 10
    assert create_character.HitBox_height == 20
    assert create_character.x_speed == 0
    assert create_character.y_speed == 0
    assert not create_character.Is_jumping 
    assert not create_character.Is_colliding
    assert not create_character.Is_on_top
    assert create_character.who_collide == 'none'
    assert create_character.Load_collision_box_width == 45
    assert create_character.Load_collision_box_height == 60
    assert create_character.camera == None

def test_speak(monkeypatch):
    calls = []
    monkeypatch.setattr("Class.pyxel.text", lambda x, y, text, color: calls.append((x, y, text, color)),)
    perso = character(10, 100, 10, 20, camera(zoom = 2))
    perso.speak("The test passed", "fr")
    assert calls == [
        (20, 172, "The test",8),
        (20, 186, "passed", 8)
    ]



