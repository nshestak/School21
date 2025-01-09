import sys

def read_file(file_path):
    with open(file_path, mode='r', newline='') as file:
        return file.readlines()

def create_table(file_path, data):
    with open(file_path, mode='w', newline='') as tsv_file:
        tsv_file.write('Name\tSurname\tE-mail\n')
        for line in data:
            name = line.split('.')[0].capitalize()
            surname = line.split('.')[1].split('@')[0].capitalize()
            tsv_file.write(f'{name}\t{surname}\t{line}')

def main():
    tsv_file_path = 'employees.tsv'

    if len(sys.argv) != 2:
        sys.exit('No arguments or more than two')
    else:
        file_readlines = read_file(sys.argv[1])
        create_table(tsv_file_path, file_readlines)

if __name__ == '__main__':
    main()