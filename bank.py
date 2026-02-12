import streamlit as st
import Bank

bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account",
    ],
)

# CREATE
if menu == "Create Account":
    st.subheader("Create Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create"):
        ok, res = bank.create_account(name, age, email, int(pin))
        if ok:
            st.success("Account Created Successfully")
            st.json(res)
        else:
            st.error(res)

# DEPOSIT
elif menu == "Deposit Money":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        ok, res = bank.deposit(acc, int(pin), amount)
        st.success(f"New Balance: {res}") if ok else st.error(res)

# WITHDRAW
elif menu == "Withdraw Money":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        ok, res = bank.withdraw(acc, int(pin), amount)
        st.success(f"Remaining Balance: {res}") if ok else st.error(res)

# SHOW
elif menu == "Show Details":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        ok, res = bank.show_details(acc, int(pin))
        st.json(res) if ok else st.error(res)

# UPDATE
elif menu == "Update Details":
    acc = st.text_input("Account Number")
    pin = st.text_input("Old PIN", type="password")
    name = st.text_input("New Name")
    email = st.text_input("New Email")
    newpin = st.text_input("New PIN")

    if st.button("Update"):
        ok, res = bank.update_details(
            acc, int(pin), name, email, int(newpin) if newpin else None
        )
        st.success(res) if ok else st.error(res)

# DELETE
elif menu == "Delete Account":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        ok, res = bank.delete_account(acc, int(pin))
        st.success(res) if ok else st.error(res)
