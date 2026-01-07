# tracker.py
from datetime import datetime
from habit import Habit
from database import load_habits, save_habits

class HabitTracker:
    def __init__(self):
        self.habits = load_habits()

    def _save(self):
        save_habits(self.habits)

    def add_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self._save()

    def delete_habit(self, name):
        self.habits = [h for h in self.habits if h.name != name]
        self._save()

    def complete_habit(self, name, timestamp=None):
        for h in self.habits:
            if h.name == name:
                h.complete(timestamp)
                self._save()
                return
        raise ValueError("Habit not found")
