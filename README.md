# Sales Analyzer — projekt dydaktyczny
Projekt dydaktyczny mający na celu naukę testowania oraz przygotowania GitHub Actions

## Przygotowanie i uruchamianie projektu
Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Testowanie kodu
Do przeprowadzenia testów wykorzystana została biblioteka *pytest*
Uruchamianie testów:
```bash
python -m pytest -v
```