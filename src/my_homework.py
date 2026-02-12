# my_homework.py
"""Модуль содержит описание двух основных классов"""


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
    category_count: int = 0
    product_count: int = 0

    """ Создание групп товаров """
    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(self.products)
