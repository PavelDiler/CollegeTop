num1 = int(input())
num2 = int(input())

n = 0

for  i in range(num1, num2 + 1):
    print(i)
print()

for  j in range(num2, num1 - 1, -1):
    print(j)    
print()

for g in range(num1, num2 + 1):
    if g % 7 == 0:
        print(g)
print()

for u in range(num1, num2 + 1):
    if u % 5 == 0:
        n += 1
print(n)