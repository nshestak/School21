import sys

def search_company_ticker(str):
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
    
    # Создаем обратный словарь для быстрого поиска компании по тикеру
    TICKER_TO_COMPANY = {v: k for k, v in COMPANIES.items()}

    for item in str:
        company = item.lower().capitalize()
        ticker = item.upper()
        if company in COMPANIES:
            stock_price = STOCKS[COMPANIES[company]]
            print(f'{company} stock price is {stock_price}')
        elif ticker in STOCKS:
            company_name = TICKER_TO_COMPANY.get(ticker, None)
            print(f'{ticker} is a ticker symbol for {company_name}')
        else:
            print(f'{item} is an unknown company or an unknown ticker symbol')


def processing_str(str):
    list_str = []
    for s in str.split(','):
        if s.strip().isalpha():
            list_str.append(s.strip())
        else:
            return
    return list_str
    
def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    list_str = processing_str(sys.argv[1])
    if list_str == None:
        sys.exit(1)
    else:
        search_company_ticker(list_str)
    
if __name__ == '__main__':
    main()