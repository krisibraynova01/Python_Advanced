size = int(input())
matrix = []

for _ in range(size):
    cur_row = [int(x) for x in input().split()]
    matrix.append(cur_row)



def get_sum_of_primary_diagonal(matrix):
    sum_of_primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
    return sum(sum_of_primary_diagonal)


result = get_sum_of_primary_diagonal(matrix)
print(result)


