import numpy as np

hours = np.arange(0, 22, 3)
print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

line = np.linspace(0, 1, 5)
print(line)

zeros = np.zeros(6, dtype=int)
print(zeros)

unknown_table = np.full((2, 3), -1)
print(unknown_table)

identity = np.eye(3, dtype=int)
print(identity)

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures)
print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)

print(temperatures[1, 2])
print(temperatures[0])
print(temperatures[:, -1])
print(temperatures[:2, 1:])
print(temperatures[0:2, 1:3])

matrix = np.arange(1, 26).reshape(5, 5)
print(matrix)

first_three_rows = matrix[:3, :]
print(first_three_rows)
print(first_three_rows.shape)

last_two_rows = matrix[-2:, :]
print(last_two_rows)
print(last_two_rows.shape)

first_two_columns = matrix[:, :2]
print(first_two_columns)
print(first_two_columns.shape)

middle_block = matrix[1:4, 2:5]
print(middle_block)
print(middle_block.shape)

bottom_right = matrix[-2:, -2:]
print(bottom_right)
print(bottom_right.shape)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print(vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print(small_matrix)

# copy() создаёт независимую копию массива, поэтому изменения не затрагивают исходный hours.
changed_hours = hours.copy()
print(changed_hours)

changed_hours[2:5] = 99
print(changed_hours)

changed_hours[::2] = -1
print(changed_hours)
print(hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print(changed_matrix)
print(matrix)

numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = table.T

print(numbers)
print(table)
print(transposed)

print(numbers.shape)
print(table.shape)
print(transposed.shape)
# reshape(3, 4) работает, потому что в массиве 12 элементов, а 3 * 4 = 12.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15, а в исходном массиве только 12 элементов.