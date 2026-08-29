"""Command-line interface for the currency converter."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.converter import (
    CurrencyConverterError,
    convert_currency,
    load_rates,
)
from src.logger import setup_logger


BASE_DIR = Path(__file__).resolve().parent
RATES_FILE = BASE_DIR / "rates.json"
LOG_FILE = BASE_DIR / "app.log"


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Convert an amount from one currency to another."
    )
    parser.add_argument(
        "--from",
        dest="from_currency",
        required=True,
        help="Source currency code, e.g. INR",
    )
    parser.add_argument(
        "--to",
        dest="to_currency",
        required=True,
        help="Target currency code, e.g. USD",
    )
    parser.add_argument(
        "--amount",
        required=True,
        help="Amount to convert, e.g. 1000",
    )
    return parser


def main() -> int:
    """Run the CLI application."""
    logger = setup_logger(LOG_FILE)
    parser = build_parser()

    try:
        args = parser.parse_args()

        try:
            amount = float(args.amount)
        except (TypeError, ValueError):
            message = "Invalid amount: please enter a numeric value, e.g. 1000."
            logger.error(message)
            print(f"Error: {message}")
            return 1

        rates = load_rates(RATES_FILE)
        result = convert_currency(
            amount,
            args.from_currency,
            args.to_currency,
            rates,
        )

        from_code = args.from_currency.strip().upper()
        to_code = args.to_currency.strip().upper()

        logger.info(
            "Conversion successful | %.2f %s -> %.2f %s",
            amount,
            from_code,
            result,
            to_code,
        )

        print(f"{amount:,.2f} {from_code} = {result:,.2f} {to_code}")
        return 0

    except CurrencyConverterError as exc:
        logger.error("Conversion failed | %s", exc)
        print(f"Error: {exc}")
        return 1
    except OSError as exc:
        logger.error("System error | %s", exc)
        print("Error: Unable to access the required application file.")
        return 1
    except Exception as exc:
        # Last-resort protection: users should never see a traceback.
        logger.exception("Unexpected application error | %s", exc)
        print("Error: An unexpected problem occurred. Check app.log for details.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
