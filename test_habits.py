# test_habits.py
import datetime
import tempfile
from tracker import HabitTracker
from analytics import longest_streak_for_habit, longest_streak_all
from fixtures import create_tracker_with_data
from database import save_habits

# ----------------------------
# Tests
# ----------------------------

def test_create_and_list_habits():
    tracker = create_tracker_with_data()
    tracker.add_habit("Meditation", "daily")
    names = [h.name for h in tracker.habits]
    assert "Meditation" in names
    assert "Brush Teeth" in names

def test_habits_by_periodicity():
    tracker = create_tracker_with_data()
    daily_habits = [h.name for h in tracker.habits if h.periodicity == "daily"]
    weekly_habits = [h.name for h in tracker.habits if h.periodicity == "weekly"]
    monthly_habits = [h.name for h in tracker.habits if h.periodicity == "monthly"]

    assert "Brush Teeth" in daily_habits
    assert "Call Parents" in weekly_habits
    assert "Pay Rent" in monthly_habits

def test_daily_longest_streak():
    tracker = create_tracker_with_data()
    habit = next(h for h in tracker.habits if h.name == "Brush Teeth")
    # Add 5 more consecutive completions
    now = datetime.datetime.now()
    for i in range(5):
        habit.complete(now + datetime.timedelta(days=i))
    assert longest_streak_for_habit("Brush Teeth") >= 10

def test_weekly_longest_streak():
    tracker = create_tracker_with_data()
    habit = next(h for h in tracker.habits if h.name == "Call Parents")
    # Add 2 more weekly completions
    now = datetime.datetime.now()
    for i in range(2):
        habit.complete(now + datetime.timedelta(days=i*7))
    assert longest_streak_for_habit("Call Parents") >= 4

def test_longest_streak_overall():
    tracker = create_tracker_with_data()
    # Ensure the daily habit has the longest streak
    assert longest_streak_all() >= 10
