import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

FILE = "expenses.csv"

# Ensure CSV exists
if not os.path.exists(FILE):
    with open(FILE, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    date_str = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter amount: "))
        datetime.strptime(date_str, "%Y-%m-%d")  # validate date
    except:
        print("❌ Invalid date or amount!")
        return
    
    with open(FILE, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date_str, category, amount])
    print("✅ Expense added.")

def show_summary():
    df = pd.read_csv(FILE, parse_dates=["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    month = input("Enter month to summarize (YYYY-MM): ")
    try:
        month_period = pd.Period(month)
    except:
        print("❌ Invalid month format.")
        return

    month_df = df[df["Month"] == month_period]
    if month_df.empty:
        print("No data for that month.")
        return

    summary = month_df.groupby("Category")["Amount"].sum()
    print(f"\n📊 Expense Summary for {month}")
    print(summary)

    # Pie Chart
    summary.plot.pie(autopct='%1.1f%%', figsize=(6, 6), title=f"Expenses by Category - {month}")
    plt.ylabel("")
    plt.show()

    # Bar Chart
    summary.plot.bar(title=f"Expenses by Category - {month}", ylabel="Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. Show Monthly Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
