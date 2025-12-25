#My_functions.py

def read_fasta_file(file):
    fasta_dict = {}
    ID = ""
    seq = ""
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq != "":
                    fasta_dict[ID] = seq
                    seq = ""
                line = line.replace('>', "")
                ID = line
            else:
                seq += line
    if seq != "":
        fasta_dict[ID] = seq
    return fasta_dict

def find_overlap_end(seqA, seqB):
    max_overlap_end = 0
    for t in range(1, min(len(seqA), len(seqB)) + 1):
        if seqB.endswith(seqA[:t]):
            max_overlap_end = t
    return max_overlap_end

def find_overlap_start(seqA, seqB):
    max_overlap_start = 0
    for v in range(len(seqA)):
        if seqB.startswith(seqA[v:]):
            max_overlap_start = len(seqA[v:])
    return max_overlap_start

def building_DNA_end(seq, DNA):
    if DNA == "":
        return seq
    else:
        max_overlap = 0
        for t in range(1, len(seq) + 1):
            if DNA.endswith(seq[:t]):
                max_overlap = t
        return seq[max_overlap:]

def building_DNA_upfront(seq, DNA):
    if DNA == "":
        return seq
    for v in range(len(seq)):
        if DNA.startswith(seq[v:]):
            return seq[:v]
    return None