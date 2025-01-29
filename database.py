import json

class Database:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file)
        print("Data saved successfully!")

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
