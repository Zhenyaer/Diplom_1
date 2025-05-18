from database import Database


class TestDatabase:

    # Проверка длины списка buns
    def test_available_buns_length(self):
        database = Database()

        assert len(database.available_buns()) == 3

    # Проверка длины списка ingredients
    def test_available_ingredients_length(self):
        database = Database()

        assert len(database.available_ingredients()) == 6
