n = int(input())
chemical_elements = set()

for _ in range(n):
    chemical_compound = input().split()
    [chemical_elements.add(el) for el in chemical_compound]

print(*chemical_elements, sep = '\n')
