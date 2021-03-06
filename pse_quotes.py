#! /usr/bin/python

"""
    Python Script which retrieves PSE stock quotes from the Open PSE Initiative.
    See http://openpse.com/ for more information.
"""
# __author__ = "John Lawrence M. Penafiel"
# __copyright__ = "Copyright 2015, John Lawrence M. Penafiel"
# __credits__ = ["John Lawrence M. Penafiel"]
# __maintainer__ = ["John Lawrence M. Penafiel"]
# __email__ = "penafieljlm@gmail.com"
# __status__ = "Prototype"

import argparse
import datetime
import json
import requests
import sys

# define date type
def date(value):
    try:
        return datetime.date(*(int(x) for x in value.split('-')))
    except:
        raise argparse.ArgumentTypeError("%s is an invalid date value" % value)

def get_quote():

    # parse arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-s', '--stocks',
                        help='the symbols of the stocks to retrieve, separated by commas',
                        default=None)
    
    parser.add_argument('-st', '--start',
                        type=date,
                        help='[yyyy-mm-dd] retrieve quotes beginning from this date',
                        default=datetime.date(1900, 1, 1).__str__())
    
    parser.add_argument('-ed', '--end',
                        type=date,
                        help='[yyyy-mm-dd] retrieve quotes up until this date',
                        default=datetime.date.today().__str__())
    
    args = parser.parse_args()

    # determine relevant companies
    targets = None
    if args.stocks is not None:
        targets = []
        for stock in args.stocks.split(','):
            stock = stock.strip().upper()
            if stock not in targets:
                targets.append(stock)

    # tests the api to see if it's running and gets a list of stocks
    response = requests.get('http://phisix-api.appspot.com/stocks.json')
    if response.status_code != 200:
        sys.exit()
    companies = json.loads(response.text)
    
    # makes sure the stock exists so that only valid stock codes are pulled
    stocks = []
    for company in companies['stock']:
        if targets is None or company['symbol'].upper() in targets:
            stocks.append(company['symbol'].upper())
    
    # request stock quotes per company
    quotes = []
    for stock in stocks:
        response = requests.get('http://openpse.com/api/quotes/?{parameters}'.format(
                                parameters='&'.join((
                                'stocks={stock}'.format(stock=stock),
                                'from_date={start}'.format(start=args.start),
                                'to_date={end}'.format(end=args.end)
                                ))))
        if response.status_code != 200:
            continue
        stock_quotes = json.loads(response.text)
        for quote in stock_quotes:
            quotes.append(quote)
    
    # dump results
    return json.dumps(quotes, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":
    data = get_quote()
    print(data)