import json
from habit import Habit

FILE = "habits.json"

def save_habits(habits):
    with open(FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)

def load_habits():
    try:
        with open(FILE) as f:
            content = f.read().strip()
            if not content:
                return []
            return [Habit.from_dict(h) for h in json.loads(content)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
