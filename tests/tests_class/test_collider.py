import pytest
from Class import collider

@pytest.fixture(scope = "function")
def create_object():
    objects = {}
    i=0

    def _create_object(x, y, width = None, height = None):
        nonlocal i
        i += 1

        if width is None and height is None :
            objet = (x,y)
        else :
            objet = (x, y, width, height)  
        objects[f"objet{i}"] = objet
        return objects

    return _create_object

@pytest.fixture
def create_collider():
    return collider()

def test_Is_close_to_collide_True(create_object, create_collider):
    objects = create_object(5,5,5,5)
    create_object(15,15,5,5)
    assert create_collider.Is_close_to_collide(*objects["objet1"],*objects["objet2"])

def test_Is_close_to_collide_False(create_object,create_collider):
    objects = create_object(5,5,5,5)
    create_object(100,10,5,5)
    assert not create_collider.Is_close_to_collide(*objects["objet1"],*objects["objet2"])

def test_Is_close_to_collide_False_vertical(create_collider):
    assert not create_collider.Is_close_to_collide(0, 0, 5, 5, 0, 100, 5, 5)

def test_Rect_to_rect_True_angle(create_collider, create_object):
    objects = create_object(5,5,5,5)
    create_object(10,10,5,6)
    assert create_collider.Rect_to_rect(*objects["objet1"],*objects["objet2"])

def test_Rect_to_rect_True_border(create_collider, create_object):
    objects = create_object(5,5,5,5)
    create_object(10,9,5,6)
    assert create_collider.Rect_to_rect(*objects["objet1"],*objects["objet2"])

def test_Rect_to_rect_True_on_top(create_collider, create_object):
    objects = create_object(5,5,5,5)
    create_object(9,9,5,6)
    assert create_collider.Rect_to_rect(*objects["objet1"],*objects["objet2"])

def test_Rect_to_rect_True_same(create_collider, create_object):
    objects = create_object(5,5,5,5)
    create_object(5,5,5,5)
    assert create_collider.Rect_to_rect(*objects["objet1"],*objects["objet2"])

def test_Rect_to_rect_False(create_collider, create_object):
    objects = create_object(5,5,5,5)
    create_object(15,15,5,5)
    assert not create_collider.Rect_to_rect(*objects["objet1"],*objects["objet2"])

def test_Rect_to_rect_False_cond2(create_collider):
    assert not create_collider.Rect_to_rect(10, 0, 5, 5, 0, 0, 5, 5)

def test_Rect_to_rect_False_cond3(create_collider):
    assert not create_collider.Rect_to_rect(0, 0, 5, 5, 0, 10, 5, 5)

def test_Rect_to_rect_False_cond4(create_collider):
    assert not create_collider.Rect_to_rect(0, 10, 5, 5, 0, 0, 5, 5)

def test_Point_to_rect_True_angle(create_collider,create_object):
    objects = create_object(5,5,5,5)
    create_object(5,5)
    assert create_collider.Point_to_rect(*objects["objet2"], *objects["objet1"])

def test_Point_to_rect_True_border(create_collider,create_object):
    objects = create_object(5,5,5,5)
    create_object(5,7)
    assert create_collider.Point_to_rect(*objects["objet2"], *objects["objet1"])

def test_Point_to_rect_True_in(create_collider,create_object):
    objects = create_object(5,5,5,5)
    create_object(8,7)
    assert create_collider.Point_to_rect(*objects["objet2"], *objects["objet1"])

def test_Point_to_rect_False(create_collider,create_object):
    objects = create_object(5,5,5,5)
    create_object(15,15)
    assert not create_collider.Point_to_rect(*objects["objet2"], *objects["objet1"])

def test_Point_to_rect_False_cond1(create_collider):
    assert not create_collider.Point_to_rect(4, 7, 5, 5, 5, 5)

def test_Point_to_rect_False_cond2(create_collider):
    assert not create_collider.Point_to_rect(7, 4, 5, 5, 5, 5)

def test_Point_to_rect_False_cond4(create_collider):
    assert not create_collider.Point_to_rect(7, 11, 5, 5, 5, 5)