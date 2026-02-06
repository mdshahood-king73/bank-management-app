import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Bank App", layout="centered")
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Create Account", "Show Details"]
)

if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    email = st.text_input("Email")
    pin = st.text_input("4 digit PIN", type="password")

    if st.button("Create"):
        if len(pin) != 4:
            st.error("PIN must be 4 digits")
        else:
            acc = bank.create_account(name, age, email, int(pin))
            st.success("Account Created")
            st.write("Account Number:", acc["AccountNo"])

elif menu == "Show Details":
    st.subheader("Show Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = bank.get_user(acc, int(pin))
        if user:
            st.json(user)
        else:
            st.error("Invalid account or pin")
