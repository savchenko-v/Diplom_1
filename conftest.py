import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as FILLING


@pytest.fixture()
def burger():  # создание бургера
    burger = Burger()

    return burger


@pytest.fixture()
def mock_set_buns():  # мок для булки
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Мокированная космическая булка'
    mock_bun.get_price.return_value = 500

    return mock_bun


@pytest.fixture()
def mock_add_ingredient():  # мок для ингредиента (начинки)
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = Data.INGREDIENT_NAME_THREE
    mock_ingredient.get_type.return_value = FILLING
    mock_ingredient.get_price.return_value = Data.INGREDIENT_PRICE_THREE

    return mock_ingredient


@pytest.fixture()
def database():
    database = Database()

    return database
