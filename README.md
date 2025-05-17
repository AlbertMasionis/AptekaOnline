# Apteka Online

## Opis projektu

Apteka Online jest aplikacją stworzoną w Pythonie, umożliwiającą zarządzanie klientami, lekami oraz zakupami w aptece internetowej.  
Projekt wykorzystuje bibliotekę `customtkinter` do stworzenia interfejsu graficznego oraz moduły do obsługi baz danych w formacie CSV i XLSX.

---

## Funkcjonalności

- Rejestracja i usuwanie klientów z bazy danych
- Dodawanie i usuwanie leków w bazie
- Przegląd dostępnych leków
- Zakupy leków przez klientów 
- Automatyczne generowanie unikalnych ID klientów
- Graficzny interfejs użytkownika 
- Obsługa plików danych w folderze `data/` (CSV, XLSX)
- Obsługa plików zakupów klienta w folderze `data/`

---

## Instalacja

1. Sklonuj repozytorium:
git clone https://github.com/twojlogin/AptekaOnline.git
cd AptekaOnline

2. Utwórz i aktywuj wirtualne środowisko (opcjonalnie):
- Windows:
  ```
  python -m venv .venv
  .venv\Scripts\activate
  ```
- Linux/MacOS:
  ```
  python3 -m venv .venv
  source .venv/bin/activate
  ```

3. Zainstaluj wymagane pakiety:
pip install -r requirements.txt

---

## Uruchomienie aplikacji

Po zainstalowaniu zależności uruchom program poleceniem:

python main.py

---

## Używane biblioteki

- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) — nowoczesny GUI dla Tkinter  
- [Pillow](https://python-pillow.org/) — obsługa grafiki i zdjęć  
- [openpyxl](https://openpyxl.readthedocs.io/) — odczyt i zapis plików Excel XLSX  
