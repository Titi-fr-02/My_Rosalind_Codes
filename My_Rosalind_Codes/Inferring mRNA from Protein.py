import pyperclip
from aa_table import REVERSE_CODON_TABLE

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

with open(file_path, 'r') as file:
    prot_string = file.read()

total_possibilities = 1

for i in prot_string:
    if i in REVERSE_CODON_TABLE:
        total_possibilities *= REVERSE_CODON_TABLE[i]

total_possibilities *= 3 # Stop codon

pyperclip.copy(total_possibilities % 1000000)
print(f"copied to clipboard; \n{total_possibilities % 1000000}")