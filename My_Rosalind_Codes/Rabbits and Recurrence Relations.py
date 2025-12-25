n = int(input("Enter the number of months: "))
k = int(input("Enter the number of rabbits per litter: "))
if n <= 2:
    Result = 1
else:
    a, b = 1, 1
    for n in range(3, n + 1):
        a, b = b, b + a * k
    result = b

print(b)