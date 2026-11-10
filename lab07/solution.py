import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    a = np.asarray(values, dtype=float)
    a = a.reshape(-1, width)

    return a.tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    a = np.asarray(matrix, dtype=float)

    if a.size == 0 or len(rows) == 0:
        return []

    if len(columns) == 0:
        return [[] for _ in rows]

    return a[np.ix_(rows, columns)].tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    a = np.asarray(matrix, dtype=float)

    if a.size == 0:
        return []

    return np.round(a.mean(axis=0), 6).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    a = np.asarray(matrix, dtype=float)

    if a.size == 0:
        return 0.0

    values = a[:, column]
    return round(float(values.max() - values.min()), 6)