LibraNet

LibraNet is a modern command-line library management system that manages books, audiobooks, and e-magazines. It demonstrates clean object-oriented design, extensibility, and professional software practices in Python. The system supports borrowing, returning, fines, receipts, searching, and tabular displays with persistent JSON-based storage.

Features

Borrow and Return

Tracks due dates and automatically calculates fines.

Grace period is configurable through constants.

Terminal User Interface

Built using the rich library for tables, colors, and panels.

Clear status messages for success, warnings, and errors.

Support for Multiple Media Types

Books with page counts.

Audiobooks with playback durations.

E-magazines with issue numbers and archiving capabilities.

Search and Filter

Search items by title, author, or type.

Results are shown in formatted tables.

Receipts and Transactions

Each borrow and return generates a receipt.

All transactions are stored in JSON for history and auditing.

Persistent Data Management

Library items and fines are saved in library.json.

Automatic backups are created.

Corrupted or missing data is handled gracefully.

Statistics Dashboard

Displays total items, borrowed versus available counts, and total fines collected.

Project Structure
LibraNet/
│── main.py               # Entry point with menu system
│── data_manager.py       # JSON load, save, and backup
│── library_manager.py    # Business logic for borrow, return, search
│── models/
│   ├── base_item.py      # Abstract class for all items
│   ├── book.py           # Book implementation
│   ├── audiobook.py      # Audiobook implementation
│   ├── emagazine.py      # E-magazine implementation
│── utils/
│   ├── ui.py             # Rich-based UI and tables
│   ├── receipt.py        # Receipt generation and storage
│   └── constants.py      # Configurations for fines, grace period, colors
│── data/
│   ├── library.json      # Main library data
│   ├── transactions.json # Borrow/return history
│   └── library_backup.json # Auto backup file

Getting Started

Install dependencies:

pip install rich


Run the program:

python main.py

Example Usage

Program menu:

Welcome to LibraNet
1. List all items
2. Borrow item
3. Return item
4. Search items
5. View transactions
6. Exit


Borrowing a book:

Successfully borrowed '1984'
Due on: 2025-09-26 10:00:00


Returning the same book late:

Returned '1984' late
Fine charged: ₹30.00

Design Choices and Code Explanation

Object-Oriented Design

A base abstract class LibraryItem defines common attributes and methods (title, author, availability, borrow, return).

Specialized classes (Book, Audiobook, EMagazine) extend the base class and implement their unique behaviors, such as get_page_count(), play(), and archive_issue().

This design makes the system extensible. Adding a new item type only requires creating a new subclass.

Data Management with JSON

Library items, fines, and transactions are stored in JSON files for persistence.

JSON was chosen for readability, portability, and universal support.

A backup file is always created to prevent data loss.

Validation ensures the system does not crash if the data is corrupted.

Separation of Concerns

library_manager.py contains the business rules for borrowing, returning, fines, and searching.

data_manager.py is responsible for loading and saving JSON data.

ui.py manages how the system displays information in the terminal.

receipt.py handles receipts and transaction logging.

This separation makes the system modular and easy to maintain.

Error Handling and Robustness

Borrowing an unavailable item, invalid IDs, and corrupted JSON files are all handled gracefully.

Fines are calculated using Python’s Decimal to avoid floating-point inaccuracies.

User Experience

The rich library was used to present tables, panels, and colored messages.

This improves readability and creates a professional, user-friendly interface.

Extensibility

Constants such as fine rates and grace periods are stored in constants.py.

This makes it simple to change system-wide policies without modifying the logic.

The design supports easy integration of new features such as PDFs, accounts, or even a web interface.

Future Enhancements

Export receipts to PDF.

Add user accounts with borrowing limits.

Web interface using Flask or Django.

Integration with external book APIs for metadata.

Author

LibraNet was developed as a demonstration of professional software design principles, object-oriented programming, and persistent data handling in Python.