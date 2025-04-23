import streamlit as st
from function import add_expense, get_monthly_summary, get_monthly_totals_by_currency

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💸 Expense Tracker")

# Select user
user = st.selectbox("👤 Select or enter your name:", options=["Papah", "Mamah", "Guest", "Other"])
if user == "Other":
    user = st.text_input("Enter your name:")
    
# Currency selector
currency = st.selectbox("💰 Choose currency:", options=["EUR", "IDR"])

# Input form
with st.form("expense_form"):
    user_input = st.text_input("Enter expense (e.g., Starbucks 5)")
    submit = st.form_submit_button("Add Expense")
    if submit:
        success, message = add_expense(user, currency, user_input)
        if success:
            st.success(message)
        else:
            st.error(message)

# Summary section
df, total = get_monthly_summary(user, currency)
st.metric("📆 This Month's Total", f"{total:.2f} {currency}")
with st.expander(f"📋 {user}'s Expenses This Month"):
    st.dataframe(df)

# Show totals for all currencies
st.subheader(f"🌐 {user}'s Total Expenses by Currency (This Month)")

summary_df = get_monthly_totals_by_currency(user)

if not summary_df.empty:
    # Format amount column with thousand separator (dot) and comma for decimals
    summary_df["amount"] = summary_df["amount"].apply(
        lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

    st.table(summary_df.rename(columns={"currency": "Currency", "amount": "Total"}))
else:
    st.info("No expenses yet this month.")


