def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input("напишите кол-во строк матрицы:"))
m = int(input("напишите кол-во столбцов матрицы:"))
value = input(f'напишите значения матрицы:')
print('-------' * m)
matrix = get_matrix(n, m, value)
if n <= 0:
    print("написано неверное количество строк:", n)
elif m <=0:
    print("написано неверное количество столбцов:" ,m)
else:
    print("матрица:")
    for i in matrix:
        print(*i)