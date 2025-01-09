import sys

def call_center(clients, recipients):
    list_call_center = [item for item in clients if item not in recipients]
    list_call_center = list(set(list_call_center))
    return list_call_center

def potential_client(clients, participants):
    list_potential_client = [item for item in participants if item not in clients]
    list_potential_client = list(set(list_potential_client))
    return list_potential_client

def loyalty_program(clients, participants):
    list_loyalty_program = [item for item in clients if item not in participants]
    list_loyalty_program = list(set(list_loyalty_program))
    return list_loyalty_program

def handle_command(command):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']

    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    
    command_map = {
        'call_center': call_center(clients, recipients),
        'potential_client': potential_client(clients, participants),
        'loyalty_program': loyalty_program(clients, participants)
    }

    if command in command_map:
        print(command_map[command])
    else:
        sys.exit('There is no such task')

def main():
    if len(sys.argv) != 2:
        sys.exit('No arguments or more than two')
    else:
        handle_command(sys.argv[1])

if __name__ == '__main__':
    main()