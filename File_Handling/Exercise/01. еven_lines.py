symbols = ["-", ",", ".", "!", "?"]

with open("../files/text.txt", "r") as file:
    lines = file.readlines()


for row in range(0, len(lines), 2):

    for symbol in symbols:
        lines[row] = lines[row].replace(symbol, "@")

    print(*lines[row].split()[::-1], sep=" ")
