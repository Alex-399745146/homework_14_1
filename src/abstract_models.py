# abstract_models.py
"""Тут описанные абстрактные модели классов"""

from abc import ABC, abstractmethod
from typing import Any


# Создаём базовый абстрактный класс, наследуется от ABC
class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, quantity: int):
        self.name = name
        self.description = description
        # Не инициализируем __price здесь — пусть дочерние классы делают это
        self.quantity = quantity

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> float:
        """Абстрактный метод-класса для создания экземпляра"""
        # Pass т.к. в class Product переопределим этот метод
        pass
