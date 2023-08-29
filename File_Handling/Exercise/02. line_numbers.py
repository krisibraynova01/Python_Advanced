from string import punctuation

with open("../files/text_line_numbers.txt", "r") as file:
    lines = file.readlines()

output_file = open("../files/output.txt", "w")

for i in range(len(lines)):
    letters, marks = 0, 0

    for symbol in lines[i]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(lines[i][:-1])} ({letters}) ({marks})\n")

output_file.close()