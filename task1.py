# Напишите функцию для транспонирования матрицы
my_matrix = [[1, 2, 3], [4, 5, 6]]

def change_matrix(matrix:list[list[int]]) -> list[list[int]]:
    return list(zip(*matrix))

print(change_matrix(my_matrix))
            