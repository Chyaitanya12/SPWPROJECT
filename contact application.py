import tkinter as tk
from tkinter import messagebox

class ContactsApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Contacts Application")
        self.contacts = []

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill="x")
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(fill="x")
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill="x")

        tk.Label(self.frame1, text="Name:").pack(side="left")
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.pack(side="left")
        tk.Label(self.frame1, text="Phone:").pack(side="left")
        self.phone_entry = tk.Entry(self.frame1)
        self.phone_entry.pack(side="left")
        
        tk.Button(self.frame2, text="Add", command=self.add_contact).pack(side="left")
        tk.Button(self.frame2, text="Delete", command=self.delete_contact).pack(side="left")
        tk.Button(self.frame2, text="Update", command=self.update_contact).pack(side="left")
        tk.Button(self.frame2, text="Search", command=self.search_contact).pack(side="left")

        self.listbox = tk.Listbox(self.frame3)
        self.listbox.pack(fill="both", expand=True)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append((name, phone))
            self.contacts.sort()
            self.listbox.delete(0, tk.END)
            for contact in self.contacts:
                self.listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone number")

    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.listbox.delete(selected_index[0])
        else:
            messagebox.showerror("Error", "Please select a contact to delete")

    def update_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            if name and phone:
                self.contacts[selected_index[0]] = (name, phone)
                self.contacts.sort()
                self.listbox.delete(0, tk.END)
                for contact in self.contacts:
                    self.listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter both name and phone number")
        else:
            messagebox.showerror("Error", "Please select a contact to update")

    def search_contact(self):
        search_term = self.name_entry.get()
        if search_term:
            self.listbox.delete(0, tk.END)
            for contact in self.contacts:
                if search_term in contact[0]:
                    self.listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")
            self.name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a search term")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactsApplication(root)
    root.mainloop()