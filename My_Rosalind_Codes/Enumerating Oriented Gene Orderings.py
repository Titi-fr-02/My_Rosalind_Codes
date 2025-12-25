import itertools

file_path = input("Enter file path: ")
file_path = file_path.replace('"', '')
with open(file_path, 'r') as file:
    n = int(file.read().strip())
string_list = list(range(1, n + 1))
result = []

for i in itertools.permutations(string_list):
    for r in itertools.product([-1, 1], repeat=n):
        signed_perm = [a * s for a, s in zip(i, r)]
        result.append(signed_perm)

with open(file_path, 'w') as file:
    file.write(str(len(result)) + "\n")
    for A in result:
        file.write(" ".join(map(str, A)) + "\n")
print("Output saved in file")