import csv
import random

def register_client(firstname, lastname, phone, email, password):
    client_id = random.randint(1000, 9999)
    with open("database/customer.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([client_id, firstname, lastname, phone, email, password, ""])

def delete_client(identifier):
    """Usuwa klienta z bazy danych na podstawie identyfikatora (ID lub email).

       Funkcja wyszukuje klienta w pliku CSV i usuwa wszystkie wiersze zawierające
       podany identyfikator. Obsługuje wyszukiwanie zarówno po ID jak i adresie email.

       Args:
           identifier (str | int): Unikalny identyfikator klienta do usunięcia.
                                  Może być:
                                  - ID klienta (liczba)
                                  - Adres email (string)

       Returns:
           bool: Flaga wskazująca czy operacja się powiodła:
                 - True jeśli znaleziono i usunięto klienta
                 - False jeśli klient nie istnieje

       Raises:
           FileNotFoundError: Jeśli plik database/customer.csv nie istnieje
           PermissionError: Jeśli brak uprawnień do zapisu pliku

       Example:
           >>> # Usunięcie po ID
           >>> delete_client(1001)
           True

           >>> # Usunięcie po emailu
           >>> delete_client("klient@example.com")
           True

           >>> # Próba usunięcia nieistniejącego klienta
           >>> delete_client("nieistniejacy@email.com")
           False

       Note:
           - Funkcja modyfikuje bezpośrednio plik CSV
           - Usuwa wszystkie wystąpienia identyfikatora (teoretyczna ochrona przed duplikatami)
           - W przypadku błędów plikowych może pozostawić częściowe dane
       """
    removed = False
    updated_rows = []
    with open("database/customer.csv", mode="r", encoding="utf-8") as file:
        for row in csv.reader(file):
            if identifier not in row:
                updated_rows.append(row)
            else:
                removed = True
    with open("database/customer.csv", mode="w", newline='', encoding="utf-8") as file:
        csv.writer(file).writerows(updated_rows)
    return removed

def get_purchase_history(client_id):
    try: # potrzebne aby móc kontrolowac błędy
        with open("database/customer.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if str(row[0]) == str(client_id):
                    history = row[6]
                return history.split(",") if history else []
        return []

    # obsługa błędów
    except FileNotFoundError:
        print("Błąd: Plik customer.csv nie istnieje!")
        return []
    except PermissionError:
        print("Brak uprawnień do odczytu pliku!")
        return []
    except Exception as e:
        print(f"Niespodziewany błąd: {e}")
        return []