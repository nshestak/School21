#!/bin/sh

# Создаем файл hh_uniq_positions.csv и записываем в него заголовок
echo '"name","count"' > hh_uniq_positions.csv

# Указываем путь к входному файлу, который будет обрабатываться
input_file="../ex03/hh_positions.csv"

# Определяем массив с уникальными позициями
positions=("Junior" "Middle" "Senior")

# Проходим по каждой позиции в массиве
for position in "${positions[@]}"; do
    count=$(grep -o "$position" "$input_file" | wc -l)
    
    # Проверяем, найдено ли вхождение позиции
    if [ "$count" -eq 0 ]; then
        # Если позиция не найдена, записываем в файл 0
        echo "\"$position\",0"
    else
        # Если позиция найдена, записываем в файл количество вхождений
        echo "\"$position\",$count"
    fi
done >> hh_uniq_positions.csv  # Добавляем результаты в файл hh_uniq_positions.csv