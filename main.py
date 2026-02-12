# main.py
"""Основной исполнительный файл"""

from src.my_homework import Category, Product

if __name__ == "__main__":
    # Создание объектов с вводом данных в атрибуты путем позиционных аргументов.
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    # Вывод в данных через атрибут объекта-поиск данных по принципу MRO.
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
    print("-----------------------------")
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)
    print("-----------------------------")
    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
    print("-----------------------------")
    print(product4.name)
    print(product4.description)
    print(product4.price)
    print(product4.quantity)

    category1 = Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации, но и получения
        "дополнительных функций для удобства жизни""",
        [product1, product2, product3],
    )

    category2 = Category(
        "Телевизоры",
        """Современный телевизор, который позволяет наслаждаться просмотром,
        станет вашим другом и помощником""",
        [product4],
    )

    print("-----------------------------")
    # print(category1.name == "Смартфоны")  немного поправил выданный файл к чему это сравнение
    print(category1.name)
    print(category1.description)
    print("Кол-во изделий:", len(category1.products))
    print("Счётчик категорий:", category1.category_count)
    print("Счётчик изделий:", category1.product_count)
    print("-----------------------------")
    print(category2.name)
    print(category2.description)
    print("Кол-во изделий:", len(category2.products))
    # print(category2.products) немного поправил выданный файл похоже в нем ошибка
    print("Счётчик категорий:", category2.category_count)
    print("Счётчик изделий:", category2.product_count)
    print("-----------------------------")
    print("Всего групп:", Category.category_count)
    print("Всего изделий:", Category.product_count)
