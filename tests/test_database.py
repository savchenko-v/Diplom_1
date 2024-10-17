import pytest
from data import DbParams


class TestDatabase:

    @pytest.mark.parametrize(DbParams.BUN_PARAM, DbParams.BUN_VALUE)
    def test_available_buns(self, database, index, bun_name, bun_price):
        buns = database.available_buns()

        assert buns[index].get_name() == bun_name and buns[index].get_price() == bun_price

    @pytest.mark.parametrize(DbParams.INGREDIENT_PARAM, DbParams.INGREDIENT_VALUE)
    def test_available_ingredients(self, database, index, ingredient_type, ingredient_name, ingredient_price):
        ingredients = database.available_ingredients()

        assert (ingredients[index].get_type() == ingredient_type and ingredients[index].get_name() == ingredient_name
                and ingredients[index].get_price() == ingredient_price)
