matrix = []

for i in range(int(input())):
    current_row = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
    matrix.append(current_row)

print(matrix)





