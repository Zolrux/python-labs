import random

def output_matrix(matrix: list):
    print('-' * len(str(matrix[0]).strip().replace(",", "")))
    for row in matrix:
         str_lst = str(row).strip().replace(",", "")
         for el in row:
            print(el, end="|")
         print(f"\n{'-' * len(str_lst)}")


def init_same_el_list(matrix: list):
    info = {}

    for i in range(len(matrix)):
        key_dict = f"row_{i}"
        info[key_dict] = {}
        for el in matrix[i]:
            key = f"el_{el}"
            count = matrix[i].count(el)
            if count > 1 and key not in info[key_dict]:
                info[key_dict][key] = count
    return list(info.values())

def get_same_counters(lst: list):
    count_same_lst = []
    for dct in lst:
        if isinstance(dct, dict):
            count = len(list(dct.keys()))
            count_same_lst.append(count)
            
    return count_same_lst

matrix = []

row_len = random.randint(5, 8)
col_len = random.randint(5, 8)

for i in range(row_len):
    matrix.append([])
    for j in range(col_len):
        matrix[i].append(random.randint(0, 9))

output_matrix(matrix)

same_lst = init_same_el_list(matrix)
same_lst_dct = get_same_counters(same_lst)

print("\nКоличество повторяющихся элементов в строках:")

min_el = same_lst_dct[0]

for el in same_lst_dct:
    print(el, end = "|")
    if el > 0 and el < min_el:
        min_el = el

min_count_duplicates_row = same_lst_dct.index(min_el)

print(f"\n\nНомер строки (начиная с 0): {min_count_duplicates_row}")