def transformation_list():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]
    
    country_code = {}
    
    for country, code in list_of_tuples:
        if code in country_code:
            # Если код уже существует, добавляем новое значение в кортеж
            current_countries = country_code[code]
            country_code[code] = current_countries + (country,)  # Объединяем кортежи
        else:
            # Создаем новый ключ с кортежем значений
            country_code[code] = (country,)
    
    return country_code

def output_dict(func_dict):
    for code, countries in func_dict.items():
        # Проверяем, что countries является итерируемым объектом
        if isinstance(countries, (list, tuple)):
            for country in countries:
                print(f"'{code}' : '{country}'")
        else:
            print(f"'{code}' : '{countries}'")  # Обработка случая, если значение не итерируемое

def main():
    output_dict(transformation_list())

if __name__ == '__main__':
    main()