from datetime import datetime
import json
from decimal import Decimal
from .constants import TRANSACTIONS_JSON
from rich.console import Console
from rich.panel import Panel
console=Console()
def print_receipt_console(transaction: dict):
    lines=[]
    lines.append(f"[bold]Transaction:[/bold] {transaction.get('type')}")
    lines.append(f"[bold]Item ID:[/bold] {transaction.get('item_id')}")
    lines.append(f"[bold]Title:[/bold] {transaction.get('title')}")
    lines.append(f"[bold]Date:[/bold] {transaction.get('date')}")
    if transaction.get("details"):
        lines.append(f"[bold]Details:[/bold] {transaction.get('details')}")
    if transaction.get("fine") and str(transaction.get("fine")) != "0":
        lines.append(f"[bold red]Fine:[/bold red] ₹{transaction.get('fine')}")
    console.print(Panel("\n".join(lines), title="LibraNet Receipt", subtitle="Thank you"))
def save_transaction(transaction: dict):
    TRANSACTIONS_JSON.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(TRANSACTIONS_JSON, "r", encoding="utf-8") as f:
            data=json.load(f)
    except Exception:
        data=[]
    tx=dict(transaction)
    if isinstance(tx.get("fine"), Decimal):
        tx["fine"]=str(tx["fine"])
    data.append(tx)
    with open(TRANSACTIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)