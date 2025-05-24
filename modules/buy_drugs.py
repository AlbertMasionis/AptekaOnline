import customtkinter as ctk
import pandas as pd
import tkinter.messagebox as msg
from modules.session import logged_user


class BuyDrugsWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Kup leki")
        self.geometry("600x500")
        self.configure(fg_color="#1f2937")
        self.focus()
        self.grab_set()

        if not logged_user:
            msg.showwarning("Brak dostępu", "Musisz być zalogowany, aby kupić leki.")
            self.destroy()
            return

        self.drugs_df = pd.read_excel("database/drugs.xlsx")
        self.selected_drug = ctk.StringVar()
        self.quantity = ctk.IntVar(value=1)

        ctk.CTkLabel(
            self, text="Wybierz lek", font=("Arial", 28, "bold"), text_color="#329e76"
        ).pack(pady=(20, 10))

        drug_names = self.drugs_df["nazwa"].tolist()
        self.dropdown = ctk.CTkOptionMenu(
            self, values=drug_names, variable=self.selected_drug
        )
        self.dropdown.pack(pady=10)

        ctk.CTkLabel(
            self, text="Ilość", font=("Arial", 20, "bold"), text_color="white"
        ).pack(pady=(20, 5))

        self.qty_entry = ctk.CTkEntry(
            self, textvariable=self.quantity, width=100, font=("Arial", 20)
        )
        self.qty_entry.pack()

        ctk.CTkButton(
            self,
            text="Kup",
            command=self.kup_lek,
            fg_color="#329e76",
            hover_color="#32959e",
            text_color="#1f2937",
            font=("Arial", 20, "bold"),
            height=50,
            corner_radius=20,
            width=200,
        ).pack(pady=30)

    def kup_lek(self):
        nazwa = self.selected_drug.get()
        ilosc = self.quantity.get()

        if ilosc <= 0:
            msg.showerror("Błąd", "Podaj poprawną ilość.")
            return

        index = self.drugs_df[self.drugs_df["nazwa"] == nazwa].index

        if index.empty:
            msg.showerror("Błąd", "Lek nie istnieje.")
            return

        index = index[0]
        stan = self.drugs_df.at[index, "stan_magazynowy"]

        if ilosc > stan:
            msg.showerror("Błąd", "Brak wystarczającej ilości w magazynie.")
            return

        # Aktualizacja magazynu
        self.drugs_df.at[index, "stan_magazynowy"] = stan - ilosc
        self.drugs_df.to_excel("database/drugs.xlsx", index=False)

        # Zapis zakupu do historii użytkownika
        self.zapisz_zakup(nazwa, ilosc)

        msg.showinfo("Sukces", f"Kupiono {ilosc}x {nazwa}")
        self.destroy()

    def zapisz_zakup(self, lek, ilosc):
        df = pd.read_csv("database/customer.csv")
        idx = df[df["email"] == logged_user["email"]].index[0]

        obecne = df.at[idx, "historia_zakupow"] if "historia_zakupow" in df.columns else ""
        if pd.isna(obecne):
            obecne = ""

        nowa = f"{obecne}; {lek}:{ilosc}".strip("; ")
        df.at[idx, "historia_zakupow"] = nowa
        df.to_csv("database/customer.csv", index=False)
