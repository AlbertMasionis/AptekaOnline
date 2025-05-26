import csv
import random

def register_client(firstname, lastname, phone, email, password):
    client_id = random.randint(1000, 9999)
    with open("database/customer.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([client_id, firstname, lastname, phone, email, password, ""])

def delete_client(identifier):
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
    with open("database/customer.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if str(row[0]) == str(client_id):
                history = row[6]
                return history.split(",") if history else []
    return []
