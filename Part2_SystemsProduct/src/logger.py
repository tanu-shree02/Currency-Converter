"""Application logging configuration."""

import logging
from pathlib import Path


def setup_logger(log_file: str | Path = "app.log") -> logging.Logger:
    """Create and configure the application logger."""
    logger = logging.getLogger("currency_converter")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
