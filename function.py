FILE = "expenses.csv"

def init_file():
    if not os.path.exists(FILE) or os.path.getsize(FILE) == 0:
        df = pd.DataFrame(columns=["date", "user", "item", "amount", "currency"])
        df.to_csv(FILE, index=False)

def add_expense(user, currency, user_input):
    init_file()
    match = re.match(r"(.+?)\s+(\d+(?:\.\d+)?)\$", user_input.strip())
    if not match:
        return False, "❌ Format error. Use: Item 5$"

    item = match.group(1).strip()
    amount = float(match.group(2))
    date_str = datetime.now().strftime("%Y-%m-%d")

    df = pd.read_csv(FILE)
    new_row = pd.DataFrame([[date_str, user, item, amount, currency]],
                           columns=["date", "user", "item", "amount", "currency"])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE, index=False)

    return True, f"✅ Added: {item} {amount} {currency} (by {user})"

def get_monthly_summary(user):
    init_file()
    df = pd.read_csv(FILE)
    current_month = datetime.now().strftime("%Y-%m")
    monthly_df = df[df["date"].str.startswith(current_month)]
    user_df = monthly_df[monthly_df["user"] == user]
    total = user_df["amount"].sum()
    return
