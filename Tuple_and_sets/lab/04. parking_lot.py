n = int(input())
cars = set()
for _ in range(n):
    data = input().split(', ')
    direction = data[0]
    cars_number = data[1]

    if direction == 'IN':
        cars.add(cars_number)
    else:
        cars.discard(cars_number)


if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
