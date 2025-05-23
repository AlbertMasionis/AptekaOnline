import csv
import os


from modules.Model_Adres import Adres
from modules.Model_Klient import klient


class SerwisKlientow:
    def __init__(self):
        self.klienci = self.wczytaj_klientow()
        self.adresy = self.wczytaj_adresy()
    def wczytaj_klientow(self):
        sciezka = os.path.join("database","customer.csv")
        klienci = []

        if os.path.exists(sciezka):
            with open(sciezka, mode='r', encoding="utf-8")as plik:
                reader = csv.DictReader(plik)
                for row in reader:
                    klienci.append(klient(
                        row['id_klienta'],
                        row['imie'],
                        row['nazwisko'],
                        row['telefon'],
                        row['email'],
                    ))
        return klienci
    def wczytaj_adresy(self):
        sciezka = os.path.join("database","address.csv")
        adresy = []
        if os.path.exists(sciezka):
            with open(sciezka, mode='r', encoding='utf-8')as plik:
                reader = csv.DictReader(plik)
                for row in reader:
                    adresy.append(Adres(
                        row['id_klienta'],
                        row['ulica'],
                        row['miasto'],
                        row['kod_pocztowy'],
                        row['kraj']
                    ))
        return adresy

    def zapisz_klientow(self):
        sciezka = os.path.join('database','customer.csv')

        with open(sciezka, mode='w', encoding='utf-8', newline='') as plik:
            pola = ['id_klienta', 'imie', 'nazwisko',' telefon', 'email']
            writer = csv.DictWriter(plik, fieldnames=pola)

            writer.writeheader()
            for klient in self.klienci:
                writer.writerow({
                    'id_klienta': klient.id_klienta,
                    'imie': klient.imie,
                    'nazwisko': klient.nazwisko,
                    'telefon': klient.telefon,
                    'email': klient.email,
                })

    def zapisz_adresy(self):
        sciezka = os.path.join('database','address.csv')

        with open(sciezka, mode='w',encoding='utf-8', newline='') as plik:
            pola = ['id_klienta','ulica','miasto','kod-pocztowy','kraj']
            writer = csv.DictWriter(plik, fieldnames=pola)

            writer.writeheader()
            for adres in self.adresy:
                writer.writerow({
                    'id_klienta': adres.id_klienta,
                    'ulica': adres.ulica,
                    'miasto': adres.miasto,
                    'kod-pocztowy': adres.kod_pocztowy,
                    'kraj': adres.kraj
                })
    def generator_id(self):
        if not self.klienci:
            nowe_id = 1
        else:
            max_id = max(int(k.id_klienta) for k in self.klienci)
            nowe_id = max_id + 1
        if nowe_id > 9999:
            raise ValueError("Brak dostępnych ID")
        return f"{nowe_id:04d}"


    def zarejestruj(self, imie, nazwisko, telefon, email, ulica, miasto, kod_pocztowy, kraj):
        id_klienta = self.generator_id()

        nowy_klient = klient(id_klienta, imie, nazwisko, telefon, email)
        nowy_adres = Adres(id_klienta, ulica, miasto, kod_pocztowy, kraj)

        self.klienci.append(nowy_klient)
        self.adresy.append(nowy_adres)

        return id_klienta

    def znajdz_klienta(self, id_klienta):
        for klient in self.klienci:
            if klient.id_klienta==id_klienta:
                return klient
            return None