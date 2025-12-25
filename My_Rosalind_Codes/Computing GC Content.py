file_path = input("Enter file path: ")
file_path = file_path.replace('"', "")
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

gc_results = {}
for id, seq in fasta_dict.items():
    gc_count = seq.count('G') + seq.count('C')
    gc_content = (gc_count / len(seq)) * 100
    gc_results[id] = gc_content

higher_id = max(gc_results, key=gc_results.get)
higher_gc_content = gc_results[higher_id]
print(f"{higher_id} {higher_gc_content:.6f}%")