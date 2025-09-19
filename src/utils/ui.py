from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from datetime import datetime
from decimal import Decimal
from ..utils.constants import LIBRARY_NAME
console=Console()
def table_for_items(items):
    t=Table(title=f"{LIBRARY_NAME}-Collection", box=box.ROUNDED, show_lines=False)
    t.add_column("ID", justify="right", style="cyan", no_wrap=True)
    t.add_column("Title", style="bold")
    t.add_column("Author")
    t.add_column("Type")
    t.add_column("Available", justify="center")
    t.add_column("Due Date", justify="center")
    for it in items:
        due_str=it.due_date.strftime("%Y-%m-%d") if getattr(it, "due_date", None) else "-"
        avail="[green]Yes[/green]" if it.available else "[red]No[/red]"
        t.add_row(str(it.item_id), it.title, it.author, it.__class__.__name__, avail, due_str)
    console.print(t)
def dashboard(items, fines: dict):
    total=len(items)
    borrowed=len([i for i in items if not i.available])
    available=total-borrowed
    total_fines=sum(Decimal(v) if isinstance(v, str) else v for v in fines.values()) if fines else Decimal("0.00")
    body=(
        f"Total items: [bold]{total}[/bold]\n"
        f"Borrowed: [bold red]{borrowed}[/bold red]\n"
        f"Available: [bold green]{available}[/bold green]\n"
        f"Total fines collected: [bold yellow]₹{total_fines}[/bold yellow]\n"
        f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    console.print(Panel(body, title="LibraNet Dashboard", subtitle=LIBRARY_NAME))