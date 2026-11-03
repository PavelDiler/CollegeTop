sizeY = int(input())
sizeX = int(input())

for y in range(sizeY):
    for x in range(sizeX):
        if y == 0 or y == sizeY - 1 or x == 0 or x == sizeX - 1:
            print ("*", end=" ")
        else:
            print (" ", end=" ")
    print()