from src.ingredient import Ingredient
import re


class TestBurger:

    def test_init(self, burger):
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun.name == bun.name
        assert burger.bun.price == bun.price

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].price == ingredient.price
        assert burger.ingredients[0].name == ingredient.name
        assert burger.ingredients[0].type == ingredient.type

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        ingredient_1 = Ingredient("test1", "test1", 42.0)
        ingredient_2 = Ingredient("test2", "test2", 43.0)
        ingredient_3 = Ingredient("test3", "test3", 44.0)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].type == ingredient_2.type
        assert burger.ingredients[0].name == ingredient_2.name
        assert burger.ingredients[0].price == ingredient_2.price

    def test_get_price(self, burger, bun):
        ingredient_1 = Ingredient("test1", "test1", 42.0)
        ingredient_2 = Ingredient("test2", "test2", 43.0)
        ingredient_3 = Ingredient("test3", "test3", 44.0)
        expected_price = bun.get_price() * 2 + ingredient_1.get_price() + ingredient_2.get_price() + ingredient_3.get_price()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert len(list(re.finditer(bun.get_name(), receipt))) == 2
        assert f"{str(ingredient.get_type()).lower()} {ingredient.get_name()}" in receipt
        assert f'Price: {burger.get_price()}' in receipt
