# conftest.py
"""conftest.py для хранения фикстур"""

import os
from pathlib import Path
from typing import Any

import pytest

from src.exctract_data import get_info_file_json
from src.models import Category, Product


@pytest.fixture
def fixture_init_prod() -> dict:
    return {"name": "Toshiba", "description": "Микровалновая печь для дома", "price": 1000, "quantity": 5}


@pytest.fixture(autouse=True)
def reset_category_count() -> None:
    """Сброс счётчика категорий перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def fix_path_file_json() -> Any:
    """Возвращает путь до data и фала в нем"""
    project_root = os.path.dirname(os.path.dirname(__file__))
    path_file_json = os.path.join(project_root, "data", "products.json")
    return path_file_json


@pytest.fixture
def fix_data_json(fix_path_file_json: Path) -> Any:
    data = get_info_file_json(str(fix_path_file_json))
    return data


@pytest.fixture
def fix_diamond_product() -> Product:
    """Возвращает объект класса Product"""
    return Product("diamond", "Star of Africa - 621.35 grams", 400000000.0, 1)


@pytest.fixture
def fixture_category(fix_diamond_product: Product) -> Category:
    """Возвращает объект класса Category"""
    return Category("Украшения", "Драгоценные камни", [fix_diamond_product])


if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(__file__))
    path_file_json = os.path.join(project_root, "data", "products.json")
    print(path_file_json)
