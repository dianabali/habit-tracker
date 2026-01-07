# fixtures.py
import datetime
from tracker import HabitTracker
from database import save_habits
from habit import Habit

# ----------------------------
# Helper
# ----------------------------
def insert_completions(habit, count):
    """Add `count` consecutive completions to a habit."""
    now = datetime.datetime.now()
    step = {"daily": 1, "weekly": 7, "monthly": 30}[habit.periodicity]
    for i in range(count):
        habit.complete(now + datetime.timedelta(days=i * step))

# ----------------------------
# Fixture
# ----------------------------
def create_tracker_with_data():
    """
    Creates a HabitTracker with sample habits and completions.
    All data is in-memory; safe for Windows.
    """
    tracker = HabitTracker()
    # Sample habits with periodicity
    habits_data = [
        ("Brush Teeth", "daily", 10),
        ("Workout", "daily", 8),
        ("Read Book", "daily", 7),
        ("Call Parents", "weekly", 4),
        ("Pay Rent", "monthly", 3),
    ]

    for name, period, count in habits_data:
        tracker.add_habit(name, period)
        habit = next(h for h in tracker.habits if h.name == name)
        insert_completions(habit, count)

    # Save to JSON (optional for tests)
    save_habits(tracker.habits)
    return tracker
