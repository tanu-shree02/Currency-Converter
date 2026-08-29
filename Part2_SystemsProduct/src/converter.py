"""Core currency conversion logic using rates loaded from a JSON file."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


class CurrencyConverterError(Exception):
    """Base exception for expected converter errors."""


class UnsupportedCurrencyError(CurrencyConverterError):
    """Raised when a currency is not available in the rates file."""


class InvalidAmountError(CurrencyConverterError):
    """Raised when an amount is not a positive number."""


def load_rates(rates_file: str | Path) -> Dict[str, float]:
    """Load currency rates from a JSON file.

    Rates are expressed relative to USD. For example, INR: 95.24 means
    1 USD = 95.24 INR.
    """
    path = Path(rates_file)

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise CurrencyConverterError(f"Rates file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CurrencyConverterError("Rates file contains invalid JSON.") from exc
    except OSError as exc:
        raise CurrencyConverterError(f"Could not read rates file: {exc}") from exc

    if not isinstance(data, dict) or not data:
        raise CurrencyConverterError("Rates file must contain a non-empty JSON object.")

    rates: Dict[str, float] = {}
    for currency, rate in data.items():
        code = str(currency).upper()
        if not isinstance(rate, (int, float)) or isinstance(rate, bool) or rate <= 0:
            raise CurrencyConverterError(
                f"Invalid exchange rate for currency '{code}'."
            )
        rates[code] = float(rate)

    if "USD" not in rates:
        raise CurrencyConverterError("Rates file must contain a USD rate.")

    return rates


def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
    rates: Dict[str, float],
) -> float:
    """Convert an amount between two currencies.

    Rates are relative to USD.
    """
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise InvalidAmountError("Amount must be a number.")

    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0.")

    from_code = from_currency.strip().upper()
    to_code = to_currency.strip().upper()

    if from_code not in rates:
        raise UnsupportedCurrencyError(
            f"Unsupported source currency: {from_code}"
        )

    if to_code not in rates:
        raise UnsupportedCurrencyError(
            f"Unsupported target currency: {to_code}"
        )

    # Convert source -> USD -> target.
    amount_in_usd = amount / rates[from_code]
    converted = amount_in_usd * rates[to_code]

    return converted
