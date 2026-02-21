# models.py
"""Модуль содержит описание классов объектов"""


class Product:
    """Создание объектов - товаров"""

    # Описание типов данных в классе.
    name: str
    description: str
    __price: float  # Приватный атрибут
    quantity: int

    # Конструктор класса с атрибутами объектов.
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params: dict) -> "Product":
        """Метод-класса для создания экземпляра Product"""
        return cls(
            name=params["name"], description=params["description"], price=params["price"], quantity=params["quantity"]
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
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

    @property
    def products(self) -> str:
        """Метод вывода наименований товаров и их количество с ценами"""
        name_prod = ""
        for prod in self.__products:
            name_prod += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return name_prod

    @products.setter
    def products(self, products: list[Product]) -> None:
        """Метод создания атрибута для экземпляров класса"""
        self.__products = []
        for prod in products:
            self.__products.append(prod)

    def add_product(self, product: Product) -> None:
        """Публичный метод для добавления продукта в категорию"""
        self.__products.append(product)
        Category.product_count += product.quantity


if __name__ == "__main__":
    product1 = Product('Philips 55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category = Category(
        "Телевизоры",
        """Современный телевизор, который позволяет наслаждаться просмотром,
          станет вашим другом и помощником""",
        [product1],
    )

    print("Группа:", category.name)
    print("В категории:", category.product_count)

    product2 = Product("Sony", "Мини c матовым покрытие экрана", 15000.0, 10)
    category.add_product(product2)

    print("Группа:", category.name)
    print("В категории:", category.product_count)
