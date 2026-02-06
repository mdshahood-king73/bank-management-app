def __init__(self):
    self.data = []
    if not Path(self.database).exists():
        self._save()
    else:
        try:
            with open(self.database, "r", encoding="utf-8") as f:
                self.data = json.load(f) or []
        except (json.JSONDecodeError, ValueError):
            # If file is empty or corrupt, initialize fresh database
            self.data = []
            self._save()

def _save(self):
    with open(self.database, "w", encoding="utf-8") as f:
        json.dump(self.data, f, indent=4)

def _next_account_no(self):
    if not self.data:
        return 1001
    try:
        max_no = max(int(u.get("AccountNo", 0)) for u in self.data)
    except ValueError:
        max_no = 1000
    return max_no + 1

def create_account(self, name, age, email, pin):
    # basic validation
    if not name:
        raise ValueError("Name is required")
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer")
    if not pin or not str(pin).isdigit():
        raise ValueError("Pin must be numeric")

    # ensure email uniqueness (optional)
    if any(u.get("Email") == email for u in self.data):
        raise ValueError("An account with this email already exists")

    acc_no = str(self._next_account_no())
    acc = {
        "Name": name,
        "Age": age,
        "Email": email,
        "Pin": str(pin),           # consider hashing in real app
        "AccountNo": acc_no,
        "Balance": 0.0
    }
    self.data.append(acc)
    self._save()
    return acc.copy()  # return a copy to avoid accidental external mutation

def get_user(self, acc, pin=None):
    acc = str(acc)
    for u in self.data:
        if u.get("AccountNo") == acc and (pin is None or u.get("Pin") == str(pin)):
            return u.copy()
    return None

# example convenience methods
def deposit(self, acc, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    user = self.get_user(acc)
    if not user:
        raise ValueError("Account not found")
    # find and update the stored record
    for u in self.data:
        if u["AccountNo"] == str(acc):
            u["Balance"] = float(u.get("Balance", 0)) + amount
            self._save()
            return u.copy()

def withdraw(self, acc, amount, pin):
    if amount <= 0:
        raise ValueError("Withdraw amount must be positive")
    # authenticate
    for u in self.data:
        if u.get("AccountNo") == str(acc) and u.get("Pin") == str(pin):
            if float(u.get("Balance", 0)) < amount:
                raise ValueError("Insufficient funds")
            u["Balance"] = float(u.get("Balance", 0)) - amount
            self._save()
            return u.copy()
    raise ValueError("Account not found or invalid PIN")
