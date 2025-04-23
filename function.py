# trial.py
import pandas as pd
import os
import re
from datetime import datetime

FILE = "expenses.csv"

# Create file with headers if not exist
def init_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["date", "item", "amount"])
        df.to_csv(FILE, index=False)

def add_expense(user_input):
    init_file()
    match = re.match(r"(.+?)\s+(\d+(?:\.\d+)?)\$", user_input.strip())
    if not match:
        return False, "❌ Format error. Use: Item 5$"

    item = match.group(1).strip()
    amount = float(match.group(2))
    date_str = datetime.now().strftime("%Y-%m-%d")

    df = pd.read_csv(FILE)
    new_row = pd.DataFrame([[date_str, item, amount]], columns=["date", "item", "amount"])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE, index=False)

    return True, f"✅ Added: {item} {amount}$"

def get_monthly_summary():
    init_file()
    df = pd.read_csv(FILE)
    current_month = datetime.now().strftime("%Y-%m")
    monthly_df = df[df["date"].str.startswith(current_month)]
    total = monthly_df["amount"].sum()
    return monthly_df, total
