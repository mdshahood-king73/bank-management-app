import json
from pathlib import Path

class Bank:
    database = "data.json"

    def __init__(self):
        if not Path(self.database).exists():
            with open(self.database, "w") as f:
                json.dump([], f)

        with open(self.database, "r") as f:
            self.data = json.load(f)

    def save(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4)

    def create_account(self, name, age, email, pin):
        acc = {
            "Name": name,
            "Age": age,
            "Email": email,
            "Pin": pin,
            "AccountNo": str(len(self.data) + 1001),
            "Balance": 0
        }
        self.data.append(acc)
        self.save()
        return acc

    def get_user(self, acc, pin):
        for u in self.data:
            if u["AccountNo"] == acc and u["Pin"] == pin:
                return u
        return None
