import customtkinter as ctk
from modules.buy_drugs import BuyDrugsWindow
from modules.session import logged_user
from modules.customer_manager import get_purchase_history


class UserPanel(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Panel użytkownika")
        self.geometry("600x500")
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

        # Historia zakupów
        client_id = logged_user.get("id_klienta")
        history = get_purchase_history(client_id)
        history_text = "Brak historii zakupów." if not history else "Historia zakupów:\n" + "\n".join(f"• {item}" for item in history)

        self.history_label = ctk.CTkLabel(
            self,
            text=history_text,
            font=("Arial", 16),
            text_color="white",
            justify="left",
            wraplength=500
        )
        self.history_label.pack(pady=10)
