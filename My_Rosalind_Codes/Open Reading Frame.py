import pyperclip
from aa_table import CODON_TABLE

file_path = input("Enter the file path: ").replace('"', '')
ID = ""
sequence = ""

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            ID += line
        else:
            sequence += line

complement_table = str.maketrans('ATCG', 'TAGC')
reverse_complement = sequence.translate(complement_table)[::-1]
mRNA_sequence = sequence.replace('T', 'U')
mRNA_reverse_complement = reverse_complement.replace('T', 'U')

def extract_orfs(mrna_seq):
    start_codon = "AUG"
    stop_codons = {"UAA", "UAG", "UGA"}
    orfs = []

    for offset in range(3):
        for i in range(offset, len(mrna_seq) - 2, 3):
            frame = mrna_seq[i:i + 3]
            if frame == start_codon:
                codon_list = []
                for j in range(i, len(mrna_seq) - 2, 3):
                    current_codon = mrna_seq[j:j + 3]
                    if current_codon in stop_codons:
                        break
                    codon_list.append(current_codon)
                if codon_list:
                    orfs.append("".join(codon_list))
    return orfs

all_orfs = extract_orfs(mRNA_sequence) + extract_orfs(mRNA_reverse_complement)

protein_encoded = []
for mRNA in all_orfs:
    protein = ""
    for b in range(0, len(mRNA) - 2, 3):
        codon = mRNA[b:b + 3]
        aa = CODON_TABLE.get(codon, '')
        if aa == '':
            break
        protein += aa
    if protein.startswith('M'):
        protein_encoded.append(protein)

unique_proteins = sorted(set(protein_encoded))
pyperclip.copy("\n".join(unique_proteins))
print("Result copied to clipboard")