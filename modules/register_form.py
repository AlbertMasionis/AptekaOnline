import customtkinter as ctk

class register(ctk.CTkToplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.title("Rejestracja")
        self.geometry("600x800")
        self.configure(fg_color = "#1f2937")

        self.focus()
        self.grab_set()

        ctk.CTkLabel(
            self,
            text = "Rejestracja",
            font=("Arial", 34, "bold"),
            text_color = "#329e76"
        ).pack(pady = 30)

        self.inputs = {}

        fields = [
            ("Imię", "first_name"),
            ("Nazwisko", "last_name"),
            ("Email", "email"),
            ("Hasło", "password"),
            ("Powtórz hasło", "confirm_password"),
            ("Adres", "address"),
            ("Telefon", "phone")
        ]

        for label_text, field_name in fields:
            ctk.CTkLabel(self, text = label_text, font = ("Arial", 16), text_color = "white").pack(pady = (10, 0))
            entry = ctk.CTkEntry(self, width = 400, show = "*" if "hasło" in label_text.lower() else "")
            entry.pack(pady = 5)
            self.inputs[field_name] = entry

        ctk.CTkButton(
            self,
            text = "Zarejestruj się",
            command = self.submit_form,
            fg_color = "#329e76",
            hover_color = "#2d7f64",
            font = ("Arial", 18),
            text_color = "#1f2937",
            height = 50,
            corner_radius = 25
        ).pack(pady = 30)

    def submit_form(self):
        #
        #
        #
        data = {key: widget.get() for key, widget in self.inputs.items()}
        print("Dane z formularza:", data)
        self.destroy()
