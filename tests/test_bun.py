from praktikum.bun import Bun
from data import Data


class TestBun:

    def test_get_name(self):
        bun = Bun(Data.BUN_NAME_ONE, Data.BUN_PRICE_ONE)

        assert bun.get_name() == Data.BUN_NAME_ONE

    def test_get_price(self):
        bun = Bun(Data.BUN_NAME_TWO, Data.BUN_PRICE_TWO)

        assert bun.get_price() == Data.BUN_PRICE_TWO
