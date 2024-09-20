from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from data import Data
from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, burger, mock_set_buns):
        burger.set_buns(mock_set_buns)

        assert burger.bun == mock_set_buns

    def test_add_ingredient(self, burger, mock_add_ingredient):
        burger.add_ingredient(mock_add_ingredient)

        assert mock_add_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, mock_add_ingredient):
        burger.add_ingredient(mock_add_ingredient)
        burger.remove_ingredient(0)

        assert mock_add_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, mock_add_ingredient):
        burger.add_ingredient(mock_add_ingredient)  # мок из фикстуры
        mock_add_sauce = Mock()
        mock_add_sauce.add_ingredient.return_value = SAUCE, Data.INGREDIENT_NAME_ONE, Data.INGREDIENT_PRICE_ONE
        burger.add_ingredient(mock_add_sauce)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_add_sauce

    def test_get_price(self, burger, mock_set_buns, mock_add_ingredient):
        burger.set_buns(mock_set_buns)
        burger.add_ingredient(mock_add_ingredient)

        bun_price = mock_set_buns.get_price.return_value
        ingredient_price = mock_add_ingredient.get_price.return_value

        assert burger.get_price() == 2 * bun_price + ingredient_price

    def test_get_receipt(self, burger, mock_set_buns, mock_add_ingredient):
        burger.set_buns(mock_set_buns)
        burger.add_ingredient(mock_add_ingredient)
        receipt = burger.get_receipt()
        assert burger.get_receipt() == receipt
