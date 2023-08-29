n = int(input())
names = set()

for _ in range(n):
    name = input()
    names.add(name)

for person in names:
    print(person)