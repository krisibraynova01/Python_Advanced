text = input()
dict = {}

for el in text:
    dict[el] = text.count(el)

sorted_dict = sorted(dict.items())
for char, count_times in sorted_dict:
    print(f"{char}: {count_times} time/s")