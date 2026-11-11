import pytest

from game_objects import Collider


@pytest.fixture(scope="function")
def create_object():
    objects = {}
    i = 0

    def _create_object(x, y, width=None, height=None):
        nonlocal i
        i += 1

        if width is None and height is None:
            objet = (x, y)
        else:
            objet = (x, y, width, height)
        objects[f"objet{i}"] = objet
        return objects

    return _create_object


@pytest.fixture
def create_collider():
    return Collider()


def test_is_close_to_collide_true(create_object, create_collider):
    objects = create_object(5, 5, 5, 5)
    create_object(15, 15, 5, 5)
    assert create_collider.is_close_to_collide(
        *objects["objet1"], *objects["objet2"]
    )


def test_is_close_to_collide_false(create_object, create_collider):
    objects = create_object(5, 5, 5, 5)
    create_object(100, 10, 5, 5)
    assert not create_collider.is_close_to_collide(
        *objects["objet1"], *objects["objet2"]
    )


def test_is_close_to_collide_false_vertical(create_collider):
    assert not create_collider.is_close_to_collide(0, 0, 5, 5, 0, 100, 5, 5)


def test_rect_to_rect_true_angle(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(10, 10, 5, 6)
    assert not create_collider.rect_to_rect(
        *objects["objet1"], *objects["objet2"]
    )


def test_rect_to_rect_true_border(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(10, 9, 5, 6)
    assert not create_collider.rect_to_rect(
        *objects["objet1"], *objects["objet2"]
    )


def test_rect_to_rect_true_on_top(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(9, 9, 5, 6)
    assert create_collider.rect_to_rect(*objects["objet1"], *objects["objet2"])


def test_rect_to_rect_true_same(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(5, 5, 5, 5)
    assert create_collider.rect_to_rect(*objects["objet1"], *objects["objet2"])


def test_rect_to_rect_false(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(15, 15, 5, 5)
    assert not create_collider.rect_to_rect(
        *objects["objet1"], *objects["objet2"]
    )


def test_rect_to_rect_false_cond2(create_collider):
    assert not create_collider.rect_to_rect(10, 0, 5, 5, 0, 0, 5, 5)


def test_rect_to_rect_false_cond3(create_collider):
    assert not create_collider.rect_to_rect(0, 0, 5, 5, 0, 10, 5, 5)


def test_rect_to_rect_false_cond4(create_collider):
    assert not create_collider.rect_to_rect(0, 10, 5, 5, 0, 0, 5, 5)


def test_point_to_rect_true_angle(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(5, 5)
    assert not create_collider.point_to_rect(
        *objects["objet2"], *objects["objet1"]
    )


def test_point_to_rect_true_border(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(5, 7)
    assert not create_collider.point_to_rect(
        *objects["objet2"], *objects["objet1"]
    )


def test_point_to_rect_true_in(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(8, 7)
    assert create_collider.point_to_rect(
        *objects["objet2"], *objects["objet1"]
    )


def test_point_to_rect_false(create_collider, create_object):
    objects = create_object(5, 5, 5, 5)
    create_object(15, 15)
    assert not create_collider.point_to_rect(
        *objects["objet2"], *objects["objet1"]
    )


def test_point_to_rect_false_cond1(create_collider):
    assert not create_collider.point_to_rect(4, 7, 5, 5, 5, 5)


def test_point_to_rect_false_cond2(create_collider):
    assert not create_collider.point_to_rect(7, 4, 5, 5, 5, 5)


def test_point_to_rect_false_cond4(create_collider):
    assert not create_collider.point_to_rect(7, 11, 5, 5, 5, 5)
