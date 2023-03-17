import random

def output_list(lst):
	print('[', end=" ")
	for el in lst:
		print(el, end=", ")
	print(']')

def delete_elements(lst: list, new_num):
	if lst[0] < new_num:
		lst.pop(0)
	if lst[len(lst) - 1] < new_num:
		lst.pop(len(lst) - 1)
	return lst

lst = []

for i in range(10):
	lst.append(random.randint(-5, 25))

print(f"Начальный список: {lst}")

data = input("Введите через запятую число и номер позиции: ")
num = int(data.split(",")[0])
pos = int(data.split(",")[1])

lst.insert(pos, num)

print(f"Список после добавленного числа: {lst}")

lst = delete_elements(lst, num)

print(f"Список после возможных удалений элементов: {lst}")