import itertools
import pyperclip

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

with open(file_path, 'r') as file:
    lines = file.read().splitlines()
    alphabet = lines[0].split()
    n = int(lines[1])

combinations = list(itertools.permutations(alphabet, n))
Output = ""
for i in itertools.product(alphabet, repeat=n):
    Output += f"\n{"".join(i)}"
pyperclip.copy(Output)
print("Output copied to clipboard :", Output)