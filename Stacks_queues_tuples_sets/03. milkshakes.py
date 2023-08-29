from collections import deque
milkshakes = 0

chocolate_stacks = deque(int(x) for x in input().split(', '))
milk_deque = deque(int(x) for x in input().split(', '))

while milkshakes != 5 and chocolate_stacks and milk_deque:
    chocolate = chocolate_stacks.pop()
    cup_of_milk = milk_deque.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        milk_deque.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolate_stacks.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        milk_deque.append(cup_of_milk)
        chocolate_stacks.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolate_stacks) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk_deque) or 'empty'}")






