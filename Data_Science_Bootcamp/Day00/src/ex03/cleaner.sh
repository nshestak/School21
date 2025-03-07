# Извлечение заголовка из файла hh.csv и запись его в новый файл hh_positions.csv
cat ../ex01/hh.csv | head -n 1 > hh_positions.csv

# Извлечение последних 20 строк из отсортированного файла hh_sorted.csv
# Обработка этих строк с помощью awk для форматирования и замены значений в третьем столбце
cat ../ex02/hh_sorted.csv | tail -n 20 | \
awk -F '",|,"' '{
    # Проверка значения в третьем столбце и замена его на соответствующее значение
    if ($3 ~ /Junior/) $3 = "\"Junior\""; 
    else if ($3 ~ /Middle/) $3 = "\"Middle\""; 
    else if ($3 ~ /Senior/) $3 = "\"Senior\""; 
    else $3 = "\"-\""; 
    # Печать строки с правильным форматом CSV
    print
}' | awk -F ' ' '{
    # Форматирование вывода для соответствия CSV-формату
    printf "%s\",%s\",%s,%s,\"%s\n", $1, $2, $3, $4, $5
}' >> hh_positions.csv  # Добавление отформатированной строки в файл hh_positions.csv
