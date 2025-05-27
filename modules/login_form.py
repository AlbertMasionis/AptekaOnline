import customtkinter as ctk
import csv
from modules.session import logged_user

class login(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Logowanie")
        self.geometry("400x600")
        self.configure(fg_color="#1f2937")
        self.focus()
        self.grab_set()

        ctk.CTkLabel(
            self,
            text="Logowanie",
            font=("Arial", 38, "bold"),
            text_color="#329e76"
        ).pack(pady=(20, 30))

        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        form_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        form_frame.pack(fill="x")

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

        message_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        message_frame.pack(pady=(10, 0), fill="x")

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
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        try:
            with open("database/customer.csv", "r", encoding="utf-8", newline='') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row.get("email") == email and row.get("haslo") == password:
                        logged_user.update(row)
                        self.show_message("Logowanie pomyślne!", error=False)
                        self.after(1000, self.finish_login)
                        return

                self.show_message("Nieprawidłowy email lub hasło", error=True)

        except Exception as e:
            print(f"Błąd logowania: {str(e)}")
            self.show_message("Wystąpił błąd podczas logowania", error=True)

    def show_message(self, text, error=True):
        self.message_label.configure(
            text=text,
            text_color="#ff5f5f" if error else "#4CAF50"
        )

    def finish_login(self):
        try:
            user_id = int(logged_user.get("id_klienta", -1))
            if user_id == 0:
                from modules.admin_panel import AdminPanel
                AdminPanel(self.master if self.master else None)
            else:
                from modules.user_panel import UserPanel
                UserPanel(self.master if self.master else None)
        except Exception as e:
            print(f"Błąd podczas otwierania panelu: {e}")

        self.destroy()

