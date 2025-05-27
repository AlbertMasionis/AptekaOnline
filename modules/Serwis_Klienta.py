import csv
import os
from functools import wraps
from datetime import datetime

from modules.Model_Adres import Adres
from modules.Model_Klient import klient

class SerwisKlientow:
    def __init__(self):
        self.klienci = self.wczytaj_klientow()
        self.adresy = self.wczytaj_adresy()

    def loguj_akcje(func):
        @wraps(func)
        def dekorator(self, *args, **kwargs):
            print(f"[{datetime.now()}] Wywołano funkcje:{func.__name__}")
            try:
                result = func(self, *args, **kwargs)
                print(f"[{datetime.now()}] Funckja: {func.__name__} zakończona sukcsesem")
                return result
            except Exception as e:
                print(f"[{datetime.now()}] Błąd funkcji {func.__name__}: {str(e)}")
                raise
        return dekorator

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
                        row['haslo']
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
            pola = ['id_klienta', 'imie', 'nazwisko','telefon', 'email','haslo']
            writer = csv.DictWriter(plik, fieldnames=pola)

            writer.writeheader()
            for klient in self.klienci:
                writer.writerow({
                    'id_klienta': klient.id_klienta,
                    'imie': klient.imie,
                    'nazwisko': klient.nazwisko,
                    'telefon': klient.telefon,
                    'email': klient.email,
                    'haslo': klient.haslo,
                })

    def zapisz_adresy(self):
        sciezka = os.path.join('database','address.csv')

        with open(sciezka, mode='w',encoding='utf-8', newline='') as plik:
            pola = ['id_klienta','ulica','miasto','kod_pocztowy','kraj']
            writer = csv.DictWriter(plik, fieldnames=pola)

            writer.writeheader()
            for adres in self.adresy:
                writer.writerow({
                    'id_klienta': adres.id_klienta,
                    'ulica': adres.ulica,
                    'miasto': adres.miasto,
                    'kod_pocztowy': adres.kod_pocztowy,
                    'kraj': adres.kraj
                })
    #Generator ID generujący po prostu od najmniejszej
    def generator_id(self):
        if not self.klienci:
            nowe_id = 1
        else:
            max_id = max(int(k.id_klienta) for k in self.klienci)
            nowe_id = max_id + 1
        if nowe_id > 9999:
            raise ValueError("Brak dostępnych ID")
        return f"{nowe_id:04d}"


    def zarejestruj(self, imie, nazwisko, telefon, email, haslo, ulica, miasto, kod_pocztowy, kraj):
        id_klienta = self.generator_id()

        nowy_klient = klient(id_klienta, imie, nazwisko, telefon, email, haslo)
        nowy_adres = Adres(id_klienta, ulica, miasto, kod_pocztowy, kraj)

        self.klienci.append(nowy_klient)
        self.adresy.append(nowy_adres)

        return id_klienta

    def znajdz_klienta(self, id_klienta):
        """
        Wyszukuje klienta w systemie na podstawie identyfikatora.

          Przegląda listę zarejestrowanych klientów i zwraca obiekt klienta
          o podanym ID lub None jeśli klient nie istnieje.

          Args:
              id_klienta (str): Unikalny identyfikator klienta w systemie
                                (powinien być 4-cyfrowym stringiem np. "0421")

          Returns:
              Optional[Klient]: Znaleziony obiekt klienta lub None jeśli nie znaleziono

          Example:
              >>> klient = serwis.znajdz_klienta("0421")
              >>> if klient:
              ...     print(f"Znaleziono: {klient.imie} {klient.nazwisko}")
              ... else:
              ...     print("Klient nie istnieje")

          Note:
              - Wyszukiwanie jest dokładne (exact match)
              - Funkcja nie rzuca wyjątków dla nieistniejących ID
              - W przypadku duplikatów ID zwraca pierwsze znalezione wystąpienie
          """
        for klient in self.klienci:
            if klient.id_klienta==id_klienta:
                return klient
        return None
    @loguj_akcje
    def Czy_jest_email(self, email):
        """
        Sprawdza, czy podany email istnieje już w systemie klientów.

            Funkcja wykonuje porównanie adresów email po normalizacji (usunięcie białych znaków
            i konwersja na małe litery), aby zapewnić niezawodne sprawdzanie unikalności.

            Args:
                email (str): Adres email do sprawdzenia. Powinien zawierać poprawny format email.

            Returns:
                bool:
                    - True jeśli email istnieje w systemie
                    - False jeśli email nie istnieje

            Raises:
                AttributeError: Jeśli obiekt klienta nie posiada atrybutu 'email'

            Example:
                >>> serwis = SerwisKlientow()
                >>> serwis.Czy_jest_email("jan.kowalski@example.com")
                True
                >>> serwis.Czy_jest_email("nieistniejacy@email.com")
                False

            Note:
                - Porównanie jest niewrażliwe na wielkość liter
                - Funkcja ignoruje białe znaki na początku/końcu adresu
                - Nie sprawdza poprawności formatu email (tylko porównuje istniejące)
            """
        email = email.strip().lower()
        for klient in self.klienci:
            if klient.email.strip().lower() == email:
                return True
        return False
    @loguj_akcje
    def Czy_jest_telefon(self, telefon):
        for klient in self.klienci:
            if klient.telefon.lower() == telefon.lower():
                return True
        return False