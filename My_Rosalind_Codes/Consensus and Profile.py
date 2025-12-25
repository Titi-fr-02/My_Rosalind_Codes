file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')
id = ""
seq = ""
fasta_dict = {}
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if seq != "":
                fasta_dict[id] = seq
                seq = ""
            line = line.replace('>', '')
            id = line
        else :
            seq += line
if seq != "":
    fasta_dict[id] = seq

sequences = list(fasta_dict.values())
length = len(sequences[0])

profile = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
}

for i in range(length):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for seq in sequences:
        base = seq[i]
        counts[base] += 1
    for base in counts:
        profile[base].append(counts[base])

consensus = ""
for i in range(length):
    max_base = max(profile, key=lambda b: profile[b][i])
    consensus += max_base

print(consensus)
for base in profile:
    counts = ' '.join(str(n)
    for n in profile[base])
    print(f"{base}: {counts}")