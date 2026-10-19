def read_rows(lines: list[str]) -> list[dict]:
    result = []
    headers = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = line.split(",")
        fields = [field.strip() for field in fields]
        if headers is None:
            headers = fields
            continue
        if len(fields) != len(headers):
            continue
        row = dict(zip(headers, fields))
        result.append(row)
    return result
def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1
    return counts
def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row["тип"] == kind:
            value = row["минуты"].replace(",", ".")
            try:
                minutes = float(value)
                total += minutes
            except ValueError:
                continue
    return round(total, 1)
def to_csv(counts: dict) -> str:
    result = "тип,количество\n"
    for kind in sorted(counts):
        result += kind + "," + str(counts[kind]) + "\n"
    return result