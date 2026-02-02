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
    print("\n📊=== Analytics Menu 📊===\n")

    print("1️⃣  List all habits")
    print("2️⃣  List habits by periodicity")
    print("3️⃣  Longest streak (overall)")
    print("4️⃣  Longest streak for a habit")
    print("5️⃣  Back to main menu")

    choice = input("👉 Your choice: ")


    # Add a new habit
    if choice == "1":
        name = input("Name: ")
        periodicity = input("Periodicity (daily/weekly/monthly): ")
        try:
            tracker.add_habit(name, periodicity)
        except ValueError as e:
            print("Error:", e)

    # Complete a habit
    elif choice == "2":
        name = input("Habit name: ")
        tracker.complete_habit(name)

    # List all habits
    elif choice == "3":
        for h in list_all_habits(tracker.file_path):
            print("-", h)

    # Analytics submenu
    elif choice == "4":
        while True:
            print("\n📊✨=== Analytics Menu ✨📊\n")

            print("1️⃣  List all habits 📝")
            print("2️⃣  List habits by periodicity 📅")
            print("3️⃣  Longest streak (overall) 🔥")
            print("4️⃣  Longest streak for a habit ⭐")
            print("5️⃣  Back 🔙")

            sub = input("👉 Your choice: ")


            if sub == "1":
                for h in list_all_habits(tracker.file_path):
                    print("-", h)

            elif sub == "2":
                period = input("Periodicity (daily/weekly/monthly): ")
                habits = habits_by_periodicity(period, tracker.file_path)
                if habits:
                    for h in habits:
                        print("-", h)
                else:
                    print("No habits found.")

            elif sub == "3":
                print("Longest streak overall:", longest_streak_all(tracker.file_path))

            elif sub == "4":
                name = input("Habit name: ")
                print(f"Longest streak for '{name}':", longest_streak_for_habit(name, tracker.file_path))
            elif sub == "5":
                break
            else:
                print("Invalid choice")

    # Exit the application
    elif choice == "5":
        break
    else:
        print("Invalid choice")
