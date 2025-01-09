import sys

import sys

def find_stock_by_ticker(ticker):

    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    try:
        key = next((key for key, value in COMPANIES.items() if value == ticker), None)
        stock = STOCKS[ticker]
        print(f'{key} {stock}')
    except:
        print('Unknown company')

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    find_stock_by_ticker(sys.argv[1])

if __name__ == '__main__':
    main()