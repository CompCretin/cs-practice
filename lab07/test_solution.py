from solution import reshape_rows, block, column_means, column_range

assert reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3) == [
    [12.0, 14.5, 11.0],
    [13.0, 15.5, 10.5]
]
assert reshape_rows([1, 2, 3, 4, 5], 2) == []

assert block(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [0, 2],
    [1, 2]
) == [[2.0, 3.0], [8.0, 9.0]]
assert block([], [0], [0]) == []

assert column_means([[1, 2], [3, 4], [5, 6]]) == [3.0, 4.0]
assert column_means([]) == []
assert column_means([[1], [2], [2]]) == [1.666667]

assert column_range([[1, 2], [5, 7]], 1) == 5.0
assert column_range([], 0) == 0.0

print("Все проверки пройдены!")