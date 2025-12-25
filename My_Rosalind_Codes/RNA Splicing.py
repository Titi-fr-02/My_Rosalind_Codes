from aa_table import CODON_TABLE
import pyperclip

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

ID = ""
seq = ""
fasta_dict = {}

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if seq != "":
                fasta_dict[id] = seq
                seq = ""
            line = line.replace('>', "")
            id = line
        else:
            seq += line
if seq != "":
    fasta_dict[id] = seq

sequence = list(fasta_dict.values())[0]
actual_seq = sequence
for ID, substring in fasta_dict.items():
    if substring == sequence:
        pass
    else:
        actual_seq = actual_seq.replace(substring, '')

RNA = actual_seq.replace('T', 'U')

protein = ""
for i in range(0, len(RNA) - 2, 3):
    codon = RNA[i:i+3]
    aa = CODON_TABLE.get(codon, '')
    if aa == '':
        break
    protein += aa

print("Protein copied to clipboard :", protein)
pyperclip.copy(protein)