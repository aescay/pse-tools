# PSE Tools (pse-tools)
A collection of useful Python scripts involving the Philippine Stock Exchange.

## Scripts
The list of scripts included in this collection are as follows:

### pse_quotes.py
Python Script which retrieves PSE stock quotes from the Open PSE Initiative.
See http://openpse.com/ for more information.

#### Usage
The pse_quotes.py script is invoked in the following manner:
```
    pse_quotes.py --stocks <stocks> --start <yyyy-mm-dd> --end <yyyy-mm-dd>
```
It can also be invoked in the following manner:
```
    pse_quotes.py -s <stocks> -st <yyyy-mm-dd> -ed <yyyy-mm-dd>
```

#### Arguments
The pse_quotes.py script takes in the following Command-Line arguments:
```
    stocks: optional, string, default=None
        The symbols of the stocks to retrieve, separated by commas.
        Simply not providing this option will mean that all stocks are to be selected.
    start: optional, string, default='1900-01-01'
        Retrieve quotes beginning from this date.
        This date should be in yyyy-mm-dd format.
    end: optional, string, default=datetime.date.today()
        Retrieve quotes up until this date.
        This date should be in yyyy-mm-dd format.
```

#### Input
The pse_quotes.py script does not read anything from Standard Input.
    
#### Output
The pse_quotes.py script dumps the following onto the Standard Output upon completion:
```
    [
        {
            "name": "<stock-name>",
            "price_close": "<closing-price>",
            "price_high": "<high-price>",
            "price_low": "<low-price>",
            "price_open": "<opening-price>",
            "quote_date": "<yyyy-mm-dd>",
            "symbol": "<stock-symbol>",
            "volume": <trade-volume>
        }
    ]
```
If the script fails, nothing is dumped onto the Standard Output.
See http://openpse.com/api/quotes/ for more information.

#### Use Cases
Some example use cases of the pse_quotes.py script are as follows:

* Get All Stock Quotes
```
    pse_quotes.py
```
* Get All Stock Quotes for BDO and BPI
```
    pse_quotes.py --stocks BDO,BPI
```
* Get All Stock Quotes for BDO since March 06, 2008
```
    pse_quotes.py --stocks BDO --start 2008-03-06
```
* Get All Stock Quotes for BPI up until August 21, 2012
```
    pse_quotes.py --stocks BPI --end 2012-08-21
```
* Get All Stock Quotes since September 2, 2010
```
    pse_quotes.py --stocks BPI --start 2010-09-02
```

## Development Notes
This project is being implemented using Python.

## Future Ideas
* Chrome/Firefox Extension which shows stock rating in your COL Financial Dashboard
* Computed recommended stock to be purchased next in COL based on rating, board lot, current cash, and stocks currently on hand (for diversitifcation purposes)

## References
* Open PSE Initiative: An open-source project which aims to store end-of-day quotes from the Philippines Stock Exchange and make it available to the public through a REST API. See http://openpse.com/ for more information.

## Author(s)
* Peñafiel, John Lawrence M. (https://github.com/penafieljlm/)

## Contact
Contact me at penafieljlm@gmail.com for any questions or concerns.
