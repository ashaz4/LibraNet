from datetime import datetime
from decimal import Decimal
from .models.base_item import LibraryItem
from .utils.time_utils import parse_duration_to_timedelta, InvalidDurationError
from .data_manager import save_library, load_library
from .utils.receipt import print_receipt_console, save_transaction
from .utils.ui import table_for_items, dashboard, console
class LibraryManager:
    def __init__(self):
        items, fines=load_library()
        self.items=items
        self.fines=fines or {}
    def add_item(self, item: LibraryItem):
        if any(i.item_id==item.item_id for i in self.items):
            raise KeyError(f"Item id {item.item_id} already exists.")
        self.items.append(item)
        self._auto_save()
    def get_item(self, item_id: int):
        for it in self.items:
            if it.item_id==int(item_id):
                return it
        return None
    def borrow_item(self, item_id: int, duration_str: str, borrow_date: datetime=None):
        item=self.get_item(item_id)
        if not item:
            raise KeyError(f"No item with id {item_id}")
        if not item.available:
            raise Exception("Item not available for borrow.")
        try:
            delta=parse_duration_to_timedelta(duration_str)
        except InvalidDurationError as e:
            raise
        due_date = (borrow_date or datetime.now())+delta
        item.borrow(due_date, borrow_date)
        tx = {
            "type": "borrow",
            "item_id": item.item_id,
            "title": item.title,
            "date": (borrow_date or datetime.now()).isoformat(),
            "details": f"due_date: {due_date.isoformat()}",
            "fine": "0.00"
        }
        save_transaction(tx)
        self._auto_save()
        print_receipt_console(tx)
        return due_date
    def return_item(self, item_id: int, return_date: datetime = None):
        item=self.get_item(item_id)
        if not item:
            raise KeyError(f"No item with id {item_id}")
        if item.available:
            raise Exception("Item is not currently borrowed.")
        fine=item.return_item(return_date)
        if fine and fine>0:
            self.fines[item.item_id]=self.fines.get(item.item_id, Decimal("0.00"))+fine
        tx = {
            "type": "return",
            "item_id": item.item_id,
            "title": item.title,
            "date": (return_date or datetime.now()).isoformat(),
            "details": "",
            "fine": str(fine)
        }
        save_transaction(tx)
        print_receipt_console(tx)
        self._auto_save()
        return fine
    def search(self, keyword: str = None, item_type: str = None, available: bool | None = None):
        results=self.items
        if keyword:
            q=keyword.lower()
            results=[i for i in results if q in i.title.lower() or q in i.author.lower()]
        if item_type:
            results=[i for i in results if i.__class__.__name__.lower()==item_type.lower()]
        if available is not None:
            results=[i for i in results if i.available==available]
        return results
    def display_all(self):
        table_for_items(self.items)
    def show_dashboard(self):
        dashboard(self.items, self.fines)
    def _auto_save(self):
        save_library(self.items, self.fines)