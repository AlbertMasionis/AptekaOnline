import customtkinter as ctk
from modules.register_form import register
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


def run_gui():
    app = ctk.CTk()
    app.title("Apteka Online")
    app.geometry("1000x900")
    app.configure(fg_color="#1f2937")

    app.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))

    header = ctk.CTkLabel(
        app,
        text = "▰▱▰▱▰▱▰▱▰▱▰▱▰▱  APTEKA ONLINE  ▰▱▰▱▰▱▰▱▰▱▰▱▰▱",
        font = ("Arial", 56, "bold"),
        text_color = "#329e76"
    )
    header.pack(pady=40)

    main_frame = ctk.CTkFrame(app, fg_color="#1f2937")
    main_frame.pack(pady=20, ipadx=40, ipady=40)

    tiles = [
        ("Zaloguj się", lambda: print("Logowanie")),
        ("Zarejestruj się", lambda: register(app)),
        ("Przeglądaj leki", lambda: print("Przegląd")),
        ("Kup leki", lambda: print("Zakup")),
        ("Panel administratora", lambda: print("Admin")),
        ("Wyjdź", lambda: sys.exit(0))
    ]

    for text, command in tiles:
        tile = ctk.CTkButton(
            master = main_frame,
            text = text,
            command = command,
            height = 80,
            width = 400,
            font = ("Arial", 24, "bold"),
            text_color = "#1f2937",
            fg_color = "#329e76",
            hover_color = "#32959e",
            corner_radius = 30
        )
        tile.pack(pady = 15)

    app.mainloop()

if __name__ == "__main__":
    run_gui()