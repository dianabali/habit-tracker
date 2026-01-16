import json
from pathlib import Path
from habit import Habit

# Default path to persist habit data in JSON format
DEFAULT_FILE = Path("habits.json")


def save_habits(habits, file_path=DEFAULT_FILE):
    """
    Save a list of Habit objects to a JSON file.

    Each Habit is converted into a dictionary using its `to_dict()` method
    before being serialized to JSON.

    Args:
        habits (list[Habit]): A list of Habit instances to be saved.
        file_path (Path or str, optional): Path to the JSON file.
                                           Defaults to 'habits.json'.
    """
    file_path = Path(file_path)
    with open(file_path, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)


def load_habits(file_path=DEFAULT_FILE):
    """
    Load habits from the JSON file and reconstruct Habit objects.

    Returns an empty list if the file does not exist or is invalid.

    Args:
        file_path (Path or str, optional): Path to the JSON file.
                                           Defaults to 'habits.json'.

    Returns:
        list[Habit]: A list of reconstructed Habit instances.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        return []

    try:
        content = file_path.read_text().strip()
        if not content:
            return []
        data = json.loads(content)
        return [Habit.from_dict(h) for h in data]
    except json.JSONDecodeError:
        # If the file contains invalid JSON, return empty list
        return []
