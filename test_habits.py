import datetime
from analytics import longest_streak_for_habit, longest_streak_all
from fixtures import create_tracker_with_data

"""
Test suite for the Habit Tracker application.

These tests verify:
- habit creation and storage,
- filtering by periodicity,
- longest streak calculations for individual habits,
- longest streak calculation across all habits.

The tests rely on predefined fixtures to ensure consistent and
repeatable test data.
"""

# Tests
def test_create_and_list_habits():
    """
    Verify that habits can be created and are present in the tracker.
    """
    tracker = create_tracker_with_data()
    tracker.add_habit("Meditation", "daily")
    names = [h.name for h in tracker.habits]
    assert "Meditation" in names
    assert "Brush Teeth" in names

def test_habits_by_periodicity():
    """
    Verify that habits are correctly categorized by periodicity.
    """
    tracker = create_tracker_with_data()
    daily_habits = [h.name for h in tracker.habits if h.periodicity == "daily"]
    weekly_habits = [h.name for h in tracker.habits if h.periodicity == "weekly"]
    monthly_habits = [h.name for h in tracker.habits if h.periodicity == "monthly"]

    assert "Brush Teeth" in daily_habits
    assert "Call Parents" in weekly_habits
    assert "Pay Rent" in monthly_habits

def test_daily_longest_streak():
    """
    Verify the longest streak calculation for a daily habit.
    """
    tracker = create_tracker_with_data()
    habit = next(h for h in tracker.habits if h.name == "Brush Teeth")
    # Add 5 more consecutive completions
    now = datetime.datetime.now()
    for i in range(5):
        habit.complete(now + datetime.timedelta(days=i))
    assert longest_streak_for_habit("Brush Teeth") >= 10

def test_weekly_longest_streak():
    """
    Verify the longest streak calculation for a weekly habit.
    """
    tracker = create_tracker_with_data()
    habit = next(h for h in tracker.habits if h.name == "Call Parents")
    # Add 2 more weekly completions
    now = datetime.datetime.now()
    for i in range(2):
        habit.complete(now + datetime.timedelta(days=i*7))
    assert longest_streak_for_habit("Call Parents") >= 4

def test_longest_streak_overall():
    """
    Verify that the longest streak across all habits is correctly identified.
    """
    tracker = create_tracker_with_data()
    # Ensure the daily habit has the longest streak
    assert longest_streak_all() >= 10
