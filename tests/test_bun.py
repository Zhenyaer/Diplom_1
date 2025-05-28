import pytest
from bun import Bun


class TestBun:

    # Проверка получения названия булочки
    @pytest.mark.parametrize('name, price', [('Г', 100.0), ('Anything english name', 200.0),
                                             ('Длинное предлинное очень длинное название булочки', 300.0)])
    def test_get_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    # Проверка получения цены булочки
    @pytest.mark.parametrize('name, price', [('Флюоресцентная булка', 100.0), ('Флюоресцентная булка', 43.56),
                                             ('Флюоресцентная булка', 1000000000.9)])
    def test_get_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name
