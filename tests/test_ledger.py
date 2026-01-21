"""
Unit tests for the Ledger class.
"""
from models.ledger import Ledger
from models.transaction import Transaction
from datetime import date

def test_add_and_len():
    ledger = Ledger()
    ledger.add(Transaction(10, "Food", "2025-12-06"))
    ledger.add(Transaction(20, "Transport", "2025-12-07"))

    assert len(ledger) == 2
    assert ledger.transactions[0]._id == 1
    assert ledger.transactions[1]._id == 2


def test_find_by_category():
    ledger = Ledger()
    ledger.add(Transaction(10, "Food", "2025-12-06"))
    ledger.add(Transaction(20, "Food", "2025-12-07"))
    ledger.add(Transaction(30, "Transport", "2025-12-08"))

    foods = ledger.find_by_category("Food")

    assert len(foods) == 2
    assert all(transaction.category == "Food" for transaction in foods)


def test_find_by_date_range():
    ledger = Ledger()
    ledger.add(Transaction(10, "Food", "2025-12-01"))
    ledger.add(Transaction(20, "Transport", "2025-12-05"))
    ledger.add(Transaction(300, "Rent", "2025-12-10"))

    result = ledger.find_by_date_range(date(2025,12,2), date(2025,12,8))

    assert len(result) == 1
    assert result[0].amount == 20


def test_monthly_summary():
    ledger = Ledger()
    ledger.add(Transaction(10, "Food", "2025-12-01"))
    ledger.add(Transaction(20, "Food", "2025-12-10"))
    ledger.add(Transaction(30, "Rent", "2025-11-15"))

    summary = ledger.monthly_summary()

    assert summary["2025-12"] == 30
    assert summary["2025-11"] == 30


def test_remove():
    ledger = Ledger()
    ledger.add(Transaction(10, "Food", "2025-12-06")) 
    ledger.add(Transaction(20, "Transport", "2025-12-07"))

    removed = ledger.remove(1)

    assert removed is True
    assert len(ledger) == 1
    assert ledger.transactions[0]._id == 2


def test_invalid_amount():
    try:
        Transaction(-5, "Food", "2025-12-06")
        assert False
    except ValueError:
        assert True


def run_all_tests():
    test_add_and_len()
    test_find_by_category()
    test_find_by_date_range()
    test_monthly_summary()
    test_remove()
    test_invalid_amount()


if __name__ == "__main__":
    print("Running ledger tests...")
    run_all_tests()
    print("Ledger tests passed.")