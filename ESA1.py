import tkinter as tk
from tkinter import messagebox

# Function to add expense
def add_expense():
    description = description_entry.get()
    amount = amount_entry.get()
    
    if not description or not amount:
        messagebox.showerror("Error", "Please enter both description and amount.")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return
    
    expenses.append((description, amount))
    update_expense_list()

# Function to split bills and display balances
def split_bills():
    total_expense = sum(amount for _, amount in expenses)
    individual_share = total_expense / len(users)
    user_balances = {user: individual_share for user in users}
    
    for expense in expenses:
        description, amount = expense
        for user in users:
            if user in description.lower():
                user_balances[user] -= amount / len(users)
    
    message = "Balances:\n"
    for user, balance in user_balances.items():
        message += f"{user}: ${balance:.2f}\n"
    
    messagebox.showinfo("Balances", message)

# Function to update the expense list
def update_expense_list():
    expense_list.delete(0, tk.END)
    for description, amount in expenses:
        expense_list.insert(tk.END, f"{description} : ${amount:.2f}")

# Function to handle changing the list of users
def change_users():
    global users
    user_input = users_entry.get()
    users = [user.strip() for user in user_input.split(",")]
    messagebox.showinfo("Success", "Users updated successfully.")
    update_expense_list()

# Initialize Tkinter
root = tk.Tk()
root.title("Expense Sharing App")

# List to store expenses
expenses = []

# List of users (default)
users = ["User 1", "User 2", "User 3"]

# Expense description entry
description_label = tk.Label(root, text="Description:")
description_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

description_entry = tk.Entry(root)
description_entry.grid(row=0, column=1, padx=10, pady=5)

# Expense amount entry
amount_label = tk.Label(root, text="Amount ($):")
amount_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

# Add Expense button
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)

# Split Bills button
split_button = tk.Button(root, text="Split Bills", command=split_bills)
split_button.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)

# Expense list
expense_list = tk.Listbox(root, width=50)
expense_list.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Change Users label and entry
users_label = tk.Label(root, text="Users (comma-separated):")
users_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

users_entry = tk.Entry(root)
users_entry.insert(0, ", ".join(users))
users_entry.grid(row=4, column=1, padx=10, pady=5)

# Change Users button
change_users_button = tk.Button(root, text="Change Users", command=change_users)
change_users_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)

# Run the Tkinter event loop
root.mainloop()
