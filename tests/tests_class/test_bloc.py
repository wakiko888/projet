import pytest
from Class import bloc, camera

@pytest.fixture
def create_bloc(create_camera):
    return bloc(0, 0, 10, 10, create_camera )

@pytest.fixture
def create_camera():
    return camera(0, 0, 256, 256, 2)

def test_bloc_init(create_bloc, create_camera):
    assert create_bloc.x == 0
    assert create_bloc.y == 0
    assert create_bloc.width == 10
    assert create_bloc.height == 10
    assert create_bloc.camera is create_camera
    assert create_camera.zoom == 2

def test_bloc_draw(monkeypatch, create_bloc, create_camera):
    calls = []
    bloc_1 = bloc(10, 10, 10, 10, create_camera)
    monkeypatch.setattr("Class.pyxel.rect", lambda x, y, width, height, color : 
                        calls.append((x, y, width, height, color)))
    create_bloc.draw()
    bloc_1.draw()
    assert calls == [
        (0, 0, 20, 20, 5),
        (20, 20, 20, 20, 5)
    ]
