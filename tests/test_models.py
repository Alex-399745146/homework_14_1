# test_models.py
"""Модуль с кейсами проверок работы классов"""

from src.models import Category, Product


def test_init_product(fix_diamond_product: Product) -> None:
    """Проверка создания объектов класса Product"""
    assert fix_diamond_product.name == "diamond"
    assert fix_diamond_product.description == "Star of Africa - 621.35 grams"
    assert fix_diamond_product.price == 400000000.0
    assert fix_diamond_product.quantity == 1
    # Проверка типа данных
    assert isinstance(fix_diamond_product.name, str)
    assert isinstance(fix_diamond_product.description, str)
    assert isinstance(fix_diamond_product.price, float)
    assert isinstance(fix_diamond_product.quantity, int)


def test_init_category(fixture_category: Category, fix_diamond_product: Product) -> None:
    """Проверка создания объектов класса Category"""
    assert fixture_category.name == "Украшения"
    assert fixture_category.description == "Драгоценные камни"
    assert fixture_category.category_count == 1
    assert fixture_category.product_count == 1
    # Проверка типа данных
    assert isinstance(fixture_category.name, str)
    assert isinstance(fixture_category.description, str)
    assert isinstance(fixture_category.products, str)
    assert isinstance(fixture_category.category_count, int)
    assert isinstance(fixture_category.product_count, int)
