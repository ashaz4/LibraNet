from decimal import Decimal
from pathlib import Path
FINE_RATE=Decimal("10.00")           
GRACE_PERIOD_DAYS=2               
DATA_DIR=Path.cwd()/"data"
LIBRARY_JSON=DATA_DIR/"library.json"
TRANSACTIONS_JSON=DATA_DIR/"transactions.json"
BACKUP_JSON=DATA_DIR/"library_backup.json"
LIBRARY_NAME = "LibraNet"
