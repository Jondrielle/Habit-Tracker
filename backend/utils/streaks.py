from datetime import date, timedelta
from typing import Optional

def calculate_streak(
    streak: int,
    last_completed: Optional[date],
    today: date
) -> int:
    if last_completed == today:
        return streak

    if last_completed == today - timedelta(days=1):
        return streak + 1

    return 1
