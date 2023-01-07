
import json

filename = "file.json"

info = {
   "ФИО": "Иванов Иван Иванович",
   "Оценки": {
       "Математика": 4,
       "Физика": 5,
       "Информатика": 5
   },
   "Хобби": ["Программирование", "Плавание"],
   "Возраст": 14,
   "ДомЖивотные": None
}

# Запись структуры в файл в JSON-формате
with open(filename, "w", encoding="utf-8") as file:
   file.write(json.dumps(info, ensure_ascii=False, indent=4))

# Чтение из файла JSON-формата
info_2 = []
with open(filename, encoding="utf-8") as file:
   info_2 = json.loads(file.read())

print(info_2)

