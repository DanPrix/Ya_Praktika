from src.ingredient import Ingredient


class TestIngredient:

    def test_init(self):
        type = "test type"
        name = "test ingredient"
        price = 42.0
        ingredient = Ingredient(type, name, price)
        assert ingredient.type == type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_getters(self):
        type = "test type"
        name = "test ingredient"
        price = 42.0
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
