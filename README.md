LibraNet
LibraNet is a Python-based library management system that handles books, audiobooks, and e-magazines. It supports borrowing, returns, fine calculation, persistent storage in JSON, tabular displays, and receipt generation.

Features
• Core Library Functions
o Borrow and return items with due dates and fine calculation.
o Automatic fine handling based on overdue periods.
o Availability checks for each item.
• Specialized Item Behaviors
o Books include page counts.
o Audiobooks implement a playable interface.
o E-magazines allow issue archiving.
• Persistent Data Management
o All transactions stored in JSON (library.json and transactions.json).
o Automatic backup file generated (library_backup.json).
o Corrupted or missing data handled gracefully.
• User Experience Enhancements
o Rich tabular display of items with colorized terminal output.
o Search by item type, title, or author.
o Receipts generated for borrowing and returning.
• Statistics Dashboard
o Displays total items, borrowed vs available counts, and total fines collected.

Project Structure
LibraNet/
│── main.py              # Entry point with menu system
│── data_manager.py      # JSON load, save, and backup
│── library_manager.py   # Business logic for borrow, return, search
│
├── models/
│   ├── base_item.py     # Abstract class for all items
│   ├── book.py          # Book implementation
│   ├── audiobook.py     # Audiobook implementation
│   └── emagazine.py     # E-magazine implementation
│
├── utils/
│   ├── ui.py            # Rich-based UI and tables
│   ├── receipt.py       # Receipt generation and storage
│   └── constants.py     # Configurations for fines, grace periods, colors
│
└── data/
    ├── library.json         # Main library data
    ├── transactions.json    # Borrow/return history
    └── library_backup.json  # Auto backup file

Design Choices
• Object-Oriented Design
o Abstract base class BaseItem ensures all items share common properties and behavior.
o Each specialized item (Book, Audiobook, EMagazine) extends BaseItem while adding its unique functionality.
• Extensibility
o Adding a new item type only requires creating a new subclass and updating the manager minimally.
o The design supports future integrations like digital borrowing or external APIs.
• Data Persistence
o JSON chosen for simplicity, readability, and easy auditing.
o Transactions and library data are separated to ensure a clear history.
• User Interaction
o Rich library (rich) is used to provide colorized, modern console output.
o Receipts give a professional touch for tracking borrow/return actions.
• Error Handling
o Graceful recovery from missing or corrupted data files.
o Fines stored as Decimal for financial accuracy.

Getting Started
1. Clone the repository or download it.
2. Navigate to the project directory:
3. cd LibraNet
4. Install dependencies:
5. pip install rich
6. Run the program:
7. python main.py

Future Improvements
• Web or GUI version for broader usability.
• User authentication and role-based access (admin vs member).
• Integration with a payment gateway for fines.
• Recommendation engine for books and audiobooks.

