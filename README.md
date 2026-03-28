# Модель задачи: дескрипторы и @property

Реализация модели задачи в рамках платформы обработки задач с корректной инкапсуляцией и валидацией состояния.

## Установка

**1. Клонирование**
```
https://github.com/dobri3/sem2_laba2
```

**2. Запуск**
```
python -m src.main
```

## Использование

python -m src.main

2e1b74aa-2e06-4653-9b55-c289919d8dfd
обработать заказ
True
False
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\bortg\sem2_laba2\src\main.py", line 23, in <module>
    main()
    ~~~~^^
  File "C:\Users\bortg\sem2_laba2\src\main.py", line 19, in main
    task.priority = 30 #упадет
    ^^^^^^^^^^^^^
  File "C:\Users\bortg\sem2_laba2\src\priority_descriptor.py", line 17, in __set__
    raise InvalidPriorityError
src.exceptions.InvalidPriorityError: приоритет может быть только 1, 2 или 3


### Атрибуты Task


 `id`  `str`  Уникальный идентификатор, генерируется автоматически через `uuid4`, только для чтения
 `description`  `str`  Описание задачи, непустая строка
 `priority`  `int`  Приоритет задачи, допустимые значения: 1, 2, 3
 `status` `str` Статус задачи, допустимые значения: `new`, `in_progress`, `done`
 `created_at`  `datetime`  Время создания, устанавливается автоматически, только для чтения
 `is_ready`  `bool`  Вычисляемое свойство, `True` если статус `new` или `in_progress`

### Дескрипторы

`DescriptionDescriptor` — data дескриптор, проверяет что описание является непустой строкой
`PriorityDescriptor` — data дескриптор, проверяет что приоритет входит в допустимые значения
`StatusDescriptor` — data дескриптор, проверяет что статус входит в допустимые значения
`IsReadyDescriptor` — non-data дескриптор, вычисляет готовность задачи к выполнению

### Исключения

`InvalidDescriptionError` — некорректное описание
`InvalidPriorityError` — недопустимый приоритет
`InvalidStatusError` — недопустимый статус

## Тесты

Используется `pytest` и `unittest`. Для запуска тестов:
pytest
