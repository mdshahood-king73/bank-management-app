import streamlit as st
from Bank import Bank

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
        "Delete Account"
    ]
)

# CREATE
if menu == "Create Account":
    st.subheader("Create Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit Pin", type="password")

    if st.button("Create"):
        user, msg = bank.create_account(name, age, email, int(pin))
        if user:
            st.success(msg)
            st.json(user)
        else:
            st.error(msg)

# DEPOSIT
elif menu == "Deposit Money":
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Deposit"):
        st.success(bank.deposit(acc, int(pin), amount))

# WITHDRAW
elif menu == "Withdraw Money":
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):
        st.success(bank.withdraw(acc, int(pin), amount))

# SHOW
elif menu == "Show Details":
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")

    if st.button("Show"):
        user = bank.show_details(acc, int(pin))
        if user:
            st.json(user)
        else:
            st.error("Invalid credentials")

# UPDATE
elif menu == "Update Details":
    acc = st.text_input("Account Number")
    pin = st.text_input("Current Pin", type="password")
    name = st.text_input("New Name")
    email = st.text_input("New Email")
    newpin = st.text_input("New Pin", type="password")

    if st.button("Update"):
        st.success(
            bank.update_details(
                acc,
                int(pin),
                name or None,
                email or None,
                int(newpin) if newpin else None
            )
        )

# DELETE
elif menu == "Delete Account":
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")

    if st.button("Delete"):
        st.warning(bank.delete_account(acc, int(pin)))

