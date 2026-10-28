from datetime import date, timedelta

def calculate_streak(
    streak: int,
    last_completed: date | None,
    today: date
) -> int:
    if last_completed == today:
        return streak

    if last_completed == today - timedelta(days=1):
        return streak + 1

    return 1
