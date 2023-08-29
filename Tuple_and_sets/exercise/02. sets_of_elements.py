n_and_m = input().split()
n = int(n_and_m[0])
m = int(n_and_m[1])
set_n = set()
set_m = set()

for _ in range(n):
    number = int(input())
    set_n.add(number)

for _ in range(m):
    number = int(input())
    set_m.add(number)

both_sets = set_n & set_m

for set in both_sets:
    print(set)



