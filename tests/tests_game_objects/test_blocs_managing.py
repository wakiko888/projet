import pytest

from game_objects import BlocksManager, Camera


@pytest.fixture
def create_blocks_manager(create_camera):
    return BlocksManager(create_camera)


@pytest.fixture
def create_camera():
    return Camera(0, 0, 256, 256, 1)


def test_blocks_manager_init(create_blocks_manager, create_camera):
    assert create_blocks_manager.blocks == []
    assert create_blocks_manager.camera is create_camera


def test_set_block(create_blocks_manager):
    create_blocks_manager.set_block(10, 10, 20, 20)
    assert len(create_blocks_manager.blocks) == 1
    new_block = create_blocks_manager.blocks[0]
    assert new_block.x == 10
    assert new_block.y == 10
    assert new_block.width == 20
    assert new_block.height == 20
    assert new_block.camera is create_blocks_manager.camera


def test_draw_all_blocks(create_blocks_manager, monkeypatch):
    calls = []

    def fake_draw(current_block):
        calls.append(current_block)

    monkeypatch.setattr("game_objects.Block.draw", fake_draw)
    create_blocks_manager.set_block(10, 20, 30, 40)
    create_blocks_manager.set_block(50, 60, 70, 80)
    create_blocks_manager.draw_all_blocks()
    assert calls == create_blocks_manager.blocks
