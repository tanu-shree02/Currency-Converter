CURRENCY CONVERTER - PROGRAMMING SYSTEMS PRODUCT
================================================

PROJECT OVERVIEW
----------------
This project is a command-line currency converter developed as a
Programming Systems Product.

The application converts an amount from one supported currency to
another using exchange rates stored in an external rates.json file.

This version includes:
- Command-Line Interface (CLI)
- External configuration using rates.json
- Input validation
- Error handling
- File-based logging
- Automated unit tests
- Documentation


FEATURES
--------

1. Currency Conversion
   Converts amounts between supported currencies.

2. External Exchange Rates
   Exchange rates are stored in rates.json instead of being hardcoded
   directly inside the conversion logic.

3. Command-Line Interface
   Users can provide the source currency, target currency and amount
   through command-line arguments.

4. Input Validation
   The program handles negative amounts, zero amounts, non-numeric
   amounts and unsupported currency codes.

5. Error Handling
   User-friendly error messages are displayed instead of raw Python
   tracebacks.

6. Logging
   Successful operations and errors are recorded in app.log.

7. Automated Testing
   Unit tests cover successful conversions and failure cases.


SUPPORTED CURRENCIES
--------------------

The current rates.json uses USD as the base currency.

USD - US Dollar
INR - Indian Rupee
EUR - Euro
GBP - British Pound
JPY - Japanese Yen
AUD - Australian Dollar
CAD - Canadian Dollar
SGD - Singapore Dollar


EXCHANGE RATE CONFIGURATION
---------------------------

The current reference rates are:

1 USD = 1.00 USD
1 USD = 95.53 INR
1 USD = 0.86 EUR
1 USD = 0.74 GBP
1 USD = 159.32 JPY
1 USD = 1.39 AUD
1 USD = 1.39 CAD
1 USD = 1.27 SGD

These rates are stored as fixed reference values in rates.json.
They are not fetched from a live currency API.


USAGE
-----

The application is run using main.py.

Example:

python main.py --from USD --to EUR --amount 100

Example output:

100.00 USD = 86.00 EUR


MORE USAGE EXAMPLES
-------------------

USD to INR:

python main.py --from USD --to INR --amount 100

USD to GBP:

python main.py --from USD --to GBP --amount 100

USD to JPY:

python main.py --from USD --to JPY --amount 100


ERROR HANDLING
--------------

Negative amount:

python main.py --from USD --to INR --amount -100

Non-numeric amount:

python main.py --from USD --to INR --amount abc

Unsupported currency:

python main.py --from ABC --to INR --amount 100

The program displays clear, user-friendly error messages and does
not expose raw tracebacks to the user.


LOGGING
-------

Application operations and errors are recorded in:

app.log

The log can contain:
- Conversion requests
- Successful conversions
- Conversion errors
- Unexpected application errors


TESTING
-------

Automated unit tests are located in:

tests/test_converter.py

Run the tests with:

python -m pytest

The tests cover:
- Successful conversions
- Same-currency conversion
- Negative amounts
- Zero amounts
- Non-numeric amounts
- Unsupported source currency
- Unsupported target currency


FILES DESCRIPTION
-----------------

main.py
--------
Entry point of the application. It handles command-line arguments,
calls the currency converter and displays results.

src/converter.py
----------------
Contains the currency conversion logic, rate loading and validation.

src/logger.py
-------------
Provides logging functionality and writes application events and
errors to app.log.

rates.json
----------
Stores the exchange-rate configuration used by the application.

tests/test_converter.py
-----------------------
Contains automated unit tests for the currency converter.

app.log
-------
Stores application operations and error logs.
