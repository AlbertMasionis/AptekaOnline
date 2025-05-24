class klient:
    def __init__(self, id_klienta, imie, nazwisko,telefon,email,haslo):
        self.id_klienta = id_klienta
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
        self.haslo = haslo
        def __str__(self):
            return f"{self.imie} {self.nazwisko} (ID:{self.id_klienta})"

