from datetime import date, timedelta

from backend.utils.streaks import calculate_streak


def test_first_completion():
    today = date(2026, 10, 27)

    assert calculate_streak(0, None, today) == 1


def test_already_completed_today():
    today = date(2026, 10, 27)

    assert calculate_streak(3, today, today) == 3


def test_consecutive_day():
    today = date(2026, 10, 27)
    yesterday = today - timedelta(days=1)

    assert calculate_streak(3, yesterday, today) == 4


def test_missed_day_resets_streak():
    today = date(2026, 10, 27)
    two_days_ago = today - timedelta(days=2)

    assert calculate_streak(4, two_days_ago, today) == 1