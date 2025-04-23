import streamlit as st
from trial import add_expense, get_monthly_summary

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💸 Expense Tracker")

# Select user
user = st.selectbox("👤 Select or enter your name:", options=["Ali", "Sarah", "Guest", "Other"])
if user == "Other":
    user = st.text_input("Enter your name:")

# Currency selector
currency = st.selectbox("💰 Choose currency:", options=["USD", "EUR", "IDR", "JPY"])

# Input form
with st.form("expense_form"):
    user_input = st.text_input("Enter expense (e.g., Starbucks 5$)")
    submit = st.form_submit_button("Add Expense")

    if submit:
        success, message = add_expense(user, currency, user_input)
        if success:
            st.success(message)
        else:
            st.error(message)

# Summary section
df, total = get_monthly_summary(user)
st.metric("📆 This Month's Total", f"{total:.2f} {currency}")

with st.expander(f"📋 {user}'s Expenses
