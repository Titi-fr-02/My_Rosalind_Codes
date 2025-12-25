file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')
output = []
with open(file_path, 'r') as file:
    lines = file.read().strip().splitlines()
    dna = lines[0].upper()
    motif = lines[1].upper()
    for i in range(0, len(dna) - len(motif) + 1):
        seq = dna[i:i+len(motif)]
        if seq == motif:
            output.append(i + 1)
    if not output:
        print("No motif found")
    else:
        pass
result = ' '.join(str(pos) for pos in output)
print(result)