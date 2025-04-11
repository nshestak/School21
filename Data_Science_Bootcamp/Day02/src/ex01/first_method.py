class Research:
    def fil_read(self):
        with open('../data/data.csv', 'r') as file:
            file_read = file.read()
        return file_read

if __name__ == '__main__':
    print(Research().fil_read())