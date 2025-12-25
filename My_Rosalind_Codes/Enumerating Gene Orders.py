import itertools
n = int(input("Enter the integer length: "))
items = list(range(1, n + 1))
output_2 = list(itertools.permutations(items))
output_1 = len(output_2)
print(output_1)
for perm in output_2:
    print(*perm)