import pytest
from Class import blocs_managing, camera

@pytest.fixture
def create_blocs_managing(create_camera):
    return blocs_managing(create_camera)

@pytest.fixture
def create_camera():
    return camera(0, 0, 256, 256, 1)

def test_blocs_managing_init(create_blocs_managing, create_camera):
    assert create_blocs_managing.blocs == []
    assert create_blocs_managing.camera is create_camera

def test_set_block(create_blocs_managing):
    create_blocs_managing.set_block(10, 10, 20, 20)
    assert len(create_blocs_managing.blocs) == 1
    new_bloc = create_blocs_managing.blocs[0]
    assert new_bloc.x == 10
    assert new_bloc.y == 10
    assert new_bloc.width == 20
    assert new_bloc.height == 20
    assert new_bloc.camera is create_blocs_managing.camera

def test_draw_all_blocks(create_blocs_managing, monkeypatch):
    calls = []

    def fake_draw(current_bloc):
        calls.append(current_bloc)

    monkeypatch.setattr("Class.bloc.draw", fake_draw)
    create_blocs_managing.set_block(10, 20, 30, 40)
    create_blocs_managing.set_block(50, 60, 70, 80)
    create_blocs_managing.draw_all_blocs()
    assert calls == create_blocs_managing.blocs