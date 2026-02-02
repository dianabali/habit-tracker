from habit import Habit
from storage import load_habits, save_habits

class HabitTracker:
    """
    Manages a collection of habits and coordinates persistence.

    This class acts as the core application logic layer:
    - loading habits from storage,
    - adding and deleting habits,
    - marking habits as completed,
    - saving changes automatically.
    """
    def __init__(self, file_path="habits.json"):
        """
        Initialize the HabitTracker.

        Existing habits are loaded from persistent storage at startup.
        """
        self.file_path = file_path
        self.habits = load_habits(self.file_path)

    def _save(self):
        """
        Persist the current state of habits to storage.

        This is an internal helper method and should not be called
        directly from outside the class.
        """
        save_habits(self.habits, self.file_path)

    def add_habit(self, name, periodicity):
        """
        Create and add a new habit to the tracker.

        Args:
            name (str): The name or description of the habit.
            periodicity (str): The habit frequency ('daily', 'weekly', or 'monthly').
        """
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self._save()

    def delete_habit(self, name):
        """
        Delete a habit by its name.

        If multiple habits share the same name, all matching habits
        will be removed.

        Args:
            name (str): The name of the habit to delete.
        """
        self.habits = [h for h in self.habits if h.name != name]
        self._save()

    def complete_habit(self, name, timestamp=None):
        """
        Mark a habit as completed.

        Args:
            name (str): The name of the habit to complete.
            timestamp (datetime, optional): The completion time.
                                           Defaults to the current time.

        Raises:
            ValueError: If no habit with the given name is found.
        """
        for h in self.habits:
            if h.name == name:
                h.complete(timestamp)
                self._save()
                return
        raise ValueError("Habit not found")
