from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE, INGREDIENT_TYPE_FILLING as FILLING
from data import Data
import pytest


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type', [SAUCE, FILLING])
    def test_get_price(self, ingredient_type):
        ingredient = Ingredient(SAUCE, Data.INGREDIENT_NAME_ONE, Data.INGREDIENT_PRICE_ONE)

        assert ingredient.get_price() == Data.INGREDIENT_PRICE_ONE

    @pytest.mark.parametrize('ingredient_type', [SAUCE, FILLING])
    def test_get_name(self, ingredient_type):
        ingredient = Ingredient(FILLING, Data.INGREDIENT_NAME_TWO, Data.INGREDIENT_PRICE_TWO)

        assert ingredient.get_name() == Data.INGREDIENT_NAME_TWO

    @pytest.mark.parametrize('ingredient_type', [SAUCE, FILLING])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(FILLING, Data.INGREDIENT_NAME_THREE, Data.INGREDIENT_PRICE_THREE)

        assert ingredient.get_type() == FILLING
