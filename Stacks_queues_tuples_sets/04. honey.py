from collections import deque

def get_calculation(symbol, bees, nec):
    if symbol == '+':
        return bees + nec
    elif symbol == '-':
        return bees - nec
    elif symbol == '*':
        return bees * nec
    elif symbol == '/':
        return bees / nec

working_bees_deque = deque(int(x) for x in input().split())
nectar_stack = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0

while working_bees_deque and nectar_stack:
    bee, nectar = working_bees_deque.popleft(), nectar_stack.pop()
    if nectar > bee:
        result = get_calculation(symbols.popleft(), bee, nectar)
        total_honey += abs(result)
    else:
        working_bees_deque.appendleft(bee)

print(f"Total honey made: {total_honey}")
if working_bees_deque:
    print(f"Bees left: {', '.join(str(x) for x in working_bees_deque)}")
if nectar_stack:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_stack)}")


