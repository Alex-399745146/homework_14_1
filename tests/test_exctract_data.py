# test_exctract.py
"""Модуль с кейсами проверок работы функций"""

import os
from pathlib import Path
from typing import Any

from src.exctract_data import get_class_objects, get_info_file_json
from src.models import Category


def test_get_info_file_json(fix_path_file_json: Path) -> None:
    """Тест кейсы функции get_info_file_json"""
    assert os.path.exists(fix_path_file_json), "Файла по такому пути нет"

    data: Any = get_info_file_json(str(fix_path_file_json))
    first_item = data[0]

    assert len(data) > 0, "Список пуст"
    assert "name" in first_item, 'Нет поля "name" в данных'
    assert "products" in first_item, 'Нет поля "products" в данных'
    assert isinstance(first_item["products"], list), '"products" должен быть списком'


def test_get_class_objects(fix_data_json: Any) -> None:
    """Тест кейсы функции get_class_objects"""
    objects_list = get_class_objects(fix_data_json)

    assert isinstance(objects_list, list), "Результат должен быть списком"
    assert len(objects_list) > 0, "Список объектов пуст"

    category_tv = None
    for obj in objects_list:
        if isinstance(obj, Category) and obj.name == "Телевизоры":
            category_tv = obj
            break

    assert category_tv is not None, 'Категория "Телевизоры" не найдена в списке'
    assert category_tv.name == "Телевизоры"
    assert "телевизор" in category_tv.description.lower()
    assert isinstance(category_tv.products, list)
    assert len(category_tv.products) > 0
