import datetime
from pathlib import Path
import tempfile
from tracker import HabitTracker
from storage import save_habits

def insert_completions(habit, count):
    """
    Add a specified number of consecutive completions to a habit.

    Completion timestamps are generated based on the habit's periodicity
    to simulate a realistic completion streak.

    Args:
        habit (Habit): The habit to which completions will be added.
        count (int): The number of consecutive completions to insert.
    """
    now = datetime.datetime.now()
    step = {"daily": 1, "weekly": 7, "monthly": 30}[habit.periodicity]
    for i in range(count):
        habit.complete(now + datetime.timedelta(days=i * step))

def create_tracker_with_data():
    """
    Create a HabitTracker populated with sample habits and completions.

    This fixture is primarily intended for testing and demonstration.
    It initializes a tracker, inserts predefined habits with realistic
    completion streaks, and optionally persists the data to JSON.

    Returns:
        HabitTracker: A tracker instance preloaded with sample data.
    """
    temp_file = Path(tempfile.gettempdir()) / "habit_tests.json"
    tracker = HabitTracker(file_path=temp_file)
    tracker.habits = [] 

    # Sample habits: (name, periodicity, number of completions)
    habits_data = [
        ("Brush Teeth", "daily", 10),
        ("Workout", "daily", 8),
        ("Read Book", "daily", 7),
        ("Call Parents", "weekly", 4),
        ("Pay Rent", "monthly", 3),
        ("Clean House", "weekly", 5),
        ("Grocery Shopping", "monthly", 2),
        ("Journal", "daily", 6),
        ("Meditation", "daily", 9),
        ("Water Plants", "weekly", 4),
    ]

    for name, period, count in habits_data:
        tracker.add_habit(name, period)
        habit = next(h for h in tracker.habits if h.name == name)
        insert_completions(habit, count)

    return tracker
