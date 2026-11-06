def total_revenue(sales):
    return round(sum(row["cena"] * row["ilosc"] for row in sales), 2)


def total_items(sales):
    return sum(row["ilosc"] for row in sales)


def most_expensive(sales):
    return max(sales, key=lambda row: row["cena"])["produkt"] if sales else None


def average_transaction(sales):
    return round(total_revenue(sales) / len(sales), 2) if sales else 0.0
