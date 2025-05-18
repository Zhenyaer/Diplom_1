import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    return Bun('Космобулочка', 45.78)


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, 'халапеньо', 22.33)
