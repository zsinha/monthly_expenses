import streamlit as st
from function import add_expense, get_monthly_summary

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💸 Expense Tracker")

# Input form
with st.form("expense_form"):
    user_input = st.text_input("Enter an expense (e.g., Starbucks 5$)")
    submit = st.form_submit_button("Add Expense")

    if submit:
        success, message = add_expense(user_input)
        if success:
            st.success(message)
        else:
            st.error(message)

# Show summary
df, total = get_monthly_summary()
st.metric("📆 This Month's Total", f"{total:.2f}$")

with st.expander("📋 See All This Month's Expenses"):
    st.dataframe(df)
