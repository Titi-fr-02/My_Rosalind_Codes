n = int(input("Enter the number of months: "))
m = int(input("Enter the lifespan of rabbits: "))

litter = [1]
rabbits_babies = [0]
rabbits_mature = []
month = 1
d = 0

for i in range(1, n + 1):
    a = litter.pop(0)
    b = rabbits_babies.pop(0)
    rabbits_babies.append(a)
    rabbits_mature.append(b)
    if i > m - 1:
        d += rabbits_mature.pop(0)
    litter.append(sum(rabbits_mature))
    month += 1

rabbits = rabbits_babies + rabbits_mature
total_rabbits = sum(rabbits)
print(total_rabbits)