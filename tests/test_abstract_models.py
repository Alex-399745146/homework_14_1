# test_abstract_models.py
"""Модуль с кейсами проверок базовых абстрактных классов"""

import pytest
from src.abstract_models import BaseProduct


def test_abstract_models() -> None:
    """Проверяем что в абстрактном классе нельзя создавать экземпляры"""
    with pytest.raises(TypeError) as exc_info:
        BaseProduct('Лампа', 'Настольная-светодиодная', 100, 1)

    # Дополнительно проверяем сообщение об ошибке
    assert 'abstract class' in str(exc_info.value)
    assert 'BaseProduct' in str(exc_info.value)
