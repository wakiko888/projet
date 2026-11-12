import pytest

from game_objects import World
from world_rules import Rules


@pytest.fixture
def create_world():
    return World(2, 3, 3, 7)


def test_world_init(create_world):
    assert create_world.gravity == 2
    assert create_world.ground_friction == 3
    assert create_world.air_friction == 3
    assert create_world.fall_max_speed == 7


def test_rules_init():
    rules = Rules()
    assert rules.gravity == 2
    assert rules.ground_friction == 3
    assert rules.air_friction == 3
    assert rules.fall_max_speed == 7
