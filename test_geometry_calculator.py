import pytest
from geometry_calculator import area_circle, area_rectangle, area_triangle

def test_area_circle():
    assert area_circle(1) == pytest.approx(3.14159, 0.0001)
    assert area_circle(0) == 0
    with pytest.raises(ValueError):
        area_circle(-1)

def test_area_rectangle():
    assert area_rectangle(2, 3) == 6
    assert area_rectangle(0, 5) == 0
    with pytest.raises(ValueError):
        area_rectangle(-2, 3)

def test_area_triangle():
    assert area_triangle(3, 4) == 6
    assert area_triangle(0, 5) == 0
    with pytest.raises(ValueError):
        area_triangle(-3, 4)
