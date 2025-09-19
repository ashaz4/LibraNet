# LibraNet

LibraNet is a Python-based library management system that handles books, audiobooks, and e-magazines. 
It supports borrowing, returns, fine calculation, persistent storage in JSON, tabular displays, and receipt generation.

---

## Features

- **Core Library Functions**
  - Borrow and return items with due dates and fine calculation.  
  - Automatic fine handling based on overdue periods.  
  - Availability checks for each item.  

- **Specialized Item Behaviors**
  - Books include page counts.  
  - Audiobooks implement a playable interface.  
  - E-magazines allow issue archiving.  

- **Persistent Data Management**
  - All transactions stored in JSON (`library.json` and `transactions.json`).  
  - Automatic backup file generated (`library_backup.json`).  
  - Corrupted or missing data handled gracefully.  

- **User Experience Enhancements**
  - Rich tabular display of items with colorized terminal output.  
  - Search by item type, title, or author.  
  - Receipts generated for borrowing and returning.  

- **Statistics Dashboard**
  - Displays total items, borrowed vs available counts, and total fines collected.  

---

## Project Structure

```bash
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
```

---

## Design Choices

- **Object-Oriented Design**
  - Abstract base class `BaseItem` ensures all items share common properties and behavior.  
  - Each specialized item (`Book`, `Audiobook`, `EMagazine`) extends `BaseItem` while adding its unique functionality.  

- **Extensibility**
  - Adding a new item type only requires creating a new subclass and updating the manager minimally.  
  - The design supports future integrations like digital borrowing or external APIs.  

- **Data Persistence**
  - JSON chosen for simplicity, readability, and easy auditing.  
  - Transactions and library data are separated to ensure a clear history.  

- **User Interaction**
  - Rich library (`rich`) is used to provide colorized, modern console output.  
  - Receipts give a professional touch for tracking borrow/return actions.  

- **Error Handling**
  - Graceful recovery from missing or corrupted data files.  
  - Fines stored as `Decimal` for financial accuracy.  

---

## Getting Started

1. Clone or download the repository.  
2. Navigate to the project directory:  
   ```bash
   cd LibraNet
   ```  
3. Install dependencies:  
   ```bash
   pip install rich
   ```  
4. Run the program:  
   ```bash
   python main.py
   ```  

---

## Future Improvements

- Web or GUI version for broader usability.  
- User authentication and role-based access (admin vs member).  
- Integration with a payment gateway for fines.  
- Recommendation engine for books and audiobooks.  
