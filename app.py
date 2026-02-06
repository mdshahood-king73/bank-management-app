import streamlit as st
from bank import Bank

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

if menu == "Create Account":
    st.subheader("Create Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit Pin", type="password")

    if st.button("Create"):
        acc = bank.create_account_streamlit(name, age, email, pin)
        if acc:
            st.success(f"Account created 🎉 Account No: {acc}")

elif menu == "Show Details":
    st.subheader("Show Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")

    if st.button("Show"):
        data = bank.get_details(acc, pin)
        if data:
            st.json(data)
        else:
            st.error("Invalid details")
