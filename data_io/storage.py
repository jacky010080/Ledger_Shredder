"""
CSV storage utilities for loading and saving transaction data.
"""
import csv
from pathlib import Path
from models.transaction import Transaction

def load_csv(path):
    """
    Read a CSV file and return a list of dict rows. Return empty list if missing.
    """
    rows = []
    try:
        p = Path(path)
        if not p.exists():
            return []

        with p.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

    except (OSError, csv.Error) as e:
        raise RuntimeError(f"Failed to read CSV: {e}")

    else:
        return rows
    
def rows_to_transactions(rows):
    """
    Convert CSV dict rows to Transaction objects.
    """
    transactions = []

    for row in rows:
        transaction = Transaction(
            amount=float(row["amount"]),
            category=row["category"],
            date_str=row["date"],
            note=row.get("note", ""),
            # Use existing ID if present.
            _id=int(row["id"]) if row.get("id") else None,
        )
        transactions.append(transaction)

    # Sort by date.
    transactions.sort()
    return transactions

def transactions_to_rows(transactions):
    """
    Convert Transaction objects into dict rows for CSV writing.
    """
    return [
        {
            "id": transaction._id,
            "amount": transaction.amount,
            "category": transaction.category,
            "date": transaction.date.isoformat(),
            "note": transaction.note,
        }
        for transaction in transactions
    ]

def save_csv(path, rows):
    """
    Write dict rows into a CSV file.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["id", "amount", "category", "date", "note"]

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
