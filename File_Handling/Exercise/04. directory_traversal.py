import os


def save_files(directory_name, first_level=False):
    for filename in os.listdir(directory_name):
        file = os.path.join(directory_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_level:
            save_files(file, first_level=True)


directory = input()
extensions = {}
result = []

try:
    save_files(directory)
except FileNotFoundError:
    print(f"Not a valid directory")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")
    [result.append(f"- - - {file}") for file in sorted(files)]

with open("../files/report.txt", "w") as report_file:
    report_file.write("\n".join(result))