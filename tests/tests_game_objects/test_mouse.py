import pytest

from game_objects import Mouse


@pytest.fixture
def create_mouse():
    return Mouse()


def test_mouse_init(create_mouse):
    assert create_mouse.x == 0
    assert create_mouse.y == 0
    assert create_mouse.update_x == 0
    assert create_mouse.update_y == 0


def test_actual_position(monkeypatch, create_mouse):
    monkeypatch.setattr("game_objects.pyxel.mouse_x", 120)
    monkeypatch.setattr("game_objects.pyxel.mouse_y", 80)

    create_mouse.actual_position()
    assert create_mouse.x == 120
    assert create_mouse.y == 80


def test_update_position(monkeypatch, create_mouse):
    monkeypatch.setattr("game_objects.pyxel.mouse_x", 45)
    monkeypatch.setattr("game_objects.pyxel.mouse_y", 65)

    create_mouse.update_position()
    assert create_mouse.update_x == 45
    assert create_mouse.update_y == 65
