import tkinter as tk
from tkinter import ttk, messagebox
from medicines import add_medicine, get_all_medicines, delete_medicine
from customers import add_customer, get_all_customers, delete_customer
from sales import add_sale, get_all_sales, delete_sale

class PharmacyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1560x865")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        self.create_medicine_tab()
        self.create_customer_tab()
        self.create_sales_tab()
        
    def create_medicine_tab(self):
        self.medicine_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.medicine_tab, text='Medicines')

        ttk.Label(self.medicine_tab, text="Medicine Name:",foreground="blue").grid(row=0, column=0, padx=10, pady=10)
        self.medicine_name_entry = ttk.Entry(self.medicine_tab,width=50)
        self.medicine_name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        ttk.Label(self.medicine_tab, text="Generic Name:",foreground="blue").grid(row=1, column=0, padx=10, pady=10)
        self.generic_name = ttk.Entry(self.medicine_tab,width=50)
        self.generic_name.grid(row=1, column=1, padx=10, pady=10)
        
        ttk.Label(self.medicine_tab, text="Company Name:",foreground="blue").grid(row=2, column=0, padx=10, pady=10)
        self.com_name = ttk.Entry(self.medicine_tab,width=50)
        self.com_name.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.medicine_tab, text="Price:",foreground="blue").grid(row=4, column=0, padx=10, pady=10)
        self.price_entry = ttk.Entry(self.medicine_tab,width=50)
        self.price_entry.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(self.medicine_tab, text="Quantity:",foreground="blue").grid(row=3, column=0, padx=10, pady=10)
        self.quantity_entry = ttk.Entry(self.medicine_tab,width=50)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(self.medicine_tab, text="Expiry Date:",foreground="blue").grid(row=5, column=0, padx=10, pady=10)
        self.expiry_date_entry = ttk.Entry(self.medicine_tab,width=50)
        self.expiry_date_entry.grid(row=5, column=1, padx=10, pady=10)

        self.add_medicine_button = ttk.Button(self.medicine_tab, text="Add Medicine", command=self.add_medicine)
        self.add_medicine_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.delete_medicine_button = ttk.Button(self.medicine_tab, text="Delete Medicine", command=self.delete_medicine)
        self.delete_medicine_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.load_medicines()

    def create_customer_tab(self):
        self.customer_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.customer_tab, text='Customers')

        ttk.Label(self.customer_tab, text="Customer Name:").grid(row=0, column=0, padx=10, pady=10)
        self.customer_name_entry = ttk.Entry(self.customer_tab)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.customer_tab, text="Contact:").grid(row=1, column=0, padx=10, pady=10)
        self.contact_entry = ttk.Entry(self.customer_tab)
        self.contact_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_customer_button = ttk.Button(self.customer_tab, text="Add Customer", command=self.add_customer)
        self.add_customer_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.delete_customer_button = ttk.Button(self.customer_tab, text="Delete Customer", command=self.delete_customer)
        self.delete_customer_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.load_customers()

    def create_sales_tab(self):
        self.sales_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.sales_tab, text='Sales')

        ttk.Label(self.sales_tab, text="Medicine Name:").grid(row=0, column=0, padx=10, pady=10)
        self.medicine_id_entry = ttk.Entry(self.sales_tab)
        self.medicine_id_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.sales_tab, text="Customer ID:").grid(row=1, column=0, padx=10, pady=10)
        self.customer_id_entry = ttk.Entry(self.sales_tab)
        self.customer_id_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.sales_tab, text="Quantity:").grid(row=2, column=0, padx=10, pady=10)
        self.sales_quantity_entry = ttk.Entry(self.sales_tab)
        self.sales_quantity_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_sales_button = ttk.Button(self.sales_tab, text="Add Sale", command=self.add_sale)
        self.add_sales_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.delete_sales_button = ttk.Button(self.sales_tab, text="Delete Sale", command=self.delete_sale)
        self.delete_sales_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.load_sales()

    def add_medicine(self):
        name = self.medicine_name_entry.get()
        generic = self.generic_name.get()
        company = self.com_name.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        expiry_date = self.expiry_date_entry.get()
        add_medicine(name, generic, company, price, quantity, expiry_date)
        messagebox.showinfo("Success", "Medicine added successfully")
        self.load_medicines()

    def delete_medicine(self):
        selected_item = self.medicine_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a medicine to delete")
            return
        item = self.medicine_tree.item(selected_item)
        medicine_id = item['values'][0]
        delete_medicine(medicine_id)
        messagebox.showinfo("Success", "Medicine deleted successfully")
        self.load_medicines()

    def add_customer(self):
        name = self.customer_name_entry.get()
        contact = self.contact_entry.get()
        add_customer(name, contact)
        messagebox.showinfo("Success", "Customer added successfully")
        self.load_customers()

    def delete_customer(self):
        selected_item = self.customer_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a customer to delete")
            return
        item = self.customer_tree.item(selected_item)
        customer_id = item['values'][0]
        delete_customer(customer_id)
        messagebox.showinfo("Success", "Customer deleted successfully")
        self.load_customers()

    def add_sale(self):
        medicine_id = self.medicine_id_entry.get()
        customer_id = self.customer_id_entry.get()
        quantity = self.sales_quantity_entry.get()
        add_sale(medicine_id, customer_id, quantity)
        messagebox.showinfo("Success", "Sale added successfully")
        self.load_sales()

    def delete_sale(self):
        selected_item = self.sales_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a sale to delete")
            return
        item = self.sales_tree.item(selected_item)
        sale_id = item['values'][0]
        delete_sale(sale_id)
        messagebox.showinfo("Success", "Sale deleted successfully")
        self.load_sales()

    def load_medicines(self):
        for widget in self.medicine_tab.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        columns = ("ID", "Name", "Generic Name", "Company Name", "Price", "Quantity", "Expiry Date")
        self.medicine_tree = ttk.Treeview(self.medicine_tab, columns=columns, show='headings')
        for col in columns:
            self.medicine_tree.heading(col, text=col)
        self.medicine_tree.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        rows = get_all_medicines()
        for row in rows:
            self.medicine_tree.insert('', 'end', values=row)

    def load_customers(self):
        for widget in self.customer_tab.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        columns = ("ID", "Name", "Contact")
        self.customer_tree = ttk.Treeview(self.customer_tab, columns=columns, show='headings')
        for col in columns:
            self.customer_tree.heading(col, text=col)
        self.customer_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        rows = get_all_customers()
        for row in rows:
            self.customer_tree.insert('', 'end', values=row)

    def load_sales(self):
        for widget in self.sales_tab.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        columns = ("ID", "Medicine Name", "Customer ID", "Quantity", "Date")
        self.sales_tree = ttk.Treeview(self.sales_tab, columns=columns, show='headings')
        for col in columns:
            self.sales_tree.heading(col, text=col)
        self.sales_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        rows = get_all_sales()
        for row in rows:
            self.sales_tree.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyApp(root)
    root.mainloop()
