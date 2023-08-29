try:
    line = input()
    times = int(input())
    print(line * times)
except:
    print("Variable times must be an integer")