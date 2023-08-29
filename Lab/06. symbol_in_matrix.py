def check_special_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            curr_el = matrix[row][col]
            if symbol == curr_el:
                return row, col

def print_func(data, symbol):
    if data:
        print(data)
    else:
        print(f"{symbol} does not occur in the matrix")


size = int(input())
matrix = []

for _ in range(size):
    cur_row = input()
    matrix.append(cur_row)

spec_symbol = input()

print_func(check_special_symbol(matrix, spec_symbol), spec_symbol)