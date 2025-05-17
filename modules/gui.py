import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


def runGui():
    app = ctk.CTk()
    app.title("Apteka Online")
    app.geometry("1000x700")
    app.configure(fg_color = "#1f2937")

    header = ctk.CTkLabel(
        app,
        text = "APTEKA ONLINE",
        font = ("Arial", 46, "bold"),
        text_color = "white"
    )
    header.pack(pady=40)

    mainFrame = ctk.CTkFrame(app, fg_color = "#1f2937")
    mainFrame.pack(pady = 20, ipadx = 40, ipady = 40)

    tiles = [
        ("Zaloguj się", lambda: print("Logowanie")),
        ("Zarejestruj się", lambda: print("Rejestracja")),
        ("Przeglądaj leki", lambda: print("Przegląd")),
        ("Kup leki", lambda: print("Zakup")),
        ("Panel administratora", lambda: print("Admin")),
        ("Wyjdź", app.destroy)
    ]

    for text, command in tiles:
        tile = ctk.CTkButton(
            master = mainFrame,
            text = text,
            command = command,
            height = 80,
            width = 400,
            font = ("Arial", 24, "bold"),
            text_color = "#1f2937",
            corner_radius = 30
        )
        tile.pack(pady = 15)

    app.mainloop()
