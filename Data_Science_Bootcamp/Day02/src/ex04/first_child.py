import sys
from random import randint

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
                raise ValueError(f'Line {i}: Requires exactly 2 values, got {len(values)}')
            if i == 1:
                continue
            try:
                a, b = map(int, values)
            except ValueError:
                raise ValueError(f'Line {i}: Non-integer values')
            if {a, b} - {0, 1}:
                raise ValueError(f'Line {i}: Values must be 0 or 1')
            if a == b:
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
            print(f'Error: {error}')

    class Calculations:

        def __init__(self, list_lines):
            self.list_lines = list_lines

        def counts(self):
            heads = sum(1 for a, b in self.list_lines if int(a) == 1)
            tails = sum(1 for a, b in self.list_lines if int(a) == 0)
            return heads, tails
        
        def fractions(self, heads, tails):
            sum_count = heads + tails
            heads_percent =  round(heads / sum_count * 100, 2)
            tails_percent = round(tails / sum_count * 100, 2)
            return heads_percent, tails_percent
        
    class Analytics(Calculations):

        def predict_random(self, number):
            random_list = [[0, 1], [1, 0]]
            result = [random_list[randint(0, 1)] for i in range(number)]
            return result

        def predict_last(self):
            return self.list_lines[-1]

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Requires exactly 1 argument: filename')
        filename = sys.argv[1]
        research = Research(filename)
        for_print = research.file_reader()
        if for_print is not None:
            print(for_print)
            heads, tails = research.calculations.counts()
            print(heads, tails)
            heads_percent, tail_percent = research.calculations.fractions(heads, tails)
            print(heads_percent, tail_percent)
            print(research.analytics.predict_random(3))
            print(research.analytics.predict_last())
    except Exception as e:
        print(f'Error: {e}')