import sys
from datetime import datetime
from decimal import Decimal
from src.library_manager import LibraryManager
from src.utils.ui import console
def main_menu():
    manager=LibraryManager()
    console.print("\nWelcome to [bold blue]LibraNet[/bold blue]\n", style="bold")
    while True:
        manager.show_dashboard()
        console.print("\nChoose an action:", style="bold")
        console.print("1) List items")
        console.print("2) Search items")
        console.print("3) Borrow item")
        console.print("4) Return item")
        console.print("5) Add item")
        console.print("6) View transactions file (open data/transactions.json manually)")
        console.print("7) Exit\n")
        choice=console.input("Enter choice > ").strip()
        try:
            if choice=="1":
                manager.display_all()
            elif choice=="2":
                q=console.input("Keyword (title/author) (leave blank to skip) > ")
                t=console.input("Type (Book/Audiobook/EMagazine) (leave blank to skip) > ")
                avail=console.input("Available? (y/n/blank) > ").strip().lower()
                av=None
                if avail=="y":
                    av=True
                elif avail=="n":
                    av=False
                res=manager.search(keyword=q or None, item_type=t or None, available=av)
                if not res:
                    console.print("No results found.", style="yellow")
                else:
                    manager.display_all() if (q=="" and t=="") else None
                    from src.utils.ui import table_for_items
                    table_for_items(res)
            elif choice=="3":
                iid=console.input("Item ID to borrow > ").strip()
                dur=console.input("Duration (ex:'7 days','2 weeks') > ").strip()
                due=manager.borrow_item(int(iid), dur)
                console.print(f"Borrowed. Due on: {due}", style="green")
            elif choice=="4":
                iid=console.input("Item ID to return > ").strip()
                fine=manager.return_item(int(iid))
                console.print(f"Returned. Fine charged: ₹{fine}", style="yellow")
            elif choice=="5":
                typ=console.input("Type (Book/Audiobook/EMagazine) > ").strip()
                iid=int(console.input("Item ID > ").strip())
                title=console.input("Title > ").strip()
                author=console.input("Author > ").strip()
                if typ.lower()=="book":
                    pages=int(console.input("Pages > ").strip())
                    from src.models.book import Book
                    manager.add_item(Book(iid, title, author, pages))
                elif typ.lower()=="audiobook":
                    dur=int(console.input("Duration (mins) > ").strip())
                    from src.models.audiobook import Audiobook
                    manager.add_item(Audiobook(iid, title, author, dur))
                elif typ.lower()=="emagazine":
                    issue=int(console.input("Issue # > ").strip())
                    from src.models.emagazine import EMagazine
                    manager.add_item(EMagazine(iid, title, author, issue))
                else:
                    console.print("Unknown type.", style="red")
                console.print("Added item and saved.", style="green")
            elif choice=="6":
                console.print("Open data/transactions.json to view full history. (Saved automatically.)", style="cyan")
            elif choice=="7":
                console.print("saving and exiting...... Thank you for visiting LibraNet!", style="green")
                sys.exit(0)
            else:
                console.print("Invalid choice.", style="red")
        except Exception as e:
            console.print(f"Error: {e}", style="bold red")
if __name__ == "__main__":
    main_menu()