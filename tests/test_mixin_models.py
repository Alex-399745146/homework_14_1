# test_mixin_models.py
"""Модуль проверки работы миксинов"""

from src.mixin_models import PrintMixin
from src.models import Product


def test_print_mixin(capsys) -> None:
    Product('Лампа', 'Настольная-светодиодная', 100, 1)
    message = capsys.readouterr().out  # Инф.из миксин: Product(Лампа, Настольная-светодиодная, 100, 1)

    assert "Product(Лампа, Настольная-светодиодная, 100, 1)" in message
