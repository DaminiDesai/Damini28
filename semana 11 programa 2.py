def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def sort_specific_row(matrix, row):
    sorted_row = matrix[row].copy()
    selection_sort(sorted_row)
    matrix[row] = sorted_row

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Matriz bidimensional de ejemplo
matrix = [
    [9, 2, 5],
    [7, 4, 8],
    [1, 3, 6]
]

print("Matriz original:")
print_matrix(matrix)

# Ordenar la fila específica (por ejemplo, la segunda fila, índice 1)
row_to_sort = 1
sort_specific_row(matrix, row_to_sort)

print("\nMatriz con la fila", row_to_sort, "ordenada:")
print_matrix(matrix)
