import math

def partial_permutations(n, k):
    return math.factorial(n) // math.factorial(n-k)

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')
with open(file_path, 'r') as file:
    line = file.read().strip()
    n, k = map(int, line.split())

print(partial_permutations(n, k) % 1000000)
