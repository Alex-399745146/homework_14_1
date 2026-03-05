# models.py
"""Модуль содержит описание классов объектов"""

from typing import Any, Iterator

from src.abstract_models import BaseProduct
from src.mixin_models import PrintMixin


# Дочерний класс от BaseProduct
class Product(BaseProduct, PrintMixin):
    """Создание объектов - товаров"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, quantity)
        self.__price = price
        print(repr(self))

        # После инициализации 4х атрибутов проверяем - quantity
        if self.quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __str__(self) -> str:
        """Метод вывода информации определенного формата с содержанием имени товара, цены, единиц на складе"""
        return f"{self.name}, {self.__price:.2f} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Метод подсчёта полной стоймости товара на складе одного типа"""
        if type(self) is type(other):  # Проверяем точное совпадение типов
            result = (self.__price * self.quantity) + (other.__price * other.quantity)
            return result
        raise TypeError(f"Нельзя складывать разные типы товаров {type(self).__name__} и {type(other).__name__}")

    @classmethod
    def new_product(cls, params: dict) -> Any:
        """Метод-класса для создания экземпляра Product"""
        return cls(
            name=params["name"], description=params["description"], price=params["price"], quantity=params["quantity"]
        )

    @property
    def price(self) -> float:
        """Метод getter цены товара"""
        return self.__price

    @price.setter
    def price(self, price: float) -> Any:
        """Метод setter цены товара"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            response = input("Цену товара снизить?(y/n)")
            if response.lower() == "y":
                print("Цена товара снижена!!!")
                self.__price = price
            else:
                print("Изменение цены отменено")
        else:
            self.__price = price  # Устанавливаем новую цену


# Дочерний класс от Product
class Smartphone(Product):
    """Создание объектов товаров подкласса продуктов"""

    # Описание типов данных в классе.
    name: str
    description: str
    price: float
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


# Дочерний класс от Product
class LawnGrass(Product):
    """Создание объектов товаров подкласса продуктов"""

    # Описание типов данных в классе.
    name: str
    description: str
    price: float
    quantity: int
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Создание групп товаров"""

    # Атрибуты класса.
    category_count: int = 0  # количество категорий
    product_count: int = 0  # общее количество единиц товаров в категории

    # Описание типов данных в классе.
    name: str
    description: str
    __products: list  # Приватный атрибут

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        # Увеличиваем счетчики категорий и товаров
        Category.category_count += 1
        Category.product_count = sum(product.quantity for product in self.__products)

    def __str__(self) -> str:
        count_prods = 0
        for product in self.__products:
            count_prods += product.quantity
        return f"{self.name}, количество продуктов: {count_prods} шт."

    def __iter__(self) -> Iterator[Product]:
        return CategoryIterator(self)

    @property
    def products(self) -> list:
        """Метод вывода наименований товаров и их количество с ценами"""
        prod_list = []
        for prod in self.__products:
            prod_list.append(str(prod))
        return prod_list

    @products.setter
    def products(self, products: list[Product]) -> None:
        """Метод сеттер создания атрибута для экземпляров класса"""
        self.__products = []
        for prod in products:
            self.__products.append(prod)

    def add_product(self, product: Any) -> None:
        """Публичный метод для добавления продукта в категорию"""
        if not isinstance(product, (Product, LawnGrass, Smartphone)):
            raise TypeError(
                f"Нельзя добавить в категорию объект типа {type(product).__name__}. "
                "Ожидался экземпляр класса Product или его наследник (LawnGrass, Smartphone)."
            )
        self.__products.append(product)
        Category.product_count += product.quantity


class CategoryIterator:
    """Итератор перебора продуктов в категории продуктов"""

    # Описание типов данных в классе.
    category_obj: Category

    def __init__(self, category_obj: Category) -> None:
        self._category = category_obj
        self._index = 0

    def __iter__(self) -> Iterator[Product]:
        return self

    def __next__(self) -> Product:
        if self._index < len(self._category.products):
            result: Product = self._category.products[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":  # pragma: no cover
    product1 = Product('Philips 55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product2 = Product("Sony", "Мини c матовым покрытие экрана", 15000.0, 10)

    print(product1)
    print(product2, "\n")

    category = Category(
        "Телевизоры",
        """Современный телевизор, который позволяет наслаждаться просмотром,
          станет вашим другом и помощником""",
        [product1],
    )

    print("Группа:", category.name)
    print("В категории:", category.product_count, "\n")

    category.add_product(product2)

    print("Группа:", category.name)
    print("В категории:", category.product_count, "\n")

    iterator = CategoryIterator(category)

    for product in iterator:
        print(product)
