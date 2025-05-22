class klient:
    def __init__(self, id_klienta, imie, nazwisko,telefon,email):
        self.id_klienta = id_klienta
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
        def __str__(self):
            return f"{self.imie} {self.nazwisko} (ID:{self.id_klienta})"

