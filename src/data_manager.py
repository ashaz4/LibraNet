import json
from pathlib import Path
from decimal import Decimal
from datetime import datetime
from .utils.constants import LIBRARY_JSON, BACKUP_JSON
from .models.book import Book
from .models.audiobook import Audiobook
from .models.emagazine import EMagazine
from .utils.ui import console

def _ensure_data_dir():
    LIBRARY_JSON.parent.mkdir(parents=True, exist_ok=True)
def save_library(items: list, fines: dict):
    _ensure_data_dir()
    if LIBRARY_JSON.exists():
        try:
            LIBRARY_JSON.replace(BACKUP_JSON)
        except Exception:
            LIBRARY_JSON.parent.joinpath("library_backup.json").write_text(LIBRARY_JSON.read_text())
    data={
        "metadata": {
            "exported_at": datetime.now().isoformat()
        },
        "items": [ _serialize_item(i) for i in items ],
        "fines": { str(k): str(v) for k, v in (fines or {}).items() }
    }
    with open(LIBRARY_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
    console.print(f"Saved library to {LIBRARY_JSON}", style="green")
def _serialize_item(item):
    try:
        return item.to_dict()
    except Exception:
        base=item.to_dict_base()
        base.update({"extra": {}})
        return base
def load_library():
    _ensure_data_dir()
    if not LIBRARY_JSON.exists():
        console.print("No library data found — creating default seeded collection.", style="yellow")
        return _seed_default(), {}
    try:
        with open(LIBRARY_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        console.print("Failed to read library.json, starting fresh.", style="red")
        return _seed_default(), {}
    items=[]
    for it in data.get("items", []):
        t=it.get("type", "")
        if t=="Book":
            items.append(Book.from_dict(it))
        elif t=="Audiobook":
            items.append(Audiobook.from_dict(it))
        elif t=="EMagazine":
            items.append(EMagazine.from_dict(it))
        else:
            continue
    fines={ int(k): Decimal(v) for k, v in data.get("fines", {}).items() } if data.get("fines") else {}
    console.print(f"Loaded {len(items)} items and {len(fines)} fine records.", style="green")
    return items, fines
def _seed_default():
    seed=[
        Book(1, "1984", "George Orwell", 328),
        Book(2, "To Kill a Mockingbird", "Harper Lee", 281),
        Book(3, "Clean Code", "Robert C. Martin", 464),
        Book(4, "The Pragmatic Programmer", "Andrew Hunt & David Thomas", 352),
        Book(5, "Introduction to Algorithms", "Cormen et al.", 1312),
        Book(6, "Deep Learning", "Ian Goodfellow", 775),
        Audiobook(7, "Atomic Habits", "James Clear", 450),
        Audiobook(8, "The Power of Habit", "Charles Duhigg", 420),
        Audiobook(9, "Sapiens (Audio)", "Yuval Noah Harari", 660),
        Audiobook(10, "Rich Dad Poor Dad (Audio)", "Robert Kiyosaki", 300),
        EMagazine(11, "Tech Today", "Editorial Board", 42),
        EMagazine(12, "Nature Highlights", "Nature", 256),
        EMagazine(13, "AI Monthly", "AI Lab", 7),
        EMagazine(14, "Gadget Review", "Gadgets Inc.", 19),
        Book(15, "Effective Java", "Joshua Bloch", 412),
        Book(16, "Design Patterns", "Gamma et al.", 395),
        Book(17, "You Don't Know JS", "Kyle Simpson", 278),
        Audiobook(18, "Mindset", "Carol Dweck", 360),
        EMagazine(19, "Travel Weekly", "Travel Desk", 88),
        Book(20, "The Alchemist", "Paulo Coelho", 208),
    ]
    return seed