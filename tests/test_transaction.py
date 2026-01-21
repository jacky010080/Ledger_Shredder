"""
Unit tests for the Transaction class.
"""
from models.transaction import Transaction
from datetime import date

def test_create_transaction():
    transaction = Transaction(10, "Food", "2025-12-01")

    assert transaction.amount == 10
    assert transaction.category == "Food"
    assert transaction.date == date(2025, 12, 1)


def test_invalid_date():
    # Invalid date string should raise ValueError
    try:
        Transaction(10, "Food", "invalid-date")
        assert False
    except ValueError:
        assert True


def test_invalid_amount():
    # Amount must be positive
    try:
        Transaction(0, "Food", "2025-12-01")
        assert False
    except ValueError:
        assert True


def test_repr_contains_fields():
    transaction = Transaction(10, "Food", "2025-12-01")
    representation = repr(transaction)

    assert "Food" in representation
    assert "10" in representation


def test_lt_sorting():
    transaction1 = Transaction(10, "Food", "2025-12-01", _id=1)
    transaction2 = Transaction(20, "Rent", "2025-12-02", _id=2)

    assert transaction1 < transaction2


def run_all_tests():
    test_create_transaction()
    test_invalid_date()
    test_invalid_amount()
    test_repr_contains_fields()
    test_lt_sorting()


if __name__ == "__main__":
    print("Running transaction tests...")
    run_all_tests()
    print("Transaction tests passed.")