"""
Input utilities for validating numeric and date user entries.
"""
from datetime import datetime
from ui.messages import print_message

def input_float(prompt_text):
    """
    Prompt until a valid float is entered.
    """
    while True:
        value_str = input(prompt_text)
        try:
            value = float(value_str)
            return value
        except ValueError:
            print_message("Invalid number, please try again.", "red")


def input_date(prompt_text):
    """
    Prompt until a valid YYYY-MM-DD date is entered.
    """
    while True:
        date_str = input(prompt_text).strip()
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print_message("Invalid date format. Please use YYYY-MM-DD.", "red")