from pathlib import Path
from loader import load_sales
from analysis import total_revenue, total_items, most_expensive, average_transaction


def main():
    sales = load_sales(Path(__file__).parent / "data" / "sales.csv")
    print(f"Przychód: {total_revenue(sales):.2f} zł")
    print(f"Sprzedane sztuki: {total_items(sales)}")
    print(f"Najdroższy produkt: {most_expensive(sales)}")
    print(f"Średnia wartość wiersza sprzedaży: {average_transaction(sales):.2f} zł")


if __name__ == "__main__":
    main()
