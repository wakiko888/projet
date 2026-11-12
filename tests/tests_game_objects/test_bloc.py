import pytest

from game_objects import Block, Camera


@pytest.fixture
def create_block(create_camera):
    return Block(0, 0, 10, 10, create_camera)


@pytest.fixture
def create_camera():
    return Camera(0, 0, 256, 256, 2)


def test_block_init(create_block, create_camera):
    assert create_block.x == 0
    assert create_block.y == 0
    assert create_block.width == 10
    assert create_block.height == 10
    assert create_block.camera is create_camera
    assert create_camera.zoom == 2


def test_block_draw(monkeypatch, create_block, create_camera):
    calls = []
    block_1 = Block(10, 10, 10, 10, create_camera)
    monkeypatch.setattr(
        "game_objects.pyxel.rect",
        lambda x, y, width, height, color: calls.append(
            (x, y, width, height, color)
        ),
    )
    create_block.draw()
    block_1.draw()
    assert calls == [
        (0, 0, 20, 20, 5),
        (20, 20, 20, 20, 5),
    ]
