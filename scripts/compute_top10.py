import csv
from pathlib import Path

def top10(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        # last header is 2024
        year_col = len(headers)-1
        rows = []
        for r in reader:
            if not r: continue
            country = r[0]
            # some rows may have missing columns; guard
            try:
                val = int(r[year_col]) if r[year_col] else 0
            except Exception:
                try:
                    val = int(float(r[year_col]))
                except Exception:
                    val = 0
            rows.append((country, val))
    rows.sort(key=lambda x: x[1], reverse=True)
    return rows[:10]

base = Path(r"c:/Users/adria/OneDrive/FIT3179/GIT Repo/FIT3179/3_choropleth_map/data")
arr = top10(base / 'Arrivals Time Series.csv')
dep = top10(base / 'Departure Time Series.csv')
print('ARRIVALS_TOP10=')
for c,v in arr:
    print(f"{c}\t{v}")
print('\nDEPARTURES_TOP10=')
for c,v in dep:
    print(f"{c}\t{v}")
