"""Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов"""

lst = [1, 1, 1, 5, 4, 7, 7, 8, 9, 9, 10]

dic = {}
for item in lst:
    dic[item] = dic.get(item, 0) + 1

for k, v in dic.items():
    if v == 1:
        lst.remove(k)

print(list(set(lst)))

