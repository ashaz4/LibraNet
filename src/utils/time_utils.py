import re
from datetime import timedelta
from decimal import Decimal
class InvalidDurationError(ValueError):
    pass
def parse_duration_to_timedelta(duration_str: str):
    if duration_str is None:
        raise InvalidDurationError("Duration cannot be empty")
    s=str(duration_str).strip().lower()
    if re.fullmatch(r'\d+', s):
        days=int(s)
        return timedelta(days=days)
    m=re.fullmatch(r'(\d+)\s*(d|days?|w|weeks?|m|months?)', s)
    if not m:
        raise InvalidDurationError(f"Could not parse duration '{duration_str}'")
    num=int(m.group(1))
    unit=m.group(2)
    if unit.startswith('d'):
        return timedelta(days=num)
    if unit.startswith('w'):
        return timedelta(weeks=num)
    if unit.startswith('m'):
        return timedelta(days=num*30) 
    raise InvalidDurationError(f"Unknown time unit in '{duration_str}'")