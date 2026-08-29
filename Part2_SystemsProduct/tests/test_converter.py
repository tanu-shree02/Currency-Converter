"""Unit tests for the currency converter."""

import json

import pytest

from src.converter import (
    CurrencyConverterError,
    InvalidAmountError,
    UnsupportedCurrencyError,
    convert_currency,
    load_rates,
)


@pytest.fixture
def rates():
    return {
        "USD": 1.00,
        "INR": 95.53,
        "EUR": 0.86,
        "GBP": 0.74,
        "JPY": 159.32,
        "AUD": 1.39,
        "CAD": 1.39,
        "SGD": 1.27,
    }


def test_usd_to_inr(rates):
    assert convert_currency(100, "USD", "INR", rates) == pytest.approx(95.0)


def test_inr_to_usd(rates):
    assert convert_currency(9553, "INR", "USD", rates) == pytest.approx(100.0)


def test_eur_to_gbp(rates):
    expected = (100 / 0.86) * 0.74
    assert convert_currency(100, "EUR", "GBP", rates) == pytest.approx(expected)


def test_currency_codes_are_case_insensitive(rates):
    assert convert_currency(95.53, "inr", "usd", rates) == pytest.approx(1.0)


def test_zero_amount_is_rejected(rates):
    with pytest.raises(InvalidAmountError, match="greater than 0"):
        convert_currency(0, "USD", "INR", rates)


def test_negative_amount_is_rejected(rates):
    with pytest.raises(InvalidAmountError, match="greater than 0"):
        convert_currency(-10, "USD", "INR", rates)


def test_non_numeric_amount_is_rejected(rates):
    with pytest.raises(InvalidAmountError, match="must be a number"):
        convert_currency("abc", "USD", "INR", rates)


def test_unsupported_source_currency(rates):
    with pytest.raises(UnsupportedCurrencyError, match="Unsupported source"):
        convert_currency(100, "ABC", "USD", rates)


def test_unsupported_target_currency(rates):
    with pytest.raises(UnsupportedCurrencyError, match="Unsupported target"):
        convert_currency(100, "USD", "XYZ", rates)


def test_load_rates(tmp_path):
    rates_file = tmp_path / "rates.json"
    rates_file.write_text(
        json.dumps({
            "USD": 1,
            "INR": 95.53,
            "EUR": 0.86,
            "GBP": 0.74,
            "JPY": 159.32,
            "AUD": 1.39,
            "CAD": 1.39,
            "SGD": 1.27,
        }),
        encoding="utf-8",
    )

    loaded = load_rates(rates_file)

    assert loaded["USD"] == 1.0
    assert loaded["INR"] == 95.53
    assert loaded["EUR"] == 0.86
    assert loaded["GBP"] == 0.74
    assert loaded["JPY"] == 159.32
    assert loaded["AUD"] == 1.39
    assert loaded["CAD"] == 1.39
    assert loaded["SGD"] == 1.27



def test_missing_rates_file(tmp_path):
    with pytest.raises(CurrencyConverterError, match="not found"):
        load_rates(tmp_path / "missing.json")


def test_invalid_rates_json(tmp_path):
    rates_file = tmp_path / "rates.json"

    rates_file.write_text(
        "{invalid",
        encoding="utf-8",
    )

    with pytest.raises(CurrencyConverterError, match="invalid JSON"):
        load_rates(rates_file)