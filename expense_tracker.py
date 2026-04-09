import csv
import matplotlib.pyplot as plt
import os
from datetime import datetime

FILE_NAME = "expense.csv"


def add_expense():
    date_input = input("Enter date (DD-MM-YYYY): ")

    try:
        date = datetime.strptime(date_input, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format!")
        return

    category = input("Enter category (Food, Travel, Bills, Others): ").strip()

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount!")
        return

    description = input("Enter description: ")

    data = {
        "date": date.strftime("%d-%m-%Y"),
        "category": category,
        "amount": amount,
        "description": description
    }

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    print("Expense added successfully!")



def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def monthly_summary():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    month_year = input("Enter month and year (MM-YYYY): ")

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['date'][3:] == month_year:
                total += float(row['amount'])

    print(f"Total expense for {month_year}: ₹{total:.2f}")



def category_analysis():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cat = row['category']
            amt = float(row['amount'])
            categories[cat] = categories.get(cat, 0) + amt

    if not categories:
        print("No data available.")
        return

    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt:.2f}")

    max_cat = max(categories, key=categories.get)
    print(f"\nHighest spending category: {max_cat} (₹{categories[max_cat]:.2f})")



def plot_expenses():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cat = row['category']
            amt = float(row['amount'])
            categories[cat] = categories.get(cat, 0) + amt

    if not categories:
        print("No data to plot.")
        return

    plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()



def insights():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    total = 0
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amt = float(row['amount'])
            total += amt
            categories[row['category']] = categories.get(row['category'], 0) + amt

    if not categories:
        print("No data available.")
        return

    max_cat = max(categories, key=categories.get)

    print(f"\nTotal Spending: ₹{total:.2f}")
    print(f"Highest Spending Category: {max_cat}")
    print("Suggestion: Try reducing expenses in this category to save money.")



def delete_last_entry():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    with open(FILE_NAME, "r") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        print("No entries to delete.")
        return

    rows = rows[:-1]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Last entry deleted successfully!")



def main():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Analysis")
        print("5. Show Pie Chart")
        print("6. Get Insights")
        print("7. Delete Last Entry")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            plot_expenses()
        elif choice == "6":
            insights()
        elif choice == "7":
            delete_last_entry()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()