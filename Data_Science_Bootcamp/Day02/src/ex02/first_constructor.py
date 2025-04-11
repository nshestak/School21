import sys

class Research:

    def __init__(self, path):
        self.path = path

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

    def file_reader(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
                if self.check_lines(lines):
                    return ''.join(lines)
        except (FileNotFoundError, FileExistsError) as error:
            print(f'Error: {error}')


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Requires exactly 1 argument: filename')
        filename = sys.argv[1]
        research = Research(filename)
        for_print = research.file_reader()
        if for_print is not None:
            print(for_print)
    except Exception as e:
        print(f'Error: {e}')