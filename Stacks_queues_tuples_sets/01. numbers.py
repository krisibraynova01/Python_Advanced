first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    action = first_command + ' ' + second_command

    if action == 'Add First':
        [first_sequence.add(int(x)) for x in data]
    elif action == 'Add Second':
        [second_sequence.add(int(x)) for x in data]
    elif action == 'Remove First':
        [first_sequence.discard(int(x)) for x in data]
    elif action == 'Remove Second':
        [second_sequence.discard(int(x)) for x in data]
    elif action == 'Check Subset':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(*sorted(first_sequence), sep = ', ')
print(*sorted(second_sequence), sep = ', ')