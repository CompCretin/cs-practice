threshold = float(input())
n = int(input())
errors = 0
above = 0
total = 0
maximum = None
valid = 0
for i in range(n):
    value = input()
    if value == "error":
        errors = errors + 1
        continue
    temperature = float(value)
    valid = valid + 1
    total = total + temperature
    if maximum is None or temperature > maximum:
        maximum = temperature
    if temperature > threshold:
        above = above + 1
if valid > 0:
    average = total / valid
else:
    average = 0
print(n)
print(errors)
print(above)
print(maximum)
print(average)