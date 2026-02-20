# models.py
"""Модуль содержит описание классов объектов"""


# Task_1
class Product:
    """Создание объектов - товаров"""

    # Описание типов данных в классе.
    name: str
    description: str
    price: float
    quantity: int

    # Конструктор класса с атрибутами объектов.
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Создание групп товаров"""

    # Атрибуты класса.
    category_count: int = 0
    product_count: int = 0
    # Описание типов данных в классе.
    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products

        # Task_2
        Category.category_count += 1
        Category.product_count += len(self.products)
