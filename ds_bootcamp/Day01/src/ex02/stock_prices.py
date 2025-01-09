import sys

def find_stock_by_name(name):

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
        name = COMPANIES[name]
        stock = STOCKS[name]
        print(stock)
    except:
        print('Unknown company')

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    find_stock_by_name(sys.argv[1])

if __name__ == '__main__':
    main()