import math
import pyperclip

file_path = input("Enter file path: ")
file_path = file_path.replace('"', '')
with open(file_path, 'r') as file:
    lines = file.readlines()
    s = lines[0].strip()
    A = [float(k) for k in lines[1].split()]

results = []
for r in A:
    prob = 1.0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "T":
            prob *= (1 - r) / 2
        elif s[i] == "G" or s[i] == "C":
            prob *= r / 2
    results.append(round(math.log10(prob), 3))

results_print = " ".join(map(str, results))
print(results_print)
pyperclip.copy(results_print)
