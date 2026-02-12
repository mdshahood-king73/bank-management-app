import streamlit as st
from datetime import datetime
import uuid

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, age, email, pin):
        """Create a new bank account"""
        try:
            if not name or not email:
                return False, "Name and Email are required!"
            
            if pin < 1000 or pin > 9999:
                return False, "PIN must be 4 digits!"
            
            if age < 18:
                return False, "Age must be at least 18!"
            
            account_number = str(uuid.uuid4())[:8]
            
            self.accounts[account_number] = {
                "name": name,
                "age": age,
                "email": email,
                "pin": pin,
                "balance": 0,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return True, {
                "account_number": account_number,
                "message": "Account created successfully!"
            }
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def deposit(self, account_number, pin, amount):
        """Deposit money into account"""
        try:
            if account_number not in self.accounts:
                return False, "Account not found!"
            
            account = self.accounts[account_number]
            
            if account["pin"] != pin:
                return False, "Invalid PIN!"
            
            if amount <= 0:
                return False, "Amount must be greater than 0!"
            
            account["balance"] += amount
            return True, account["balance"]
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def withdraw(self, account_number, pin, amount):
        """Withdraw money from account"""
        try:
            if account_number not in self.accounts:
                return False, "Account not found!"
            
            account = self.accounts[account_number]
            
            if account["pin"] != pin:
                return False, "Invalid PIN!"
            
            if amount <= 0:
                return False, "Amount must be greater than 0!"
            
            if account["balance"] < amount:
                return False, "Insufficient balance!"
            
            account["balance"] -= amount
            return True, account["balance"]
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def show_details(self, account_number, pin):
        """Show account details"""
        try:
            if account_number not in self.accounts:
                return False, "Account not found!"
            
            account = self.accounts[account_number]
            
            if account["pin"] != pin:
                return False, "Invalid PIN!"
            
            return True, {
                "account_number": account_number,
                "name": account["name"],
                "age": account["age"],
                "email": account["email"],
                "balance": account["balance"],
                "created_at": account["created_at"]
            }
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def update_details(self, account_number, pin, name, email, new_pin):
        """Update account details"""
        try:
            if account_number not in self.accounts:
                return False, "Account not found!"
            
            account = self.accounts[account_number]
            
            if account["pin"] != pin:
                return False, "Invalid PIN!"
            
            if name:
                account["name"] = name
            
            if email:
                account["email"] = email
            
            if new_pin:
                if new_pin < 1000 or new_pin > 9999:
                    return False, "PIN must be 4 digits!"
                account["pin"] = new_pin
            
            return True, "Account updated successfully!"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def delete_account(self, account_number, pin):
        """Delete account"""
        try:
            if account_number not in self.accounts:
                return False, "Account not found!"
            
            account = self.accounts[account_number]
            
            if account["pin"] != pin:
                return False, "Invalid PIN!"
            
            del self.accounts[account_number]
            return True, "Account deleted successfully!"
        except Exception as e:
            return False, f"Error: {str(e)}"
