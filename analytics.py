from datetime import timedelta
from storage import load_habits

def list_all_habits(file_path=None):
    """
    Retrieve the names of all tracked habits.

    Returns:
        list[str]: A list containing the names of all habits.
    """
    return [h.name for h in load_habits(file_path)]

def habits_by_periodicity(periodicity, file_path=None):
    """
    Retrieve habit names filtered by periodicity.

    Args:
        periodicity (str): The desired habit frequency
                           ('daily', 'weekly', or 'monthly').

    Returns:
        list[str]: A list of habit names matching the given periodicity.
    """
    return [h.name for h in load_habits(file_path) if h.periodicity == periodicity]

def _delta(periodicity):
    """
    Return the allowed time gap between completions for a given periodicity.

    This helper function defines how much time may pass between
    consecutive completions before a streak is considered broken.

    Args:
        periodicity (str): Habit frequency ('daily', 'weekly', or 'monthly').

    Returns:
        timedelta: The maximum allowed time difference between completions.
    """
    return {
        "daily": timedelta(days=1),
        "weekly": timedelta(days=7),
        "monthly": timedelta(days=30)
    }[periodicity]

def longest_streak_for_habit(name, file_path=None):
    """
    Calculate the longest completion streak for a specific habit.

    A streak is defined as consecutive completions where the time difference
    between each completion does not exceed the habit's periodicity window.

    Args:
        name (str): The name of the habit.

    Returns:
        int: The longest streak length for the habit.
             Returns 0 if the habit does not exist or has no completions.
    """
    habits = load_habits(file_path)
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

def longest_streak_all(file_path=None):
    """
    Calculate the longest streak across all tracked habits.

    Returns:
        int: The highest streak value among all habits.
             Returns 0 if no habits exist.
    """
    habits = load_habits(file_path)
    if not habits:
        return 0
    return max(longest_streak_for_habit(h.name, file_path) for h in habits)
