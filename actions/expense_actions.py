"""
Contains all user-facing actions, including adding, editing, deleting, and listing expenses.
Called by main.py.
"""
from ui.table import format_table
from ui.input_utils import input_float, input_date
from ui.messages import print_message
from datetime import datetime
from models.transaction import Transaction

def add_expense(ledger):
    """
    Prompt the user for amount, category, date, and note, create a new Transaction, and add it to the ledger.
    """
    print_message("\n=== Add Expense ===", "title")

    amount = input_float("Amount: ")
    category = input("Category: ")
    date_obj = input_date("Date (YYYY-MM-DD): ")
    note = input("Note (optional): ")

    try:
        transaction = Transaction(amount, category, date_obj.isoformat(), note)
        ledger.add(transaction)
        print_message("Transaction added successfully!", "green")
    except Exception as e:
        print_message(f"Failed to add transaction: {e}", "red")


def edit_expense(ledger):
    """
    Edit an existing expense by ID.
    Shows current values and allows the user to update any field.
    Pressing Enter keeps the original value.
    """
    print_message("\n=== Edit Expense ===", "title")

    list_all_expenses(ledger)

    try:
        transaction_id = int(input("Enter ID to edit: ").strip())
    except ValueError:
        print_message("Invalid ID.", "red")
        return

    # Find the first transaction matching the given ID, or None if not found.
    target_transaction = next((transaction for transaction in ledger if transaction._id == transaction_id), None)
    if not target_transaction:
        print_message("No transaction found with that ID.", "red")
        return

    print_message(f"Current amount: {target_transaction.amount}", "info")
    print_message(f"Current category: {target_transaction.category}", "info")
    print_message(f"Current date: {target_transaction.date}", "info")
    print_message(f"Current note: {target_transaction.note}\n", "info")
    print_message("Press Enter to keep the current value for any field.", "info")

    # Pressing Enter keeps the original amount (represented by None)
    new_amt_str = input(f"New amount (current {target_transaction.amount}): ").strip()
    if new_amt_str:
        try:
            new_amount = float(new_amt_str)
        except ValueError:
            print_message("Invalid amount. Edit cancelled.", "red")
            return
    else:
        new_amount = None

    # Pressing Enter keeps the original category (represented by None).
    new_category = input(f"New category (current '{target_transaction.category}'): ").strip()
    if not new_category:
        new_category = None
    
    # Pressing Enter keeps the original date (represented by None).
    new_date_str = input(f"New date (YYYY-MM-DD, current {target_transaction.date}): ").strip()
    if new_date_str:
        try:
            new_date = datetime.strptime(new_date_str, "%Y-%m-%d").date()
        except ValueError:
            print_message("Invalid date format. Edit cancelled.", "red")
            return
    else:
        new_date = None

    # Pressing Enter keeps the original note (represented by None).
    new_note = input(f"New note (current '{target_transaction.note}'): ").strip()
    if not new_note:
        new_note = None

    # Apply all updates (only fields with new values will be overwritten).
    ledger.update(
        transaction_id,
        amount=new_amount,
        category=new_category,
        date=new_date,
        note=new_note
    )

    print_message("Transaction updated.", "green")


def delete_expense(ledger):
    """
    Delete a transaction by ID.
    Shows the full expense list first, then asks the user for confirmation.
    """
    print_message("\n=== Delete Expense ===", "title")

    if len(ledger) == 0:
        print_message("No expenses to delete.", "red")
        return

    list_all_expenses(ledger)
    choice = input("Enter the ID to delete (or 'cancel'): ").strip()

    if choice.lower() == "cancel":
        print_message("Cancelled.", "yellow")
        return

    if not choice.isdigit():
        print_message("Invalid input.", "red")
        return
    
    transaction_id = int(choice)

    if ledger.remove(transaction_id):
        print_message(f"Transaction {transaction_id} deleted.", "green")
    else:
        print_message("ID not found.", "red")


def list_all_expenses(ledger):
    """
    Display all expenses stored in the ledger in a formatted table.
    """
    print_message("\n=== Expense List ===", "title")

    if len(ledger) == 0:
        print_message("No expenses recorded.", "yellow")
        return

    rows = []
    for transaction in ledger:
        rows.append([
            transaction._id,
            f"${transaction.amount:.2f}",
            transaction.category,
            transaction.date.isoformat(),
            transaction.note
        ])

    headers = ["ID", "Amount", "Category", "Date", "Note"]
    print(format_table(rows, headers))


def list_all_categories(ledger):
    """
    Show all unique categories currently present in the ledger.
    """
    print_message("\n=== All Categories ===", "title")

    categories = ledger.unique_categories()

    if not categories:
        print_message("No categories found.", "yellow")
        return

    for category in sorted(categories):
        print_message(f"- {category}", "info")


def list_by_category(ledger):
    """
    Display expenses filtered by a specific category.
    Shows category list first, then prints results in table format.
    """
    print_message("\n=== List Expenses by Category ===", "title")

    # Show available categories to help user make a valid selection.
    list_all_categories(ledger)

    category = input("Enter category: ").strip()
    result = ledger.find_by_category(category)

    if not result:
        print_message("No expenses found for this category.", "yellow")
        return

    rows = []
    for transaction in result:
        rows.append([
            transaction._id,
            f"${transaction.amount:.2f}",
            transaction.category,
            transaction.date.isoformat(),
            transaction.note
        ])

    headers = ["ID", "Amount", "Category", "Date", "Note"]
    print(format_table(rows, headers))


def list_by_date_range(ledger):
    """
    Ask the user for a start and end date, then display all expenses
    within that inclusive date range.
    """
    print_message("\n=== List by Date Range ===", "title")

    # Prompt user for two valid dates using input_date.
    start_date = input_date("Start date (YYYY-MM-DD): ")
    end_date = input_date("End date (YYYY-MM-DD): ")

    result = ledger.find_by_date_range(start_date, end_date)

    if not result:
        print_message("No expenses in this date range.", "yellow")
        return

    rows = []
    for transaction in result:
        rows.append([
            transaction._id,
            f"${transaction.amount:.2f}",
            transaction.category,
            transaction.date.isoformat(),
            transaction.note
        ])

    headers = ["ID", "Amount", "Category", "Date", "Note"]
    print(format_table(rows, headers))


def list_monthly_summary(ledger):
    """
    Display a summary of total spending for each month (YYYY-MM).
    """
    print_message("\n=== Monthly Summary ===", "title")

    summary = ledger.monthly_summary()

    if not summary:
        print_message("No expenses recorded.", "yellow")
        return

    rows = []
    for month in sorted(summary.keys()):
        rows.append([
            month,
            f"${summary[month]:.2f}"
        ])

    headers = ["Month", "Total"]
    print(format_table(rows, headers))


def show_total_amount(ledger):
    """
    Display the total spending across all transactions in the ledger.
    """
    print_message("\n=== Total Amount ===", "title")

    if len(ledger) == 0:
        print_message("No expenses yet.", "yellow")
        return

    # Compute total spending by summing all transaction amounts.
    total = sum(transaction.amount for transaction in ledger)
    print_message(f"Total: ${total}", "info")