"""
    Получение (упрощенное) директории со скриптом, а также рабочей директории
"""
import os

curdir = os.path.abspath(os.path.dirname(__file__))
print('Папка со скриптом:', curdir)
print('Рабочая папка:', os.getcwd())