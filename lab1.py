# 1. Замена пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
average = sum(num for num in numbers if num is not None) / len([num for num in numbers])

numbers[numbers.index(None)] = average

print("Измененный список:", numbers)

# 2. Расчёт количества книг на дискете
# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mb = 1.44
pages_per_book = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4

disk_size_bytes = disk_size_mb * 1024 * 1024

symbols_per_book = pages_per_book * lines_per_page * symbols_per_line

book_size_bytes = symbols_per_book * bytes_per_symbol

books_on_disk = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))

# 3. Разделение игроков на две команды
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)
