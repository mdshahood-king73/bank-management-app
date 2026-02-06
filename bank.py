import json
import random
import string
from pathlib import Path


class Bank:
    def __init__(self):
        self.db = Path("data.json")
        if not self.db.exists():
            self.db.write_text(json.dumps([]))

    def _load(self):
        return json.loads(self.db.read_text())

    def _save(self, data):
        self.db.write_text(json.dumps(data, indent=4))

    def _gen_account(self):
        return ''.join(random.choices(string.digits, k=8))

    # CREATE ACCOUNT
    def create_account(self, name, age, email, pin):
        if not name or not email or len(str(pin)) != 4:
            return None, "Invalid input"

        data = self._load()
        acc = self._gen_account()

        user = {
            "account": acc,
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "balance": 0
        }

        data.append(user)
        self._save(data)
        return user, "Account created successfully"

    # DEPOSIT
    def deposit(self, acc, pin, amount):
        data = self._load()
        for u in data:
            if u["account"] == acc and u["pin"] == pin:
                u["balance"] += amount
                self._save(data)
                return "Money deposited successfully"
        return "Invalid account or pin"

    # WITHDRAW
    def withdraw(self, acc, pin, amount):
        data = self._load()
        for u in data:
            if u["account"] == acc and u["pin"] == pin:
                if u["balance"] >= amount:
                    u["balance"] -= amount
                    self._save(data)
                    return "Withdrawal successful"
                return "Insufficient balance"
        return "Invalid account or pin"

    # SHOW DETAILS
    def show_details(self, acc, pin):
        for u in self._load():
            if u["account"] == acc and u["pin"] == pin:
                return u
        return None

    # UPDATE DETAILS
    def update_details(self, acc, pin, name=None, email=None, newpin=None):
        data = self._load()
        for u in data:
            if u["account"] == acc and u["pin"] == pin:
                if name:
                    u["name"] = name
                if email:
                    u["email"] = email
                if newpin:
                    u["pin"] = newpin
                self._save(data)
                return "Details updated successfully"
        return "Invalid credentials"

    # DELETE ACCOUNT
    def delete_account(self, acc, pin):
        data = self._load()
        new_data = [u for u in data if not (u["account"] == acc and u["pin"] == pin)]
        if len(new_data) == len(data):
            return "Invalid credentials"
        self._save(new_data)
        return "Account deleted successfully"

