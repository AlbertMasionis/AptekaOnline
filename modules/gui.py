import customtkinter as ctk
from PIL import Image
from modules.register_form import register
from modules.login_form import login
from modules.drug_menager import drugs
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


def run_gui():
    app = ctk.CTk()
    app.title("Apteka Online")
    app.geometry("1000x900")
    app.iconbitmap("assets/icon.ico")
    app.configure(fg_color = "#1f2937")
    app.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))

    logo_image = ctk.CTkImage(
        light_image = Image.open("assets/logo.png"),
        dark_image = Image.open("assets/logo.png"),
        size = (300, 100)
    )
    logo_label = ctk.CTkLabel(app, image = logo_image, text = "")
    logo_label.pack(pady = (20, 0))

    main_frame = ctk.CTkFrame(app, fg_color = "#1f2937")
    main_frame.pack(pady = (20, 40), ipadx = 40, ipady = 20)

    icons = {
        "login": ctk.CTkImage(Image.open("assets/login.png"), size = (32, 32)),
        "register": ctk.CTkImage(Image.open("assets/register.png"), size = (32, 32)),
        "browse": ctk.CTkImage(Image.open("assets/browse.png"), size = (32, 32)),
        "buy": ctk.CTkImage(Image.open("assets/buy.png"), size = (32, 32)),
        "admin": ctk.CTkImage(Image.open("assets/admin.png"), size = (32, 32)),
        "exit": ctk.CTkImage(Image.open("assets/exit.png"), size = (32, 32)),
    }

    tiles = [
        ("Zaloguj się", icons["login"], lambda: login(app)),
        ("Zarejestruj się", icons["register"], lambda: register(app)),
        ("Przeglądaj leki", icons["browse"], lambda: drugs(app)),
        ("Kup leki", icons["buy"], lambda: print("Zakup")),
        ("Panel administratora", icons["admin"], lambda: print("Admin")),
        ("Wyjdź", icons["exit"], lambda: sys.exit(0))
    ]

    for text, icon, command in tiles:
        row = ctk.CTkFrame(master = main_frame, fg_color = "transparent")
        row.pack(pady = 12, fill = "x", expand = False)

        icon_wrapper = ctk.CTkFrame(
            row,
            fg_color = "#329e76",
            width = 60,
            height = 60,
            corner_radius = 30
        )
        icon_wrapper.pack_propagate(False)
        icon_wrapper.pack(side = "left", padx = (0, 20))

        icon_label = ctk.CTkLabel(icon_wrapper, image = icon, text = "")
        icon_label.pack(expand = True)

        button = ctk.CTkButton(
            master = row,
            text = text,
            command = command,
            font = ("Arial", 22, "bold"),
            text_color = "#1f2937",
            fg_color = "#329e76",
            hover_color = "#32959e",
            corner_radius = 30,
            height = 70,
            width = 400
        )
        button.pack(side = "left")

    app.mainloop()

if __name__ == "__main__":
    run_gui()