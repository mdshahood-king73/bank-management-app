import streamlit as st
st.write("✅ App started successfully")

import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Bank App", layout="centered")
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox("Menu", ["Create Account", "Show Details"])

if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    email = st.text_input("Email")
    pin = st.text_input("4 digit PIN", type="password", key="create_pin")

    if st.button("Create"):
        if not name or not email:
            st.error("Please enter name and email")
        elif not pin or not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 numeric digits")
        else:
            acc = bank.create_account(name, age, email, int(pin))
            st.success("Account Created")
            st.write("Account Number:", acc["AccountNo"])

elif menu == "Show Details":
    st.subheader("Show Account Details")

    acc = st.text_input("Account Number", key="show_acc")
    pin = st.text_input("PIN", type="password", key="show_pin")

    if st.button("Show"):
        if not acc or not pin:
            st.error("Please enter account number and PIN")
        elif not pin.isdigit():
            st.error("PIN must be numeric")
        else:
            try:
                user = bank.get_user(acc, int(pin))
            except Exception as e:
                st.error(f"Error: {e}")
            else:
                if user:
                    st.json(user)
                else:
                    st.error("Invalid account or pin")
