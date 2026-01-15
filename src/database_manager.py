import json
import os

class DatabaseManager:
    def __init__(self, db_path="data"):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)

    def save_phone(self, phone_data):
        """Save a single phone record to a JSON file."""
        if not phone_data or 'id' not in phone_data:
            print("Invalid phone data, cannot save.")
            return

        file_path = os.path.join(self.db_path, f"{phone_data['id']}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(phone_data, f, indent=2)
        print(f"Saved {phone_data['id']}")

    def save_all_phones(self, all_phones):
        """Save a monolithic JSON file containing all phones."""
        file_path = os.path.join(self.db_path, "all_phones.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(all_phones, f, indent=2)
        print(f"Saved all phones to {file_path}")

    def load_phone(self, phone_id):
        """Load a single phone record by ID."""
        file_path = os.path.join(self.db_path, f"{phone_id}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def load_all_phones(self):
        """Load all phones from the monolithic file."""
        file_path = os.path.join(self.db_path, "all_phones.json")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
