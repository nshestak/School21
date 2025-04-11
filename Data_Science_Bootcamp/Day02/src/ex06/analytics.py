from random import randint
import logging
import requests
from config import TOKEN, CHAT_ID

logging.basicConfig(level=logging.INFO, filename='analytics.log', filemode='a',
                    format='%(asctime)s %(levelname)s %(message)s')

class Research:

    def __init__(self, path):
        self.path = path
        self.list_file_lines = self.file_reader()
        self.calculations = self.Calculations(self.list_file_lines)
        self.analytics = self.Analytics(self.list_file_lines)

    def check_lines(self, lines):
        for i, line in enumerate(lines, 1):
            values = line.strip().split(',')
            if len(values) != 2:
                logging.error(f'Line {i}: Requires exactly 2 values, got {len(values)}')
                raise ValueError(f'Line {i}: Requires exactly 2 values, got {len(values)}')
            if i == 1:
                continue
            try:
                a, b = map(int, values)
            except ValueError:
                logging.error(f'Line {i}: Non-integer values')
                raise ValueError(f'Line {i}: Non-integer values')
            if {a, b} - {0, 1}:
                logging.error(f'Line {i}: Values must be 0 or 1')
                raise ValueError(f'Line {i}: Values must be 0 or 1')
            if a == b:
                logging(f'Line {i}: Values must be different')
                raise ValueError(f'Line {i}: Values must be different')
        return True
    
    def to_list(self, lines, has_header):
        arg = 1 if has_header else 0
        list_lines = [list(map(int, line.strip().split(','))) for line in lines[arg:]]
        return list_lines

    def file_reader(self, has_header=True):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
                if self.check_lines(lines):
                    list_file_lines = self.to_list(lines, has_header)
                    return list_file_lines
        except (FileNotFoundError, FileExistsError) as error:
            logging.error(f'Error: {error}')

    def save_file(self, text, filename, extension='txt'):
        try:
            with open(f'{filename}.{extension}', 'w') as file:
                file.write(text)
        except (FileNotFoundError, FileExistsError) as error:
            logging.error(f'Error: {error}')

    def send_message(self, status):
        if status:
            payload = {'chat_id': CHAT_ID, 'text': 'The report has been successfully created'}
        else:
            payload = {'chat_id': CHAT_ID, 'text': 'The report hasn’t been created due to an error'}
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json=payload)
        if response.status_code == 200:
            logging.info('Send message')
        else:
            logging.error(f'Don`t send message, status code: {response.status_code}')

    class Calculations:

        def __init__(self, list_lines):
            self.list_lines = list_lines

        def counts(self, list_lines):
            heads = sum(1 for a, b in list_lines if int(a) == 1)
            tails = sum(1 for a, b in list_lines if int(a) == 0)
            logging.info('Calculation counts')
            return heads, tails
        
        def fractions(self, heads, tails):
            sum_count = heads + tails
            heads_percent =  round(heads / sum_count * 100, 2)
            tails_percent = round(tails / sum_count * 100, 2)
            logging.info('Calculation fractions')
            return heads_percent, tails_percent
        
    class Analytics(Calculations):

        def predict_random(self, number):
            random_list = [[0, 1], [1, 0]]
            result = [random_list[randint(0, 1)] for i in range(number)]
            logging.info(f'Analytics {number} predict')
            return result

        def predict_last(self):
            logging.info('Return last')
            return self.list_lines[-1]