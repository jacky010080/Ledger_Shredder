"""
UI helpers for screen control and main menu display.
"""
import os
from ui.messages import print_message
from ui.logo import LEDGER_SHREDDER_LOGO

def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """
    Pause execution until user presses Enter.
    """
    print_message("\nPress Enter to continue...", "info")
    input()


def show_menu():
    """
    Display the main program menu.
    """
    print_message(LEDGER_SHREDDER_LOGO, "title")

    print_message("1. Add new expense", "info")
    print_message("2. Edit expense", "info")
    print_message("3. Delete expense", "info")
    print_message("4. List all expenses", "info")
    print_message("5. List by category", "info")
    print_message("6. List by date range", "info")
    print_message("7. Monthly summary", "info")
    print_message("8. Show total spending", "info")
    print()

    print_message("9. Save & Exit", "yellow")
    print_message("-" * 40, "title")
