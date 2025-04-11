class Must_read:
    with open('../data/data.csv', 'r') as file:
        print(file.read())


if __name__ == '__main__':
    Must_read()