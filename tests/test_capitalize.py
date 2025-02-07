# Нажмите кнопку Run чтобы запустить тесты.

# Файлы с исходным кодом можно посмотреть на вкладке "Files":
# src/capitalize.py        - тестируемая функция
# tests/test_capitalize.py - тесты функции

# Попробуйте изменять код функции/тестов, запуская проверки заново.

from src.capitalize import capitalize

if capitalize('asd') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('Asd') != 'asd':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
