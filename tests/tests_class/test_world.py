import pytest
from Class import world

@pytest.fixture
def create_world():
    return world(2, 3, 3, 7)

def test_world_init(create_world):
    assert create_world.Gravity == 2
    assert create_world.Ground_Friction == 3
    assert create_world.Air_friction == 3
    assert create_world.Fall_MaxSpeed == 7
