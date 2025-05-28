from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING


class TestForBurger:

    # Проверка выбора булочки
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun == bun

    # Проверка добавление ингридиента
    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient
        assert len(burger.ingredients) == 1

    # Проверка удаления ингридиента
    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    # Проверка перемещения ингридиента
    def test_move_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        ingredient_another = Ingredient(INGREDIENT_TYPE_FILLING, 'сыр', 19.99)
        burger.add_ingredient(ingredient_another)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == ingredient_another
        assert burger.ingredients[1] == ingredient

    # Проверка расчета стоимости бургера
    def test_get_price(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_price = bun.get_price() * 2 + ingredient.get_price()

        assert burger.get_price() == expected_price

    # Проверка формирования чека
    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'(==== {bun.get_name()} ====)\n'\
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'\
                           f'(==== {bun.get_name()} ====)\n'\
                           '\n'\
                           f'Price: {burger.get_price()}'

        assert burger.get_receipt() == expected_receipt
