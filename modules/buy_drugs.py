import customtkinter as ctk
import pandas as pd
from modules.session import logged_user


class BuyDrugsWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Kup lek")
        self.geometry("700x700")
        self.configure(fg_color="#1f2937")
        self.focus()
        self.grab_set()

        if not logged_user:
            self.show_message("Musisz być zalogowany", error=True)
            self.after(2000, self.destroy)
            return

        self.drugs_df = pd.read_excel("database/drugs.xlsx")
        self.selected_drug = ctk.StringVar()
        self.quantity = ctk.IntVar(value=1)

        # Nagłówek
        ctk.CTkLabel(
            self,
            text="Panel zakupu leków",
            font=("Arial", 38, "bold"),
            text_color="#329e76"
        ).pack(pady=(30, 20))

        # Ramka główna
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Ramka formularza
        form_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        form_frame.pack(pady=20)

        # Wybór leku
        ctk.CTkLabel(
            form_frame,
            text="Wybierz lek:",
            font=("Arial", 22, "bold"),
            text_color="white"
        ).pack(pady=(0, 10))

        drug_names = self.drugs_df["nazwa"].tolist()
        self.dropdown = ctk.CTkOptionMenu(
            form_frame,
            values=drug_names,
            variable=self.selected_drug,
            font=("Arial", 20),
            dropdown_font=("Arial", 18),
            width=400,
            height=45,
            corner_radius=10,
            fg_color="#329e76",
            button_color="#329e76",
            button_hover_color="#32959e",
            text_color="#1f2937",
            dropdown_fg_color="#329e76",
            dropdown_text_color="#1f2937",
            dropdown_hover_color="#32959e"
        )
        self.dropdown.pack(pady=10)

        # Ilość
        ctk.CTkLabel(
            form_frame,
            text="Ilość:",
            font=("Arial", 22, "bold"),
            text_color="white"
        ).pack(pady=(20, 10))

        self.qty_entry = ctk.CTkEntry(
            form_frame,
            textvariable=self.quantity,
            width=150,
            height=45,
            font=("Arial", 20),
            corner_radius=10,
            fg_color="#329e76",
            text_color="#1f2937",
            justify="center"
        )
        self.qty_entry.pack(pady=10)

        # Przycisk zakupu
        ctk.CTkButton(
            form_frame,
            text="Kup",
            command=self.kup_lek,
            font=("Arial", 22, "bold"),
            fg_color="#329e76",
            hover_color="#32959e",
            text_color="#1f2937",
            height=55,
            width=200,
            corner_radius=25
        ).pack(pady=30)

        # Ramka na komunikaty
        self.message_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        self.message_frame.pack(pady=(10, 20), fill="x")

        self.message_label = ctk.CTkLabel(
            self.message_frame,
            text="",
            font=("Arial", 18, "bold"),
            text_color="#ff5f5f",
            wraplength=600,
            justify="center"
        )
        self.message_label.pack()


    def kup_lek(self):
        nazwa = self.selected_drug.get()
        ilosc = self.quantity.get()

        if ilosc <= 0:
            self.show_message("Podaj poprawną ilość", error=True)
            return

        try:
            index = self.drugs_df[self.drugs_df["nazwa"] == nazwa].index[0]
            stan = self.drugs_df.at[index, "stan_magazynowy"]

            if ilosc > stan:
                self.show_message("Brak wystarczającej ilości w magazynie", error=True)
                return

            # Aktualizacja magazynu
            self.drugs_df.at[index, "stan_magazynowy"] = stan - ilosc
            self.drugs_df.to_excel("database/drugs.xlsx", index=False)

            # Zapis zakupu
            self.zapisz_zakup(nazwa, ilosc)

            self.show_message(f"Pomyślnie kupiono {ilosc}x {nazwa}", error=False)
            self.after(2000, lambda: [self.message_label.configure(text=""), self.quantity.set(1)])

        except Exception as e:
            print(f"Błąd zakupu: {str(e)}")
            self.show_message("Wystąpił błąd podczas zakupu", error=True)

    def zapisz_zakup(self, lek, ilosc):
        try:
            df = pd.read_csv("database/customer.csv")
            idx = df[df["email"] == logged_user["email"]].index[0]

            obecne = df.at[idx, "historia_zakupow"] if "historia_zakupow" in df.columns else ""
            if pd.isna(obecne):
                obecne = ""

            nowa = f"{obecne}; {lek}:{ilosc}".strip("; ")
            df.at[idx, "historia_zakupow"] = nowa
            df.to_csv("database/customer.csv", index=False)

        except Exception as e:
            print(f"Błąd zapisu historii: {str(e)}")

    def show_message(self, text, error=True):
        """Wyświetla komunikat w interfejsie"""
        self.message_label.configure(
            text=text,
            text_color="#ff5f5f" if error else "#4CAF50"
        )