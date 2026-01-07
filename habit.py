from datetime import datetime

class Habit:
    """
    Represents a habit that can be tracked over time.

    A Habit has:
    - a name (description of the habit),
    - a periodicity (daily, weekly, or monthly),
    - a creation timestamp,
    - a list of completion timestamps.

    This class also supports serialization to and from dictionaries
    for persistence (e.g., saving to JSON).
    """

    def __init__(self, name: str, periodicity: str):
        """
        Initialize a new Habit instance.

        Args:
            name (str): The name or description of the habit.
            periodicity (str): How often the habit should be completed.
                               Must be one of: 'daily', 'weekly', or 'monthly'.

        Raises:
            ValueError: If the periodicity is not one of the allowed values.
        """
        if periodicity not in {"daily", "weekly", "monthly"}:
            raise ValueError("Periodicity must be 'daily', 'weekly', or 'monthly'")

        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completions = []  # list of datetime objects

    def complete(self, timestamp: datetime = None):
        """
        Mark the habit as completed.

        If no timestamp is provided, the current time is used.

        Args:
            timestamp (datetime, optional): The time of completion.
                                            Defaults to datetime.now().
        """
        self.completions.append(timestamp or datetime.now())

    def to_dict(self):
        """
        Convert the Habit instance into a dictionary.

        This method serializes datetime objects into ISO 8601 strings
        so the habit can be easily stored (e.g., in JSON).

        Returns:
            dict: A dictionary representation of the habit.
        """
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [c.isoformat() for c in self.completions]
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Habit instance from a dictionary.

        This is the inverse of `to_dict()` and is used to reconstruct
        a Habit object from stored data.

        Args:
            data (dict): A dictionary containing habit data with keys:
                         'name', 'periodicity', 'created_at', 'completions'.

        Returns:
            Habit: A reconstructed Habit instance.
        """
        habit = Habit(data["name"], data["periodicity"])
        habit.created_at = datetime.fromisoformat(data["created_at"])
        habit.completions = [datetime.fromisoformat(c) for c in data["completions"]]
        return habit