import customtkinter as ctk
from modules.register_form import register
from modules.login import LoginForm
from PIL import Image
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def run_gui():
    app = ctk.CTk()
    app.title("Apteka Online")
    app.iconbitmap("assets/icon.ico")
    app.geometry("700x700")
    app.configure(fg_color="#1f2937")

    app.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))

    # ----- Główna ramka -----
    main_container = ctk.CTkFrame(app, fg_color="#1f2937")
    main_container.pack(expand=True, fill="both")

    # ----- Logo -----
    logo_image = ctk.CTkImage(
        light_image=Image.open("assets/logo.png"),
        dark_image=Image.open("assets/logo.png"),
        size=(300, 100)
    )

    logo_label = ctk.CTkLabel(
        main_container,
        image=logo_image,
        text="",
    )
    logo_label.pack(pady=(40,0))

    # ----- Ramka na kafelki -----
    tiles_frame = ctk.CTkFrame(main_container, fg_color="#1f2937")
    tiles_frame.pack(pady=(26,0))

    # ----- Lista kafelków -----
    tiles = [
        ("Zaloguj się", lambda: LoginForm(app)),
        ("Zarejestruj się", lambda: register(app)),
        ("Przeglądaj leki", lambda: print("Przegląd")),
        ("Kup leki", lambda: print("Zakup")),
        ("Panel administratora", lambda: print("Admin")),
        ("Wyjdź", lambda: sys.exit(0))
    ]

    for text, command in tiles:
        tile = ctk.CTkButton(
            master=tiles_frame,
            text=text,
            command=command,
            height=60,
            width=400,
            font=("Arial", 22, "bold"),
            text_color="#1f2937",
            fg_color="#329e76",
            hover_color="#32959e",
            corner_radius=30
        )
        tile.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    run_gui()
