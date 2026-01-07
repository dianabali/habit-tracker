from tracker import HabitTracker
from analytics import list_all_habits, habits_by_periodicity, longest_streak_all, longest_streak_for_habit

"""
Command-line interface (CLI) for the Habit Tracker application.

This module provides an interactive text-based menu that allows users to:
- add new habits,
- mark habits as completed,
- list existing habits,
- view analytics such as longest streaks.

The CLI acts as the presentation layer and communicates with the
HabitTracker (business logic) and analytics modules.
"""

# Initialize the habit tracker (loads existing habits from storage)
tracker = HabitTracker()

# Main application loop
while True:
    print("\n1. Add habit\n2. Complete habit\n3. List habits\n4. Analytics\n5. Exit")
    choice = input("> ")

    # Add a new habit
    if choice == "1":
        name = input("Name: ")
        periodicity = input("Periodicity (daily/weekly/monthly): ")
        tracker.add_habit(name, periodicity)

    # Complete a habit
    elif choice == "2":
        name = input("Habit name: ")
        tracker.complete_habit(name)

    # List all habits
    elif choice == "3":
        for h in list_all_habits():
            print("-", h)

    # Analytics submenu
    elif choice == "4":
        while True:
            print("\nAnalytics Menu\n1. List all habits\n2. List habits by periodicity\n3. Longest streak (overall)\n4. Longest streak for a habit\n5. Back")
            sub = input("> ")

            if sub == "1":
                for h in list_all_habits():
                    print("-", h)

            elif sub == "2":
                period = input("Periodicity (daily/weekly/monthly): ")
                habits = habits_by_periodicity(period)
                if habits:
                    for h in habits:
                        print("-", h)
                else:
                    print("No habits found.")

            elif sub == "3":
                print("Longest streak overall:", longest_streak_all())

            elif sub == "4":
                name = input("Habit name: ")
                print(f"Longest streak for '{name}':", longest_streak_for_habit(name))

            elif sub == "5":
                break
            else:
                print("Invalid choice")

    # Exit the application
    elif choice == "5":
        break
    else:
        print("Invalid choice")
