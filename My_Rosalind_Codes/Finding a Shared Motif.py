file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

id = ""
seq = ""
fasta_dict = {}
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if seq != "":
                fasta_dict[id] = seq
                seq = ""
            line = line.replace('>', "")
            id = line
        else :
            seq += line
if seq != "":
    fasta_dict[id] = seq

sequences = []

for i in fasta_dict.values():
    if i != seq:
        sequences.append(i)
    else:
        pass

reference_seq = list(fasta_dict.values())[0]
length = len(reference_seq)
other_seqs = [seq for seq in fasta_dict.values() if seq != reference_seq]
result = ""

for i in range(length, 2, -1):
    for base in range(0, length - i + 1):
        fragment = reference_seq[base:base + i]
        if all(fragment in q for q in other_seqs):
            result = fragment
            break
    if result:
        break

print(result)