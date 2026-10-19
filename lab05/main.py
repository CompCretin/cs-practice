from pathlib import Path
from tablestats import read_rows, count_types, total_minutes, to_csv

filename = input()
folder = Path(__file__).resolve().parent

with open(folder / filename, encoding="utf-8") as table:
    rows = read_rows(table)

counts = count_types(rows)
minutes = total_minutes(rows, "ошибка")

print(len(rows))
print(len(counts))
print(minutes)

with open(folder / "summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))