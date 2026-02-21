# exctract_data.py
"""Модуль функции извлечения данных"""

import json
import os
from typing import Any

from src.models import Category, Product


def get_info_file_json(file_path: str) -> Any:
    """Считывает данные из JSON файла в data"""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_class_objects(data_categories: list) -> list:
    """Создаем объекты классов из данных в файле"""
    objects_list = []

    for category in data_categories:
        obj_category = Category(category["name"], category["description"], [])

        for product in category["products"]:
            obj_product: Any = Product(product["name"], product["description"], product["price"], product["quantity"])
            obj_category.add_product(obj_product)

        objects_list.append(obj_category)

    return objects_list


if __name__ == "__main__":  # pragma: no cover
    project_root = os.path.dirname(os.path.dirname(__file__))
    path_file_json = os.path.join(project_root, "data", "products.json")

    data_json: list = get_info_file_json(path_file_json)
    objects: list = get_class_objects(data_json)

    print(type(data_json))
    print(data_json)

    print(type(objects))
    print(objects)
