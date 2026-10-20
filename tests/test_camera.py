import pytest
from Class import camera

@pytest.fixture
def create_camera():
    return camera()

def test_camera_default_value_init(create_camera):
    assert create_camera.x == 0
    assert create_camera.y == 0
    assert create_camera.size_x == 256
    assert create_camera.size_y == 256
    assert create_camera.zoom == 1

def test_camera_non_default_vaue_init():
    create_camera = camera(1, 1, 128, 128, 2)
    assert create_camera.x == 1
    assert create_camera.y == 1
    assert create_camera.size_x == 128
    assert create_camera.size_y == 128
    assert create_camera.zoom == 2