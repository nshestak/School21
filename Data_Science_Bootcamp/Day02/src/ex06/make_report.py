from analytics import Research
from config import *

if __name__ == '__main__':
    try:
        research = Research(file_path)
        for_print = research.file_reader()
        if for_print is not None:
            heads, tails = research.calculations.counts(for_print)
            heads_percent, tail_percent = research.calculations.fractions(heads, tails)
            result_random = research.analytics.predict_random(number_random)
            heads_new, tails_new = research.calculations.counts(result_random)
            text = template.format(heads + tails, tails, heads, tail_percent, heads_percent,
                                   number_random, tails_new, heads_new)
            research.save_file(text, file_output)
            research.send_message(status=True)
        else:
            research.send_message(status=False)
    except Exception as e:
        if research is not None:
            research.send_message(status=False)
        print(f'Error: {e}')