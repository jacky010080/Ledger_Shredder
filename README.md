# Ledger Shredder
A command-line expense tracking system built using Python.

## Overview
Ledger Shredder is a CLI-based expense tracker that helps users record, edit, delete, and review their personal spending.

## Features

### Expense Management
- Add new expenses with amount, category, date, and note
- Edit existing entries (amount, category, date, note)
- Delete entries by ID

### Data Viewing
- List all expenses
- Filter by category
- Filter by date range
- Show monthly spending summary
- Display total spending

### Persistence
- Saves all expenses to `expenses.csv` automatically on exit
- Loads saved data when the program starts

### Unit Testing
- Tests for Transaction validation and behavior
- Tests for Ledger add/remove/filter/update operations

## Installation
Ledger Shredder requires **Python 3.8+**.

**No third-party modules are required.**  
The project uses only the Python standard library (csv, pathlib, datetime, etc.).

## How to Run
Open terminal and navigate to the project folder:

```
cd ledger_shredder
```

Start the program:

```
python3 main.py
```

## Sample Input File
The project includes a sample input file located at:

data/expenses.csv

This file contains example transactions used for demonstration and testing.  
When the program starts, it automatically loads the entries from this file.  
Any changes made during execution (adding, editing, or deleting expenses) will be saved back to the same file.

If the file does not exist, the program will create it automatically on first save.

## Running Tests
Run the tests individually:
```
python3 -m tests.test_transaction
```
```
python3 -m tests.test_ledger
```

If successful:

```
Transaction tests passed.
``` 
``` 
Ledger tests passed.
``` 
