from unittest.mock import Mock
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    # Проверка получения цены ингридиента
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Сыр', 33.44)
        mock_get_price = Mock(return_value=55.66)
        ingredient.get_price = mock_get_price
        assert ingredient.get_price() == 55.66

    # Проверка получения названия ингридиента
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Кисло-сладкий', 9.23)
        mock_get_name = Mock(return_value='Сырный')
        ingredient.get_name = mock_get_name
        assert ingredient.get_name() == 'Сырный'

    # Проверка типа ингридиента
    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Салат', 15.15)
        mock_get_type = Mock(return_value=INGREDIENT_TYPE_SAUCE)
        ingredient.get_type = mock_get_type
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
