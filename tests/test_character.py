import pytest
from Class import character

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

def test_speak(create_character):
    create_character.speak("The test passed", "fr")
    # Non fini



