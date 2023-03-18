def output_matrix(matrix: list):
    print('-' * len(str(matrix[0]).strip().replace(",", "")))
    for row in matrix:
         str_lst = str(row).strip().replace(",", "")
         for el in row:
            print(el, end="|")
         print(f"\n{'-' * len(str_lst)}")

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

matrix = [[1, 1, 1, 3], [4, 6, 2, 6], [8, 8, 4, 8], [2, 2, 2, 2]]

output_matrix(matrix)

same_lst = init_same_el_list(matrix)

print("\nКоличество повторяющихся элементов в строках:")

for el in same_lst:
    print(el, end = "|")

min_count_duplicates_row = same_lst.index(min(same_lst))

print(f"\n\nНомер строки (начиная с 0): {min_count_duplicates_row}")