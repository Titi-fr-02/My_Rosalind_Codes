file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

id = ""
seq = ""
k = 3
fasta_dict = {}

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            if seq != "":
                fasta_dict[id] = seq
                seq = ""
            line = line.replace('>', "")
            id = line
        else:
            seq += line
if seq != "":
    fasta_dict[id] = seq

fasta_dict_comparison = fasta_dict.copy()
pairs = ""

for id in fasta_dict:
    compareA = fasta_dict.get(id)
    for v in fasta_dict_comparison:
        compareB = fasta_dict_comparison.get(v)
        if compareA != compareB:
            suffix = fasta_dict[id][-k:]
            prefix = fasta_dict[v][:k:]
            if suffix == prefix:
                pairs += f"{id} {v}\n"
        else:
            pass
print(pairs)