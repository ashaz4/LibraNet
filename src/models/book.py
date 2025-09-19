from .base_item import LibraryItem
class Book(LibraryItem):
    def __init__(self, item_id: int, title: str, author: str, page_count: int):
        super().__init__(item_id, title, author)
        self.page_count=int(page_count)
    def getPageCount(self)->int:
        return self.page_count
    def get_details(self)->str:
        return f"Book: {self.title}—{self.page_count} pages"
    def to_dict(self)->dict:
        d=self.to_dict_base()
        d.update({"page_count": self.page_count})
        return d
    @classmethod
    def from_dict(cls, data: dict):
        b=cls(data["id"], data["title"], data["author"], data.get("page_count", 0))
        if data.get("borrow_date") and data.get("due_date"):
            from datetime import datetime
            b.borrow_date=datetime.fromisoformat(data["borrow_date"])
            b.due_date=datetime.fromisoformat(data["due_date"])
            b.available=data.get("available", False)
        return b