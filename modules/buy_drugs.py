import customtkinter as ctk
import pandas as pd
from modules.session import logged_user


class BuyDrugsWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Kup leki")
        self.geometry("700x800")
        self.configure(fg_color="#1f2937")
        self.focus()
        self.grab_set()

        self.drugs_df = pd.read_excel("database/drugs.xlsx")
        self.selected_drug = ctk.StringVar()
        self.quantity = ctk.IntVar(value=1)
        self.prescription_number = ctk.StringVar()

        ctk.CTkLabel(
            self,
            text="Kup lek",
            font=("Arial", 38, "bold"),
            text_color="#329e76"
        ).pack(pady=(30, 20))

        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)

        form_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        form_frame.pack(pady=20)

        # Wybór leku
        ctk.CTkLabel(
            form_frame,
            text="Wybierz lek:",
            font=("Arial", 22, "bold"),
            text_color="#dce2e2"
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
            text_color="#dce2e2"
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

        # Numer recepty
        ctk.CTkLabel(
            form_frame,
            text="Numer recepty (jeśli wymagany, inaczej wpisz 0):",
            font=("Arial", 20, "bold"),
            text_color="#dce2e2"
        ).pack(pady=(20, 10))

        self.recepta_entry = ctk.CTkEntry(
            form_frame,
            textvariable=self.prescription_number,
            width=250,
            height=45,
            font=("Arial", 20),
            corner_radius=10,
            fg_color="#329e76",
            text_color="#1f2937",
            justify="center"
        )
        self.recepta_entry.pack(pady=10)

        # Przycisk kupna
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

        # Komunikaty
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
        recepta_input = self.prescription_number.get().strip()

        if ilosc <= 0:
            self.show_message("Podaj poprawną ilość", error=True)
            return

        if not recepta_input.isdigit():
            self.show_message("Numer recepty musi być liczbą (lub 0)", error=True)
            return

        try:
            index = self.drugs_df[self.drugs_df["nazwa"] == nazwa].index[0]
            stan = self.drugs_df.at[index, "stan_magazynowy"]
            wymagana_recepta = str(self.drugs_df.at[index, "numer_recepty"])

            if wymagana_recepta != "0" and recepta_input != wymagana_recepta:
                self.show_message("Nieprawidłowy numer recepty!", error=True)
                return

            if ilosc > stan:
                self.show_message("Brak wystarczającej ilości w magazynie", error=True)
                return

            # Aktualizacja stanu i zapis
            self.drugs_df.at[index, "stan_magazynowy"] = stan - ilosc
            self.drugs_df.to_excel("database/drugs.xlsx", index=False)

            # Historia zakupów
            self.zapisz_zakup(nazwa, ilosc)

            self.show_message(f"Pomyślnie kupiono {ilosc}x {nazwa}", error=False)
            self.after(2000, lambda: [
                self.message_label.configure(text=""),
                self.quantity.set(1),
                self.prescription_number.set("0")
            ])

        except Exception as e:
            print(f"Błąd zakupu: {str(e)}")
            self.show_message("Wystąpił błąd podczas zakupu", error=True)

    def zapisz_zakup(self, lek, ilosc):
        try:
            df = pd.read_csv("database/customer.csv")
            idx = df[df["email"] == logged_user["email"]].index[0]
            obecne = (lambda x: x if not pd.isna(x) else "")(df.at[idx, "historia_zakupow"]) if "historia_zakupow" in df.columns else ""
            nowa = f"{obecne}; {lek}:{ilosc}".strip("; ")
            df.at[idx, "historia_zakupow"] = nowa
            df.to_csv("database/customer.csv", index=False)
        except Exception as e:
            print(f"Błąd zapisu historii: {str(e)}")

    def show_message(self, text, error=True):
        self.message_label.configure(
            text=text,
            text_color="#ff5f5f" if error else "#4CAF50"
        )
