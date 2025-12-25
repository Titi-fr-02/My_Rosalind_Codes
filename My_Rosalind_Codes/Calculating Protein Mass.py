import pyperclip
from aa_table import aa_weight
file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

with open(file_path, 'r') as file:
    protein = file.read()

protein_weight = []

for aa in protein:
    if aa in aa_weight:
        protein_weight.append(aa_weight[aa])

pyperclip.copy(sum(protein_weight))
print("Result copied to clipboard")