matrix = []
for i in range(int(input())):
    current_row = [int(el) for el in input().split(', ')]
    matrix.append(current_row)

    flattering_matrix = [num for sublist in matrix for num in sublist]

print(flattering_matrix)


