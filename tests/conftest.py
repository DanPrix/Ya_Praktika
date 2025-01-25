import pytest
from src.burger import Burger
from src.bun import Bun
from src.ingredient import Ingredient
from src.database import Database


@pytest.fixture()
def burger():
    return Burger()


@pytest.fixture()
def bun():
    return Bun("test bun", 42.0)


@pytest.fixture()
def ingredient():
    return Ingredient("test type", "test ingredient", 42.0)


@pytest.fixture()
def database():
    return Database()
