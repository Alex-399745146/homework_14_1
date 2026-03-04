# test_mixin_models.py
"""Модуль проверки работы миксинов"""

from typing import Any

from src.models import Product


def test_print_mixin(capsys) -> Any:
    """Тест проверяет работу метода print_mixin"""
    Product("Лампа", "Настольная-светодиодная", 100, 1)
    message = capsys.readouterr().out  # Инф.из миксин: Product(Лампа, Настольная-светодиодная, 100, 1)

    assert "Product(Лампа, Настольная-светодиодная, 100, 1)" in message
