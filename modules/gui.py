"""
Moduł głównego interfejsu użytkownika aplikacji Apteka Online

Implementuje główne okno aplikacji z menu nawigacyjnym, wykorzystujące bibliotekę CustomTkinter.
Zawiera funkcjonalności do zarządzania wyglądem aplikacji i podstawową nawigację.

Struktura interfejsu:
1. Główne okno aplikacji (1000x900px)
   - Motyw ciemny ('dark')
   - Kolor akcentu: zielony ('green')
   - Tło: #1f2937 (ciemno-szare)

2. Główne elementy UI:
   - Logo aplikacji (assets/logo.png)
   - Przyciski nawigacyjne z ikonami:
     * Zaloguj się (assets/login.png)
     * Zarejestruj się (assets/register.png)
     * Przeglądaj leki (assets/browse.png)
     * Wyjdź (assets/exit.png)

Funkcje:
- run_gui(): Inicjalizuje i uruchamia główne okno aplikacji

Wymagania systemowe:
- Python 3.7+
- CustomTkinter >= 5.0
- Pillow (PIL) do obsługi obrazów

Ścieżki do zasobów:
- assets/icon.ico - ikona aplikacji
- assets/logo.png - logo aplikacji
- assets/[login|register|browse|exit].png - ikony przycisków

Przykład użycia:
    if __name__ == "__main__":
        run_gui()

Uwagi:
- Aplikacja używa protokołu WM_DELETE_WINDOW do poprawnego zamykania
- Wszystkie ścieżki do zasobów są względne
- Rozmiary i kolory przycisków są znormalizowane
"""


import customtkinter as ctk
from PIL import Image
from modules.register_form import register
from modules.login_form import login
from modules.drug_finder import drugs
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


def run_gui():
    app = ctk.CTk()
    app.title("Apteka Online")
    app.geometry("1000x900")
    app.iconbitmap("assets/icon.ico")
    app.configure(fg_color="#1f2937")
    app.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))

    main_container = ctk.CTkFrame(app, fg_color="transparent")
    main_container.pack(expand=True, fill="both", padx=20, pady=50)

    logo_frame = ctk.CTkFrame(main_container, fg_color="transparent", height=160)
    logo_frame.pack(fill="x")
    logo_frame.pack_propagate(False)

    logo_image = ctk.CTkImage(
        light_image=Image.open("assets/logo.png"),
        dark_image=Image.open("assets/logo.png"),
        size=(300, 100)
    )
    logo_label = ctk.CTkLabel(logo_frame, image=logo_image, text="")
    logo_label.pack(pady=(70, 0))

    menu_container = ctk.CTkFrame(main_container, fg_color="transparent")
    menu_container.pack(expand=True, fill="both")

    center_frame = ctk.CTkFrame(menu_container, fg_color="transparent")
    center_frame.place(relx=0.5, rely=0.43, anchor="center")

    icons = {
        "login": ctk.CTkImage(Image.open("assets/login.png"), size=(32, 32)),
        "register": ctk.CTkImage(Image.open("assets/register.png"), size=(32, 32)),
        "browse": ctk.CTkImage(Image.open("assets/browse.png"), size=(32, 32)),
        "exit": ctk.CTkImage(Image.open("assets/exit.png"), size=(32, 32)),
    }

    tiles = [
        ("Zaloguj się", icons["login"], lambda: login(app)),
        ("Zarejestruj się", icons["register"], lambda: register(app)),
        ("Przeglądaj leki", icons["browse"], lambda: drugs(app)),
        ("Wyjdź", icons["exit"], lambda: sys.exit(0))
    ]

    for text, icon, command in tiles:
        row = ctk.CTkFrame(master=center_frame, fg_color="transparent")
        row.pack(pady=12, fill="x", expand=False)

        icon_wrapper = ctk.CTkFrame(
            row,
            fg_color="#329e76",
            width=60,
            height=60,
            corner_radius=30
        )
        icon_wrapper.pack_propagate(False)
        icon_wrapper.pack(side="left", padx=(0, 20))

        icon_label = ctk.CTkLabel(icon_wrapper, image=icon, text="")
        icon_label.pack(expand=True)

        button = ctk.CTkButton(
            master=row,
            text=text,
            command=command,
            font=("Arial", 22, "bold"),
            text_color="#1f2937",
            fg_color="#329e76",
            hover_color="#32959e",
            corner_radius=30,
            height=70,
            width=400
        )
        button.pack(side="left")

    app.mainloop()

if __name__ == "__main__":
    run_gui()