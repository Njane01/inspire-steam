import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

# ================= DATABASE SETUP =================

conn = sqlite3.connect("supermarket_pos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    stock INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total REAL,
    payment REAL,
    change REAL,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sale_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    price REAL
)
""")

conn.commit()

# ================= POS APP =================

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket POS System")
        self.cart = []

        # Product Section
        tk.Label(root, text="Product Name").grid(row=0, column=0)
        tk.Label(root, text="Quantity").grid(row=0, column=2)

        self.product_entry = tk.Entry(root)
        self.product_entry.grid(row=0, column=1)

        self.qty_entry = tk.Entry(root)
        self.qty_entry.grid(row=0, column=3)

        tk.Button(root, text="Add to Cart", command=self.add_to_cart).grid(row=0, column=4)

        # Cart List
        self.cart_list = tk.Listbox(root, width=70)
        self.cart_list.grid(row=1, column=0, columnspan=5)

        # Total
        self.total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 14))
        self.total_label.grid(row=2, column=0, columnspan=2)

        tk.Label(root, text="Payment").grid(row=3, column=0)
        self.payment_entry = tk.Entry(root)
        self.payment_entry.grid(row=3, column=1)

        tk.Button(root, text="Checkout", command=self.checkout).grid(row=3, column=2)

    # ================= ADD TO CART =================
    def add_to_cart(self):
        name = self.product_entry.get()
        qty = int(self.qty_entry.get())

        cursor.execute("SELECT price, stock FROM products WHERE name=?", (name,))
        product = cursor.fetchone()

        if product:
            price, stock = product

            if qty <= stock:
                total_price = price * qty
                self.cart.append((name, qty, price, total_price))
                self.update_cart()
            else:
                messagebox.showerror("Error", "Not enough stock!")
        else:
            messagebox.showerror("Error", "Product not found!")

    # ================= UPDATE CART =================
    def update_cart(self):
        self.cart_list.delete(0, tk.END)
        total = 0
