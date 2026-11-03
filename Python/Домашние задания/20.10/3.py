size = int(input())

for y in range(size):
    for x in range(size):
        if y == 0 or y == size - 1 or x == 0 or x == size -1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()        