"""
Defines the Ledger class, which stores and manages all Transaction objects.
Provides functionality for adding, removing, filtering, updating, and summarizing expense data.
Used by main program actions for all expense operations.
"""
from .transaction import Transaction

class Ledger:
    """
    Manages a list of Transaction objects, including adding, removing, filtering, updating, and summarizing expenses.
    """

    def __init__(self):
        """
        Initialize an empty ledger.
        """
        self.transactions = []


    def add(self, transaction):
        """
        Add a Transaction to the ledger and automatically assign a sequential ID.
        """
        if not isinstance(transaction, Transaction):
            raise TypeError("Ledger can only store Transaction objects")

        # Assign incremental ID based on last transaction; start from 1 if ledger is empty.
        transaction._id = (self.transactions[-1]._id + 1) if self.transactions else 1
        self.transactions.append(transaction)

    
    def update(self, transaction_id, *, amount=None, category=None, date=None, note=None):
        """
        Update an existing transaction's fields by ID.
        Parameters are optional; only non-None values overwrite the old fields.
        Returns True if the transaction was found and updated, otherwise False.
        """
        for transaction in self.transactions:
            if transaction._id == transaction_id:
                if amount is not None:
                    transaction.amount = amount
                if category is not None:
                    transaction.category = category
                if date is not None:
                    transaction.date = date
                if note is not None:
                    transaction.note = note
                return True

        return False


    def remove(self, transaction_id):
        """
        Remove a transaction by ID. Returns True if removed, False otherwise.
        """
        for i, transaction in enumerate(self.transactions):
            if transaction._id == transaction_id:
                self.transactions.pop(i)
                return True
        return False


    def unique_categories(self):
        """Return a set of all categories."""
        return {transaction.category for transaction in self.transactions}
    

    def find_by_category(self, category):
        """
        Return a list of transactions whose category matches exactly.
        """
        return [transaction for transaction in self.transactions if transaction.category == category]


    def find_by_date_range(self, start_date, end_date):
        """
        Return all transactions whose date is between start_date and end_date (inclusive).
        """
        results = []
        for transaction in self.transactions:
            if start_date <= transaction.date <= end_date:
                results.append(transaction)
        return results


    def monthly_summary(self):
        """
        Return a dictionary mapping 'YYYY-MM' → total amount for that month.
        """
        # Build a summary where each key is 'YYYY-MM' and value is the sum of amounts in that month.
        summary = {}
        for transaction in self.transactions:
            month_key = transaction.date.strftime("%Y-%m")
            summary[month_key] = summary.get(month_key, 0) + transaction.amount
        return summary


    def __len__(self):
        """
        Return the number of transactions stored in the ledger.
        """
        return len(self.transactions)


    def __iter__(self):
        """
        Allow iteration over all transactions in the ledger.
        """
        return iter(self.transactions)