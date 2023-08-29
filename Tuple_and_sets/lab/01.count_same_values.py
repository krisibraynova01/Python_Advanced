values = tuple(map(float, input().split()))
count_of_value = {value: values.count(value) for value in values}

for key, value in count_of_value.items():
    print(f"{key} - {value} times")