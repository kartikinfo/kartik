import streamlit as st
from datetime import date


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

st.title("Bank Account Eligibility Checker")

birth_date = st.date_input("Enter your birth date")

if st.button("Check Eligibility"):
    age = calculate_age(birth_date)
    
    if age >= 18:
        st.success(f"You are {age} years old and eligible to create a bank account.")
    else:
        st.error(f" you are {age} years old. You need to be at least 18 years old to create a bank account.")


