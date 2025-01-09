#!/bin/sh

# Проверка на наличие аргументов
if [ "$#" -lt 2 ]; then
    exit 1
fi

# Имя выходного файла
output_file="$1"

# Удаление выходного файла, если он существует
if [ -f "$output_file" ]; then
    rm "$output_file"
fi

# Запись заголовка в выходной файл
echo '"id","created_at","name","has_test","alternate_url"' > "$output_file"

# Объединение всех входных файлов в выходной файл
shift  # Удаляем первый аргумент 
for input_file in "$@"; do
    if [ -f "$input_file" ]; then
        tail -n +2 "$input_file" >> "$output_file"
    else
        echo "Файл $input_file не найден, пропускаем."
    fi
done