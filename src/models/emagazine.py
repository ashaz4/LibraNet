from .base_item import LibraryItem
class EMagazine(LibraryItem):
    def __init__(self, item_id: int, title: str, author: str, issue_number: int):
        super().__init__(item_id, title, author)
        self.issue_number=int(issue_number)
    def archiveIssue(self)->str:
        return f"Issue #{self.issue_number} of '{self.title}' archived."
    def get_details(self)->str:
        return f"E-Magazine: {self.title} — Issue #{self.issue_number}"
    def to_dict(self) -> dict:
        d=self.to_dict_base()
        d.update({"issue_number": self.issue_number})
        return d
    @classmethod
    def from_dict(cls, data: dict):
        e = cls(data["id"], data["title"], data["author"], data.get("issue_number", 0))
        if data.get("borrow_date") and data.get("due_date"):
            from datetime import datetime
            e.borrow_date=datetime.fromisoformat(data["borrow_date"])
            e.due_date=datetime.fromisoformat(data["due_date"])
            e.available=data.get("available", False)
        return e