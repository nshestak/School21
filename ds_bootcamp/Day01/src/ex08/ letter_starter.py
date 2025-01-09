import sys

def read_file(file_path):
    with open(file_path, mode='r', newline='') as file:
        return file.readlines()
    
def find_name(data, email):
    email_found = False
    for line in data[1:]:
        name_surname_email = line.split('\t')
        if name_surname_email[2].strip() == email:
            print(f'Dear {name_surname_email[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')
            email_found = True
            break
    if not email_found:
        print(f'Error: No entry found for the email "{email}".')
    
def main():
    tsv_file = 'employees.tsv'
    if len(sys.argv) != 2:
        sys.exit('No arguments or more than two.')
    else:
        data = read_file(tsv_file)
        find_name(data, sys.argv[1])

if __name__ == '__main__':
    main()