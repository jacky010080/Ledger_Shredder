"""
Defines the Transaction class, which represents a single expense entry.
A Transaction includes amount, category, date, note, and validation logic.
This class is used throughout the program as the fundamental data unit.
"""
from datetime import date, datetime

class Transaction:
    """
    Represents a single expense record.
    Each Transaction stores amount, category, date, an optional note, and a private ID.
    The class also handles date parsing and input validation.
    """

    def __init__(self, amount, category, date_str, note="", _id=None):
        """
        Create a new Transaction.

        Parameters:
            amount: The expense amount (must be > 0).
            category: The category name.
            date_str: The date string in YYYY-MM-DD format.
            note: Optional note.
            _id: Optional ID assigned by Ledger.
        """
        self.amount = amount
        self.category = category
        self.date = self._parse_date(date_str)
        self.note = note
        self._id = _id

        self._validate()


    def _parse_date(self, date_str):
        """
        Convert YYYY-MM-DD string into a real datetime.date object.
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Use YYYY-MM-DD.")
        

    def _validate(self):
        """
        Validate the transaction fields.
        Raises ValueError if any attribute is invalid.
        """
        if self.amount <= 0:
            raise ValueError("Amount must be > 0")

        if not isinstance(self.category, str) or not self.category.strip():
            raise ValueError("Category must be a non-empty string")

        if not isinstance(self.date, date):
            raise ValueError("Date must be a datetime.date object")
        

    def __lt__(self, other):
        """
        Define how transactions are compared when sorting.
        """
        # Sort primarily by date; if equal, fall back to ID for consistent ordering.
        id_self = self._id if self._id is not None else 0
        id_other = other._id if other._id is not None else 0
        return (self.date, id_self) < (other.date, id_other)


    def __repr__(self):
        """
        Return a developer-friendly string representation of the transaction.
        """
        return (f"Transaction(id={self._id}, amount={self.amount}, "
                f"category='{self.category}', date={self.date}, note='{self.note}')")