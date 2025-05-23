class Adres:
    def __init__(self, id_klienta, ulica, miasto, kod_pocztowy, kraj):
        self.id_klienta = id_klienta
        self.ulica = ulica
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy
        self.kraj = kraj

    def __str__(self):
        return f"{self.ulica}, {self.miasto},{self.kod_pocztowy},{self.kraj}"
