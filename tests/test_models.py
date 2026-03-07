# test_models.py
"""Модуль с кейсами проверок работы классов"""

from src.models import Category, LawnGrass, Product, Smartphone


def test_init_product(fix_diamond_product: Product, fixture_init_prod: dict) -> None:
    """Проверка создания объектов класса Product"""
    assert fix_diamond_product.name == "diamond"
    assert fix_diamond_product.description == "Star of Africa - 621.35 grams"
    assert fix_diamond_product.price == 400000000.0
    assert fix_diamond_product.quantity == 1

    test_obj = Product(**fixture_init_prod)

    assert str(test_obj) == "Toshiba, 1000.00 руб. Остаток: 5 шт."
    assert test_obj + test_obj == 10000.0

    # Проверка типа данных
    assert isinstance(fix_diamond_product.name, str)
    assert isinstance(fix_diamond_product.description, str)
    assert isinstance(fix_diamond_product.price, float)
    assert isinstance(fix_diamond_product.quantity, int)

    test_obj_prod = Product.new_product(fixture_init_prod)

    assert test_obj_prod.name == "Toshiba"
    assert test_obj_prod.description == "Микровалновая печь для дома"
    assert test_obj_prod.price == 1000.0
    assert test_obj_prod.quantity == 5

    try:
        test_obj.price = 0  # Проверка защиты
    except ValueError as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"


def test_init_category(fixture_category: Category, fix_diamond_product: Product) -> None:
    """Проверка создания объектов класса Category"""
    assert fixture_category.name == "Украшения"
    assert fixture_category.description == "Драгоценные камни"
    assert fixture_category.category_count == 1
    assert fixture_category.product_count == 1

    test_obj = Category("Украшения", "Драгоценные камни", [])

    assert test_obj.middle_price() == 0

    test_obj.add_product(fix_diamond_product)

    assert str(test_obj) == "Украшения, количество продуктов: 1 шт."
    assert test_obj.middle_price() == 1

    # Проверка типа данных
    assert isinstance(fixture_category.name, str)
    assert isinstance(fixture_category.description, str)
    assert isinstance(fixture_category.products, list)
    assert isinstance(fixture_category.category_count, int)
    assert isinstance(fixture_category.product_count, int)


def test_init_smartphone(fixture_init_smartphone: dict) -> None:
    """Проверка создания объектов смартфоны"""
    test_obj = Smartphone(**fixture_init_smartphone)

    assert test_obj.name == "Fly"
    assert test_obj.description == "Раскладной телефон"
    assert test_obj.price == 15000.0
    assert test_obj.quantity == 1
    assert test_obj.efficiency == 80.0
    assert test_obj.model == "V5000"
    assert test_obj.memory == 512
    assert test_obj.color == "Чёрный"

    # Проверка типа данных
    assert isinstance(test_obj.name, str)
    assert isinstance(test_obj.description, str)
    assert isinstance(test_obj.price, float)
    assert isinstance(test_obj.quantity, int)
    assert isinstance(test_obj.efficiency, float)
    assert isinstance(test_obj.model, str)
    assert isinstance(test_obj.memory, int)
    assert isinstance(test_obj.color, str)


def test_init_lawngrass(fixture_init_lawngrass: dict) -> None:
    test_obj = LawnGrass(**fixture_init_lawngrass)

    assert test_obj.name == "Клиновидный остролистник"
    assert test_obj.description == "Стойкий пигмент, без выгорания"
    assert test_obj.price == 400.0
    assert test_obj.quantity == 100
    assert test_obj.country == "Голландия"
    assert test_obj.germination_period == "10 дней"
    assert test_obj.color == "Александрит"

    # Проверка типа данных
    assert isinstance(test_obj.name, str)
    assert isinstance(test_obj.description, str)
    assert isinstance(test_obj.price, float)
    assert isinstance(test_obj.quantity, int)
    assert isinstance(test_obj.country, str)
    assert isinstance(test_obj.germination_period, str)
    assert isinstance(test_obj.color, str)
