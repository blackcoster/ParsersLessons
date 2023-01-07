import csv

filename = "test2.csv"

shop_list = {"картофель": [2, 100], "яблоки": [3, 250], "морковь": [1, 35]}

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as file:
   writer = csv.writer(file, quoting=csv.QUOTE_ALL)
   writer.writerow(["Наименование", "Вес", "Цена/кг."])  # Заголовки столбца
   for name, values in sorted(shop_list.items()):
       writer.writerow([name, *values])
   writer.writerow(["мука", "4", "70"])  # Допишем произвольную запись

# Чтение файла
rows = []
with open(filename, "r", encoding="utf-8") as file:
   reader = csv.reader(file)
   rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк

for row in rows:
   print(row)

