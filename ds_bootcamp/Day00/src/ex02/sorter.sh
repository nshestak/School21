#!/bin/sh

# Извлекаем заголовок из файла hh.csv и записываем его в новый файл hh_sorted.csv
cat ../ex01/hh.csv | head -n 1 > hh_sorted.csv

# Извлекаем последние 20 строк из файла hh.csv, сортируем их по второму столбцу, а затем по первому
# Результат добавляется в файл hh_sorted.csv
cat ../ex01/hh.csv | tail -n 20 | sort -t, -k2 -k1 >> hh_sorted.csv