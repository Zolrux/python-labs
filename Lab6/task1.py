import random

def output_matrix(matrix: list):
    print('―' * len(str(matrix[0]).strip().replace(",", "")))
    for row in matrix:
         str_lst = str(row).strip().replace(",", "")
         for el in row:
            print(el, end="|")
         print(f"\n{'―' * len(str_lst)}")

def init_same_el_list(matrix: list):
    same_el_list = []

    for i in range(len(matrix)):
        counter_duplicates = 0
        row_duplicates = set(matrix[i])
        if len(matrix[i]) != len(row_duplicates):
            counter_duplicates = len(matrix[i]) - len(row_duplicates)
            same_el_list.append(counter_duplicates)
        else:
            same_el_list.append(0)

    return same_el_list

matrix = []

row_len = random.randint(5, 10)
col_len = random.randint(5, 10)

for i in range(row_len):
    matrix.append([])
    for j in range(col_len):
        matrix[i].append(random.randint(1, 5))

output_matrix(matrix)

same_lst = init_same_el_list(matrix)

print("\nКоличество повторяющихся элементов в строках:")

for el in same_lst:
    print(el, end = "|")

min_count_duplicates_row = same_lst.index(min(same_lst))

print(f"\n\nНомер строки (начиная с 0): {min_count_duplicates_row}")