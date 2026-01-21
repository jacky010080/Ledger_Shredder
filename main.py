"""
Main entry point for Ledger Shredder.
Handles program flow, menu navigation, data loading, and saving.
"""
from data_io.storage import (
    load_csv,
    save_csv,
    rows_to_transactions,
    transactions_to_rows
)
from models.ledger import Ledger
from ui.messages import print_message
from ui.display import clear_screen, pause, show_menu
from actions.expense_actions import (
    add_expense,
    edit_expense,
    delete_expense,
    list_all_expenses,
    list_by_category,
    list_by_date_range,
    list_monthly_summary,
    show_total_amount
)

def load_data(ledger, filepath = "data/expenses.csv"):
    """
    Load CSV data into the ledger.
    """
    print_message("Loading saved data...", "blue")

    try:
        rows = load_csv(filepath)
        transactions = rows_to_transactions(rows)
    except Exception as e:
        print_message(f"Failed to load data: {e}", "red")
        return

    for transaction in transactions:
        ledger.add(transaction)

    print_message(f"Loaded {len(ledger)} transactions.", "green")


def save_data(ledger, filepath = "data/expenses.csv"):
    """
    Save ledger data back into CSV.
    """
    print_message("Saving data...", "blue")

    rows = transactions_to_rows(list(ledger))
    save_csv(filepath, rows)

    print_message("Data saved. Goodbye!", "green")


def handle_menu_choice(choice, ledger):
    """
    Handle a menu selection. Return False to exit the program.
    """
    if choice == "1":
        add_expense(ledger)
    elif choice == "2":
        edit_expense(ledger)
    elif choice == "3":
        delete_expense(ledger)
    elif choice == "4":
        list_all_expenses(ledger)
    elif choice == "5":
        list_by_category(ledger)
    elif choice == "6":
        list_by_date_range(ledger)
    elif choice == "7":
        list_monthly_summary(ledger)
    elif choice == "8":
        show_total_amount(ledger)
    elif choice == "9":
        return False
    else:
        print_message("Invalid choice, try again.", "yellow")

    pause()
    return True


def main():
    ledger = Ledger()

    # Load existing data
    load_data(ledger)
    pause()

    # Main program loop
    running = True
    while running:
        clear_screen()
        show_menu()
        choice = input("Select an option: ").strip()
        print()

        running = handle_menu_choice(choice, ledger)

    # Save when exit
    save_data(ledger)


if __name__ == "__main__":
    main()