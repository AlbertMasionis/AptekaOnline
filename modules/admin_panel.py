import customtkinter as ctk
from tkinter import messagebox
from modules.buy_drugs import BuyDrugsWindow
from modules.customer_manager import register_client, delete_client
from modules.drug_manager import add_drug, remove_drug


class AdminPanel(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Panel Administratora")
        self.geometry("800x600")
        self.configure(fg_color="#1f2937")
        self.focus()
        self.grab_set()

        ctk.CTkLabel(
            self,
            text="Panel Administratora",
            font=("Arial", 32, "bold"),
            text_color="#329e76"
        ).pack(pady=20)

        self.tabs = ctk.CTkTabview(self, width=750, height=500)
        self.tabs.pack(pady=10)

        self.setup_drug_tab()
        self.setup_client_tab()

    def setup_drug_tab(self):
        tab = self.tabs.add("Zarządzaj lekami")

        # Dodawanie leku
        ctk.CTkLabel(tab, text="Dodaj lek", font=("Arial", 20, "bold"), text_color="white").pack(pady=10)
        self.drug_name = ctk.CTkEntry(tab, placeholder_text="Nazwa leku")
        self.drug_name.pack(pady=5)
        self.drug_price = ctk.CTkEntry(tab, placeholder_text="Cena")
        self.drug_price.pack(pady=5)
        self.drug_stock = ctk.CTkEntry(tab, placeholder_text="Stan magazynowy")  # <- poprawnie tu
        self.drug_stock.pack(pady=5)
        ctk.CTkButton(tab, text="Dodaj lek", command=self.add_drug_btn).pack(pady=10)

        # Usuwanie leku
        ctk.CTkLabel(tab, text="Usuń lek", font=("Arial", 20, "bold"), text_color="white").pack(pady=20)
        self.drug_identifier = ctk.CTkEntry(tab, placeholder_text="ID lub nazwa")
        self.drug_identifier.pack(pady=5)
        ctk.CTkButton(tab, text="Usuń lek", command=self.remove_drug_btn).pack(pady=10)

    def setup_client_tab(self):
        tab = self.tabs.add("Zarządzaj klientami")

        # Dodawanie klienta
        ctk.CTkLabel(tab, text="Dodaj klienta", font=("Arial", 20, "bold"), text_color="white").pack(pady=10)
        self.client_firstname = ctk.CTkEntry(tab, placeholder_text="Imię")
        self.client_firstname.pack(pady=5)
        self.client_lastname = ctk.CTkEntry(tab, placeholder_text="Nazwisko")
        self.client_lastname.pack(pady=5)
        ctk.CTkButton(tab, text="Dodaj klienta", command=self.add_client_btn).pack(pady=10)

        # Usuwanie klienta
        ctk.CTkLabel(tab, text="Usuń klienta", font=("Arial", 20, "bold"), text_color="white").pack(pady=20)
        self.client_identifier = ctk.CTkEntry(tab, placeholder_text="ID lub nazwisko")
        self.client_identifier.pack(pady=5)
        ctk.CTkButton(tab, text="Usuń klienta", command=self.remove_client_btn).pack(pady=10)

    def add_drug_btn(self):
        try:
            name = self.drug_name.get()
            price = float(self.drug_price.get())
            stock = int(self.drug_stock.get())
            add_drug(name, price, stock)
            messagebox.showinfo("Sukces", f"Dodano lek: {name}")
        except ValueError:
            messagebox.showerror("Błąd", "Cena i stan magazynowy muszą być liczbami.")

    def remove_drug_btn(self):
        try:
            identifier = self.drug_identifier.get()
            result = remove_drug(identifier)
            if result:
                messagebox.showinfo("Sukces", "Lek został usunięty.")
            else:
                messagebox.showerror("Błąd", "Nie znaleziono leku do usunięcia.")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def add_client_btn(self):
        try:
            firstname = self.client_firstname.get()
            lastname = self.client_lastname.get()
            register_client(firstname, lastname)
            messagebox.showinfo("Sukces", "Dodano klienta.")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def remove_client_btn(self):
        try:
            identifier = self.client_identifier.get()
            result = delete_client(identifier)
            if result:
                messagebox.showinfo("Sukces", "Klient usunięty.")
            else:
                messagebox.showerror("Błąd", "Nie znaleziono klienta.")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))
