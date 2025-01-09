#!/bin/sh

# Указываем путь к входному файлу, который будет обрабатываться
input_file="../ex03/hh_positions.csv"

# Используем tail для пропуска заголовка и начинаем цикл для чтения каждой строки файла
tail -n +2 "$input_file" | while IFS=',' read -r id created_at name has_test alternate_url; do
    # Извлекаем дату из поля created_at, оставляя только часть до 'T' (YYYY-MM-DD)
    date=$(echo "$created_at" | cut -d'T' -f1)
    
    # Проверяем, существует ли файл с именем, соответствующим дате
    if [ ! -f "${date}.csv" ]; then
        # Если файл не существует, создаем его и записываем заголовок
        echo '"id","created_at","name","has_test","alternate_url"' > "${date}.csv"
    fi
    
    # Форматируем строку и добавляем ее в соответствующий файл по дате
    echo "\"$id\",\"$created_at\",\"$name\",\"$has_test\",\"$alternate_url\"" >> "${date}.csv"
done