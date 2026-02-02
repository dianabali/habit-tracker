# Habit Tracker
A simple Python command-line based habit tracking application that allows users to create, track, and analyse habits.The project includes persistent storage, analytics for habit streaks, and a modular, maintainable code structure.

## Project Overview
Habit Tracker is designed to help users monitor daily, weekly, or monthly habits. Users can:
- Add new habits with a specified periodicity.
- Mark habits as completed.
- View a list of all habits or filter by periodicity.
- Analyse completion streaks for individual habits or across all habits.

The project demonstrates a modular Python design with:
- `Habit` class for individual habits
- `HabitTracker` for business logic
- `storage.py` for JSON persistence
- `analytics.py` for analytics such as streak calculation.
- `cli.py` for user interaction
- `pytest` for testing

## Features
- Habit creation - add habits with daily, weekly, or monthly periodicity.
- Completion logging - mark habits as completed with automatic timestamp.
- Analytics - longest streak per habit, longest streak across all habits, list habits filtered by periodicity.
- Persistent storage - habits and completions are saved to `habits.json`.

## Installation and run guide
### Prerequisites
- Python 3.10+
- Git (for cloning)
### Steps
1. Download the ZIP file from GitHub or clone the repository using this command: `git clone https://github.com/dianabali/habit-tracker.git`
2. Install Pytest for testing: `pip install pytest`
3. After installation, run `cli.py` directly or by running this command: `python cli.py`

Main menu options:
1. Add habit - create a new habit.
2. Complete habit - mark a habit as completed.
3. List habits - view all habits.
4. Analytics - submenu with list all habits, filter habits by periodicity, view longest streak (overall or per habit).
5. Exit - close the app.

Analytics submenu:
1. List all habits
2. List habits by periodicity
3. Longest streak (overall)
4. Longest streak for a habit
5. Back

## Tests
The Habit Tracker application includes a test suite to verify that all core features work correctly and consistently. These tests use predefined fixtures to simulate realistic user habits and completion data.
Test coverage:
1. Add Habit (`test_add_habit`):
   - ensures that a new habit can be added to the tracker.
   - verifies that the habit is correctly saved to and loaded from a JSON file.
2. Create and list habits (`test_create_and_list_habits`):
   - confirms that predefined habits and newly added habits are present in the tracker.
   - ensures the tracker properly maintains a list of habit names.
3. List habits by periodicity (`test_habits_by_periodicity`):
   - validates that habits are correctly categorized as daily, weekly, and monthly.
   - helps confirm that filtering by periodicity works as expected.
4. Longest streak for a daily habit (`test_daily_longest_streak`):
   - checks that the calculation of the longest consecutive completion streak for a daily habit is correct.
   - tests the streak logic by adding consecutive completions and verifying the maximum streak.
5. Longest streak for a weekly habit(`test_weekly_longest_streak`):
   - ensures the longest streak calculation works for weekly habits.
   - adds consecutive weekly completions to simulate realistic user behaviour.
6. Longest streak across all habits (`test_longest_streak_overall`):
   - verifies that the tracker correctly identifies the longest streak among all habits.
   - ensures that strak comparisons work across habits with different periodicities.
  

![Screenshot](images/test.png)

## Preview
![Screenshot](images/habit-tracker.png)
![Screenshot](images/analytics.png)














