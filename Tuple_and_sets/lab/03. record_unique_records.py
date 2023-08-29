n = int(input())
unique_records = set()
for _ in range(n):
    name = input()
    unique_records.add(name)

for person in unique_records:
    print(person)
