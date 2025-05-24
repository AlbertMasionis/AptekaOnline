import customtkinter as ctk
import csv
from modules.session import logged_user
from modules.buy_drugs import BuyDrugsWindow


class login(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Logowanie")
        self.geometry("400x600")
        self.configure(fg_color="#1f2937")
        self.focus()
        self.grab_set()

        # Nagłówek
        ctk.CTkLabel(
            self,
            text="Logowanie",
            font=("Arial", 38, "bold"),
            text_color="#329e76"
        ).pack(pady=(20, 30))

        # Główna ramka dla formularza
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Ramka na pola formularza
        form_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        form_frame.pack(fill="x")

        # Pole email
        ctk.CTkLabel(
            form_frame,
            text="Email:",
            text_color="#dce2e2",
            font=("Arial", 20, "bold")
        ).pack(pady=(10, 0))

        self.email_entry = ctk.CTkEntry(
            form_frame,
            width=350,
            height=45,
            font=("Arial", 18),
            corner_radius=10,
            text_color="#1f2937",
            fg_color="#329e76"
        )
        self.email_entry.pack(pady=(5, 20))

        # Pole hasła
        ctk.CTkLabel(
            form_frame,
            text="Hasło:",
            text_color="#dce2e2",
            font=("Arial", 20, "bold")
        ).pack(pady=(10, 0))

        self.password_entry = ctk.CTkEntry(
            form_frame,
            width=350,
            height=45,
            font=("Arial", 18),
            corner_radius=10,
            text_color="#1f2937",
            fg_color="#329e76",
            show="*"
        )
        self.password_entry.pack(pady=(5, 20))

        # Przycisk logowania
        ctk.CTkButton(
            form_frame,
            text="Zaloguj się",
            command=self.authenticate,
            font=("Arial", 22, "bold"),
            fg_color="#329e76",
            hover_color="#32959e",
            text_color="#1f2937",
            corner_radius=25,
            width=300,
            height=55
        ).pack(pady=30)

        # Ramka na komunikat
        message_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        message_frame.pack(pady=(10, 0), fill="x")

        # Etykieta komunikatu
        self.message_label = ctk.CTkLabel(
            message_frame,
            text="",
            font=("Arial", 16, "bold"),
            text_color="#ff5f5f",
            wraplength=380,
            justify="center"
        )
        self.message_label.pack()

    def authenticate(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        try:
            with open("database/customer.csv", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row.get("email") == email and row.get("haslo") == password:
                        logged_user.update(row)
                        self.show_message("Logowanie pomyślne! Przenoszenie do panelu...", error=False)
                        self.after(1500, lambda: [self.destroy(), BuyDrugsWindow(self.master)])
                        return

                self.show_message("Nieprawidłowy email lub hasło", error=True)

        except Exception as e:
            print(f"Błąd logowania: {str(e)}")
            self.show_message("Wystąpił błąd podczas logowania", error=True)

    def show_message(self, text, error=True):
        """Funkcja do wyświetlania komunikatów"""
        self.message_label.configure(
            text=text,
            text_color="#ff5f5f" if error else "#4CAF50"
        )