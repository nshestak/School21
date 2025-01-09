def read_csv(file_path):
    """Читает данные из CSV файла и возвращает их в виде списка строк."""
    with open(file_path, mode='r', newline='') as csv_file:
        return csv_file.readlines()
    
def write_tsv(file_path, data):
    """Записывает данные в TSV файл."""
    with open(file_path, mode='w', newline='') as tsv_file:
        for line in data:
            line = line.replace(', ', '#') # Заменяем запятую с пробелом на #
            line = line.replace(',', '\t') # Заменяем запятую на табуляцию
            line = line.replace('#', ', ') # Восстанавливаем запятую с пробелом
            tsv_file.write(line)

def main():
    csv_file_path = 'ds.csv'
    tsv_file_path = 'ds.tsv'

    data = read_csv(csv_file_path)
    write_tsv(tsv_file_path, data)

if __name__ == "__main__":
    main()