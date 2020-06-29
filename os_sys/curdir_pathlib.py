""" Получение текущей директории для Python 3.4+ """
from inspect import currentframe, getframeinfo
from pathlib import Path

filename = getframeinfo(currentframe()).filename
parent = Path(filename).resolve().parent

print('Файл скрипта:', filename)
print('Директория скрипта', parent)