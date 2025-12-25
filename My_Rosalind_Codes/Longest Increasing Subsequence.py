file_path = input("Enter file path: ")
file_path = file_path.replace('"', '')
with open(file_path, 'r') as file:
    lines = file.read().splitlines()
    n = int(lines[0])
    sequence = list(map(int, lines[1].split()))

print(sequence)

lis = [[] for _ in range(n)]
lds = [[] for _ in range(n)]

for i in range(n):
    for j in range(i):

        if sequence[j] < sequence[i] and len(lis[j]) > len(lis[i]):
            lis[i] = lis[j][:]

        if sequence[j] > sequence[i] and len(lds[j]) > len(lds[i]):
            lds[i] = lds[j][:]

    lis[i].append(sequence[i])
    lds[i].append(sequence[i])

longest_inc = max(lis, key=len)
longest_dec = max(lds, key=len)

print(*longest_inc)
print(*longest_dec)