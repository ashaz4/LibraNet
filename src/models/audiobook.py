from .base_item import LibraryItem
class Audiobook(LibraryItem):
    def __init__(self, item_id: int, title: str, author: str, duration_minutes: int):
        super().__init__(item_id, title, author)
        self.duration=int(duration_minutes)
    def play(self)->str:
        return f"Playing '{self.title}' ({self.duration} mins)."
    def pause(self)->str:
        return f"Paused '{self.title}'."
    def get_details(self)->str:
        return f"Audiobook: {self.title}—{self.duration} mins"
    def to_dict(self)->dict:
        d=self.to_dict_base()
        d.update({"duration": self.duration})
        return d
    @classmethod
    def from_dict(cls,data:dict):
        a=cls(data["id"], data["title"], data["author"], data.get("duration", 0))
        if data.get("borrow_date") and data.get("due_date"):
            from datetime import datetime
            a.borrow_date=datetime.fromisoformat(data["borrow_date"])
            a.due_date=datetime.fromisoformat(data["due_date"])
            a.available=data.get("available", False)
        return a