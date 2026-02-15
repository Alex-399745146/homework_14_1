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


def get_class_objects(data: Any) -> Any:
    """Создаем объекты классов из данных файла"""
    objects_list = []

    for item in data:
        # Создаём объект Category
        obj_category = Category(item["name"], item["description"], item["products"])
        objects_list.append(obj_category)

        # Для каждого продукта в категории создаём объект Product
        for product in item["products"]:
            obj_product: Any = Product(product["name"], product["description"], product["price"], product["quantity"])
            objects_list.append(obj_product)

    return objects_list


if __name__ == "__main__":  # pragma: no cover
    project_root = os.path.dirname(os.path.dirname(__file__))
    path_file_json = os.path.join(project_root, "data", "products.json")

    data_json = get_info_file_json(path_file_json)
    objects = get_class_objects(data_json)

    # print(type(data_json))
    print(data_json)
    # for obj in objects:
    #     if isinstance(obj, Product):
    #         print("\nТовар:")
    #         print(f"Название: {obj.name}")
    #         print(f"Описание: {obj.description}")
    #         print(f"Цена: {obj.price}")
    #         print(f"Количество: {obj.quantity}")
    #     elif isinstance(obj, Category):
    #         print("\nКатегория:")
    #         print(f"Название: {obj.name}")
    #         print(f"Описание: {obj.description}")
    #         # products есть у Category (список продуктов)
    #         print(f"Товары в категории: {len(obj.products)} шт.")
    #         # Можно вывести названия продуктов:
    #         for product in obj.products:
    #             print(f"  - {product['name']}")
