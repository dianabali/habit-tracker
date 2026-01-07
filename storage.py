import json
from habit import Habit

# File used to persist habit data in JSON format
FILE = "habits.json"

def save_habits(habits):
    """
    Save a list of Habit objects to a JSON file.

    Each Habit is converted into a dictionary using its `to_dict()` method
    before being serialized to JSON.

    Args:
        habits (list[Habit]): A list of Habit instances to be saved.
    """
    with open(FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)

def load_habits():
    """
    Load habits from the JSON file and reconstruct Habit objects.

    This function:
    - Returns an empty list if the file does not exist.
    - Returns an empty list if the file exists but is empty.
    - Safely handles invalid or corrupted JSON.

    Returns:
        list[Habit]: A list of reconstructed Habit instances.
    """
    try:
        with open(FILE) as f:
            content = f.read().strip()
            # Handle empty file case
            if not content:
                return []
            # Deserialize JSON and convert dictionaries to Habit objects
            return [Habit.from_dict(h) for h in json.loads(content)]
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or contains invalid JSON,
        # return an empty habit list instead of crashing
        return []
