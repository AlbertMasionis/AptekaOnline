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
            font = ("Arial", 38, "bold"),
            text_color = "#329e76"
        ).pack(pady = (20, 10))

        self.inputs = {}

        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color = "#1f2937",
            width = 550
        )
        scroll_frame.pack(fill = "both", expand = True, padx = 20, pady = (0, 20))

        fields = [
            ("Imię:", "first_name"),
            ("Nazwisko:", "last_name"),
            ("Email:", "email"),
            ("Hasło:", "password"),
            ("Powtórz hasło:", "confirm_password"),
            ("Adres:", "address"),
            ("Telefon:", "phone")
        ]

        for label_text, field_name in fields:
            ctk.CTkLabel(
                scroll_frame,
                text = label_text,
                font = ("Arial", 20, "bold"),
                text_color = "white"
            ).pack(pady = (10, 0))

            entry = ctk.CTkEntry(
                scroll_frame,
                width = 480,
                height = 45,
                font = ("Arial", 20, "bold"),
                corner_radius = 10,
                text_color = "#1f2937",
                fg_color = "#329e76",
                show = "*" if "hasło" in label_text.lower() else ""
            )
            entry.pack(pady = 5)
            self.inputs[field_name] = entry

        ctk.CTkButton(
            scroll_frame,
            text = "Zarejestruj się",
            command = self.submit_form,
            fg_color = "#329e76",
            hover_color = "#32959e",
            font = ("Arial", 22, "bold"),
            text_color = "#1f2937",
            height = 55,
            corner_radius = 25,
            width = 300
        ).pack(pady = 40)

    def submit_form(self):
        data = {key: widget.get() for key, widget in self.inputs.items()}
        print("Dane z formularza:", data)
        self.destroy()