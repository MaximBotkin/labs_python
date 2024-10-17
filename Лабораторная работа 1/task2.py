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
