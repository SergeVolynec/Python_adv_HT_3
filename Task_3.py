""" Создайте словарь со списком вещей для похода в качестве ключа
 и их массой в качестве значения. Определите какие вещи влезут в рюкзак
  передав его максимальную грузоподъёмность.
   Достаточно вернуть один допустимый вариант."""

stuff = {"котелок": 2, "палатка": 5, "лопата": 1, "продукты": 7, "мангал": 2}
max_wght = int(input("Введите максимальный вес рюкзака: "))
total_wght = 0
backpack = []

for k, v in stuff.items():
    if total_wght + v < max_wght:
        backpack.append(k)
        total_wght += v
    elif total_wght + v == max_wght:
        backpack.append(k)
        total_wght += v
        break

print("Мы берем c собой:", *backpack, ". Полный вес рюкзака:", total_wght, "кг")