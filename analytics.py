# analytics.py
from datetime import timedelta
from database import load_habits

def list_all_habits():
    return [h.name for h in load_habits()]

def habits_by_periodicity(periodicity):
    return [h.name for h in load_habits() if h.periodicity == periodicity]

def _delta(periodicity):
    return {
        "daily": timedelta(days=1),
        "weekly": timedelta(days=7),
        "monthly": timedelta(days=30)
    }[periodicity]

def longest_streak_for_habit(name):
    habits = load_habits()
    habit = next((h for h in habits if h.name == name), None)
    if not habit or not habit.completions:
        return 0

    completions = sorted(habit.completions)
    delta = _delta(habit.periodicity)

    streak = max_streak = 1
    for i in range(1, len(completions)):
        if completions[i] - completions[i-1] <= delta:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 1
    return max_streak

def longest_streak_all():
    habits = load_habits()
    if not habits:
        return 0
    return max(longest_streak_for_habit(h.name) for h in habits)
