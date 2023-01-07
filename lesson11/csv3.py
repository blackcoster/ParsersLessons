import csv

filename = "test3.csv"
# список покупок
shop_list = {"картофель": [2, 100], "яблоки": [3, 250], "морковь": [1, 35]}

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
   writer.writeheader()  # Записывает заголовки в файл
   for name, values in sorted(shop_list.items()):
       writer.writerow(dict(name=name, weight=values[0], price=values[1]))

# Чтение файла
rows = []
with open(filename, "r", encoding="utf-8") as file:
   reader = csv.DictReader(file)
   rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк

for row in rows:
   print(row)
