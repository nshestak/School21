def data_types():
    
    integer_var = 23                   # Целое число
    float_var = 23.01                  # Число с плавающей запятой
    string_var = "Hello, World!"       # Строка
    list_var = [1, 2, 3, 4, 5]         # Список
    tuple_var = (1, 2, 3)              # Кортеж
    dict_var = {"key": "value"}        # Словарь
    set_var = {1, 2, 3}                # Множество
    bool_var = True                    # Логический тип

    types_list = [
        type(integer_var).__name__,
        type(string_var).__name__,
        type(float_var).__name__,
        type(bool_var).__name__,
        type(list_var).__name__,
        type(dict_var).__name__,
        type(tuple_var).__name__,
        type(set_var).__name__
    ]

    print(types_list)

if __name__ == '__main__':
    data_types()
