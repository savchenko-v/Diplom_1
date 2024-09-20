from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE, INGREDIENT_TYPE_FILLING as FILLING


class Data:
    BUN_NAME_ONE = 'Некраторная булка'
    BUN_NAME_TWO = 'Краторная булка'
    BUN_PRICE_ONE = 1150
    BUN_PRICE_TWO = 1255.5

    INGREDIENT_NAME_ONE = 'Соус галактический'
    INGREDIENT_NAME_TWO = 'Сырный марсианский огурец'
    INGREDIENT_NAME_THREE = 'Биокотлета из космической пыли'
    INGREDIENT_PRICE_ONE = 21.3
    INGREDIENT_PRICE_TWO = 121.1
    INGREDIENT_PRICE_THREE = 424


class DbParams:
    BUN_PARAM = 'index, bun_name, bun_price'
    BUN_VALUE = [
        [0, "black bun", 100],
        [1, "white bun", 200],
        [2, "red bun", 300]
    ]

    INGREDIENT_PARAM = 'index, ingredient_type, ingredient_name, ingredient_price'
    INGREDIENT_VALUE = [
        [0, SAUCE, "hot sauce", 100],
        [1, SAUCE, "sour cream", 200],
        [2, SAUCE, "chili sauce", 300],
        [3, FILLING, "cutlet", 100],
        [4, FILLING, "dinosaur", 200],
        [5, FILLING, "sausage", 300]
    ]
