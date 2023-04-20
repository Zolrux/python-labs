import random

def create_rand_lst():
    lst = []
    for j in range(10):
        num = random.randint(0, 10)
        lst.append(num)
    return lst


def output_intersection(sets: dict):
    res = sets["set_1"]
    for key in sets:
        if key != "set_1":
            res = res.intersection(sets[key])
    print(f"\nПересечение всех множеств: {res}")
    print(f"Количество элементов: {len(res)}")


def output_union(sets: dict):
    res = sets["set_1"]
    for key in sets:
        if key != "set_1":
            res = res.union(sets[key])
    print(f"\nОбъединение всех множеств: {res}")
    print(f"Количество элементов: {len(res)}")


sets = {}

for i in range(1, 4):
    sets[f"set_{i}"] = set(create_rand_lst())
    print(f"Множество №{i}: {sets[f'set_{i}']}")

output_intersection(sets)
output_union(sets)