import customtkinter as ctk
from modules.buy_drugs import BuyDrugsWindow
from modules.session import logged_user


class UserPanel(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Panel użytkownika")
        self.geometry("600x400")
        self.configure(fg_color="#1f2937")
        self.focus()
        self.grab_set()

        # Powitanie
        ctk.CTkLabel(
            self,
            text=f"Witaj, {logged_user.get('imie', 'Użytkowniku')}!",
            font=("Arial", 28, "bold"),
            text_color="#329e76"
        ).pack(pady=20)

        # Przycisk do zakupu leków
        ctk.CTkButton(
            self,
            text="Kup leki",
            command=lambda: BuyDrugsWindow(self),
            fg_color="#329e76",
            hover_color="#32959e",
            font=("Arial", 20, "bold"),
            text_color="#1f2937",
            height=50,
            corner_radius=25,
            width=300
        ).pack(pady=20)

        # Możesz dodać więcej funkcji np.:
        # - wyloguj się
        # - zobacz historię zakupów
