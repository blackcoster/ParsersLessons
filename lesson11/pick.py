import pickle

filename = "test.txt"

shop_list = {"овощи": ["картофель", "капуста"],
           "бакалея": ["мука"],
           "бюджет": 500}

# Запись в файл
with open(filename, "wb") as file:
   pickle.dump(shop_list, file)  # помещаем объект в файл

# Считываем из хранилища
shop_list_2 = []
with open(filename, "rb") as file:
   shop_list_2 = pickle.load(file)  # загружаем объект из файла
print(shop_list_2)
