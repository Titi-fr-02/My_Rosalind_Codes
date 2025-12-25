from aa_table import CODON_TABLE

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')
with open(file_path, 'r') as file:
    rna = file.read().replace('\n', '')

protein = ""

for i in range(0, len(rna) - 2, 3):
    codon = rna[i:i+3]
    aa = CODON_TABLE.get(codon, '')
    if aa == '':
        break  # Stop codon
    protein += aa

print(protein)

