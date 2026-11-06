import csv
from pathlib import Path


def load_sales(path):
    """Wczytuje sprzedaż z CSV i zwraca listę słowników."""
    with Path(path).open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None or not {"produkt", "cena", "ilosc"}.issubset(reader.fieldnames):
            raise ValueError("CSV musi zawierać kolumny: produkt, cena, ilosc")
        result = []
        for row in reader:
            price = float(row["cena"])
            quantity = int(row["ilosc"])
            if price < 0 or quantity < 0:
                raise ValueError("Cena i ilość nie mogą być ujemne")
            result.append({"produkt": row["produkt"], "cena": price, "ilosc": quantity})
        return result
