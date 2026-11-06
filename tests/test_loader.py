import pytest
from loader import load_sales

def test_load_sales(tmp_path):
    path = tmp_path / "sales.csv"
    path.write_text("produkt,cena,ilosc\nMysz,80,2\n", encoding="utf-8")
    assert load_sales(path) == [{"produkt" : "Mysz", "cena" : 80.0, "ilosc" : 2}]