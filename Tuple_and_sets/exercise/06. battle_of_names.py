odd_set = set()
even_set = set()

for row in range(1, int(input()) +1):
    sum_ascii_values = sum(ord(el) for el in input())

    if int(sum_ascii_values / row) % 2 == 0:
        even_set.add(int(sum_ascii_values / row))
    else:
        odd_set.add(int(sum_ascii_values / row))

if sum(odd_set) > sum(even_set):
    print(', '.join(str(l) for l in odd_set.difference(even_set)))
elif sum(odd_set) == sum(even_set):
    print(', '.join(str(l) for l in odd_set.union(even_set)))
else:
    print(', '.join(str(l) for l in odd_set.symmetric_difference(even_set)))






