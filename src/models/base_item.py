from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal
from ..utils.constants import FINE_RATE, GRACE_PERIOD_DAYS
class LibraryItem(ABC):
    def __init__(self, item_id: int, title: str, author: str):
        self.item_id=int(item_id)
        self.title=title
        self.author=author
        self.available=True
        self.borrow_date=None 
        self.due_date=None
    @abstractmethod
    def get_details(self)->str:
        raise NotImplementedError
    def check_availability(self)->bool:
        return self.available
    def borrow(self, due_date: datetime, borrow_date: datetime = None):
        if not self.available:
            raise Exception(f"Item {self.item_id} '{self.title}' is already borrowed.")
        self.available=False
        self.borrow_date=borrow_date or datetime.now()
        self.due_date=due_date
        return self.due_date
    def calculate_fine(self, at_date: datetime | None=None)->Decimal:
        if self.available or self.due_date is None:
            return Decimal("0.00")
        at_date=at_date or datetime.now()
        if at_date<=self.due_date:
            return Decimal("0.00")
        days_late=(at_date.date() - self.due_date.date()).days
        late_chargeable_days=max(0, days_late-GRACE_PERIOD_DAYS)
        fine=(FINE_RATE * late_chargeable_days).quantize(Decimal("0.01"))
        return fine
    def return_item(self, return_date: datetime | None=None)->Decimal:
        if self.available:
            raise Exception(f"Item {self.item_id} '{self.title}' is not borrowed.")
        return_date=return_date or datetime.now()
        fine=self.calculate_fine(return_date)
        self.available=True
        self.borrow_date=None
        self.due_date=None
        return fine
    def to_dict_base(self)->dict:
        return {
            "id": self.item_id,
            "title": self.title,
            "author": self.author,
            "type": self.__class__.__name__,
            "available": self.available,
            "borrow_date": self.borrow_date.isoformat() if self.borrow_date else None,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }