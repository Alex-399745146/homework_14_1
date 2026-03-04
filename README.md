# Серия: Домашних заданий

*от тема: 14_1 Основы ООП*

---
## Ядро для интернет-магазина.

`В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.`

---

## Структура проекта

`
tree -L 2
`
```
.
|-- README.md
|-- data
|   `-- products.json
|-- htmlcov
|   |-- class_index.html
|   |-- coverage_html_cb_188fc9a4.js
|   |-- favicon_32_cb_c827f16f.png
|   |-- function_index.html
|   |-- index.html
|   |-- keybd_closed_cb_900cfef5.png
|   |-- status.json
|   |-- style_cb_5c747636.css
|   |-- z_145eef247bfb46b6___init___py.html
|   |-- z_145eef247bfb46b6_abstract_models_py.html
|   |-- z_145eef247bfb46b6_exctract_data_py.html
|   |-- z_145eef247bfb46b6_mixin_models_py.html
|   `-- z_145eef247bfb46b6_models_py.html
|-- main.py
|-- poetry.lock
|-- pyproject.toml
|-- src
|   |-- __init__.py
|   |-- __pycache__
|   |-- abstract_models.py
|   |-- exctract_data.py
|   |-- mixin_models.py
|   |-- models.py
|   `-- py.typed
`-- tests
    |-- __init__.py
    |-- __pycache__
    |-- conftest.py
    |-- test_abstract_models.py
    |-- test_exctract_data.py
    |-- test_mixin_models.py
    `-- test_models.py
```
---

### data

В репозитории хранятся файлы отчётности или считывания даных по товаром как шлюз ввода инфы

---

### htmlcov

В папке хранятся данные по покрытию кода тестами, инициализация автоматическая через команду в терминале
`
pytest --cov=src --cov-report=html
`

---

### main.py

Файл основной логики по запуска всех компонентов проекта(модулей).

---
### abstract_models.py

Модуль содержит базовые классы определяющие наличие для подклассов набора необходимых атрибутов и методов

---
### exctract_data.py

Модуль набор методов по выводу и вводу информации в среду проекта

---
### mixin_models.py

Модуль классов расширителей

---
### models.py

Основной модуль используемых классов и разграничений областей их использования

---
### tests

Репозиторий с тестовыми кейсами

---