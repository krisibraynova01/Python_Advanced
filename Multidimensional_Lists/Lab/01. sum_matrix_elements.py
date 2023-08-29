def get_matrix():

    matrix = []

    rows, columns = map(int, input().split(', '))

    for row in range(rows):
        row_data = list(map(int, input().split(', ')))
        matrix.append(row_data)

    return matrix

curr_matrix = get_matrix()
sum = sum([sum(el) for el in curr_matrix])
print(sum)
print(curr_matrix)

