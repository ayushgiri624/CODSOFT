import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")

        self.contacts = {}

        # Labels and Entries
        tk.Label(root, text="Name").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Phone").pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        tk.Label(root, text="Email").pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(root, text="View Contact", command=self.view_contact).pack(pady=5)
        tk.Button(root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).pack(pady=5)

        # Display area
        self.display = tk.Text(root, height=10, width=50)
        self.display.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email}
            messagebox.showinfo("Success", "Contact added.")
            self.clear_entries()

    def view_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact = self.contacts[name]
            self.display.delete('1.0', tk.END)
            self.display.insert(tk.END, f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            self.contacts[name] = {'phone': phone, 'email': email}
            messagebox.showinfo("Success", "Contact updated.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted.")
            self.display.delete('1.0', tk.END)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
