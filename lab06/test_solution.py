from solution import count_items, unique_sorted, common, only_in_first

assert count_items(["ошибка", "запуск", "ошибка"]) == {"ошибка": 2, "запуск": 1}
assert count_items([]) == {}

assert unique_sorted([3, 1, 2, 1]) == [1, 2, 3]
assert unique_sorted([]) == []

assert common(["иванов", "петрова"], ["петрова", "котов"]) == ["петрова"]
assert common(["иванов"], ["котов"]) == []

assert only_in_first(["иванов", "петрова"], ["петрова"]) == ["иванов"]
assert only_in_first([], ["петрова"]) == []

print("Все проверки пройдены!")