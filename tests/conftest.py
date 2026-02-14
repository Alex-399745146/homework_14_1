# conftest.py
"""conftest.py для хранения фикстур"""

import pytest

from src.models import Category, Product


# Фикстура для класса Product()
@pytest.fixture
def fix_diamond_product() -> Product:
    """Возвращает объект класса Product"""
    return Product("diamond", "Star of Africa - 621.35 grams", 400000000.0, 1)


# Фикстура для класса Category()
@pytest.fixture
def fixture_category(fix_diamond_product: Product) -> Category:
    """Возвращает объект класса Category"""
    return Category("Украшения", "Драгоценные камни", [fix_diamond_product])
