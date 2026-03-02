# mixin_models.py
"""Модуль с дополнительными классами миксин, расширяющие возможности классов"""

class PrintMixin:
    """Главное чтоб в классах куда подселим этот миксин, были атрибуты name_description_price_quantity"""

    def __init__(self):
        """Вызовется метод __repr__ при инициализации"""
        print(repr(self))  # Переопределение функции print

    def __repr__(self) -> str:
        """Волшебный метод вывода форматированной информации"""
        # !!! Динамичное обращение к классу self.__class__.__name__
        return f"Инф.из миксин: {self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
