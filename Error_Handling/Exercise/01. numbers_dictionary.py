numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f"The variable number must be an integer")  # Display error message if input is not an integer

    line = input()

line = input()

while line != "Remove":
    searched = line

    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print(f"Number does not exist in dictionary")  # Display error message if key does not exist

    line = input()

line = input()

while line != "End":
    searched = line

    try:
        del numbers_dictionary[searched]
    except KeyError:
        print(f"Number does not exist in dictionary")  # Display error message if key does not exist

    line = input()

print(numbers_dictionary)
