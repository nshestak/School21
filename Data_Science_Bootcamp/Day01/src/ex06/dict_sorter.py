def create_dict():

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
        country_code[country] = code
    
    return country_code

def sorte_output(country_code):
    sorted_dict = dict(sorted(country_code.items(), key=lambda item: (-int(item[1]), item[0])))
    print(*sorted_dict, sep='\n')

def main():
    country_code = create_dict()
    sorte_output(country_code)

if __name__ == '__main__':
    main()