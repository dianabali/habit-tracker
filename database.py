import json
from habit import Habit

# Path to the JSON file used for persistent storage
FILE = "habits.json"

def load_habits():
    """
    Load all habits from the JSON file.

    This function reads the stored habit data, deserializes the JSON content,
    and reconstructs Habit objects using `Habit.from_dict()`.

    If the file does not exist, is empty, or contains invalid JSON,
    an empty list is returned instead of raising an exception.

    Returns:
        list[Habit]: A list of loaded Habit instances.
    """
    try:
        with open(FILE) as f:
            content = f.read().strip()
            # Handle empty file case
            if not content:
                return []
            return [Habit.from_dict(h) for h in json.loads(content)]
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle missing or corrupted data file
        return []

def save_habits(habits):
    """
    Save all habits to the JSON file.

    Each Habit object is converted to a dictionary using its `to_dict()` method
    before being serialized to JSON.

    Args:
        habits (list[Habit]): A list of Habit instances to be saved.
    """
    with open(FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)
