rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    cur_row = [int(x) for x in input().split()]
    matrix.append(cur_row)

result = []

for column in range(columns):
    column_sum = 0
    for row_index in range(rows):
        column_sum += matrix[row_index][column]
    result.append(column_sum)

[print(x) for x in result]





