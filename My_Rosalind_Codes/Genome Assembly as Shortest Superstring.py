import pyperclip
import My_functions
file_path = input("Enter file path: ").replace('"', '')
n = 10 #number of nod retained after filtration
fasta_dict = My_functions.read_fasta_file(file_path)
overlap_dict = {}
for keyA, valueA in fasta_dict.items():
    temporary_overlap_dict = {}
    for keyB, valueB in fasta_dict.items():
        if keyA != keyB and valueA != valueB:
            seqA = valueA
            seqB = valueB
            overlap_start = My_functions.find_overlap_start(seqA, seqB)
            overlap_end = My_functions.find_overlap_end(seqA, seqB)
            if overlap_start >= min(len(seqA), len(seqB))/2:
                temporary_overlap_dict[seqA, seqB] = overlap_start
            elif overlap_end >= min(len(seqA), len(seqB))/2:
                temporary_overlap_dict[seqB, seqA] = overlap_end
    sorted_overlaps = sorted(temporary_overlap_dict.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_overlaps[:n]:
        overlap_dict[key] = value

sorted_overlaps = sorted(overlap_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_overlaps)
seqA, seqB = sorted_overlaps[0][0]
DNA = seqA + My_functions.building_DNA_end(seqB, seqA)
last_added_front = seqA
last_added_end = seqB

loop = True
while loop:
    score, candidates, next_candidates = {}, {}, {}
    for (key0, key1), value1 in overlap_dict.items():
        if last_added_end == key0 and key1 not in DNA:
            candidates[key0, key1] = value1
            score[key0, key1] = value1
    if candidates:
        for (key0, key1), value1 in candidates.items():
            for (keyLink, key2), value2 in overlap_dict.items():
                if key1 == keyLink and key2 not in DNA and key2 != key0:
                    next_candidates[key0, key1, key2] = value1 + value2
                    score[key0, key1, key2] = value1 + value2
    if next_candidates:
        for (key0, key1, key2), value_t in next_candidates.items():
            for (keyLink, key3), value3 in overlap_dict.items():
                if key2 == keyLink and key3 not in DNA and key3 != key1:
                    score[key0, key1, key2, key3] = value_t + value3
    if score:
        sorted_candidates = sorted(score.items(), key=lambda x: x[1], reverse=True)
        key = sorted_candidates[0][0]
        DNA += My_functions.building_DNA_end(key[1], DNA)
        last_added_end = key[1]
        score, candidates, next_candidates = {}, {}, {}
        if len(DNA) >= 30000:
            print("🛑 Reached 30kb limit — stopping assembly.")
            loop = False
        continue

    for (key_1, key0), value1 in overlap_dict.items():
        if key0 == last_added_front and key_1 not in DNA:
            candidates[key_1, key0] = value1
            score[key_1, key0] = value1
    if candidates:
        for (key_1, key0), value1 in candidates.items():
            for (key_2, keyLink), value2 in overlap_dict.items():
                if keyLink == key_1 and key_2 not in DNA and key_2 != key0:
                    next_candidates[key_2, key_1, key0] = value1 + value2
                    score[key_2, key_1, key0] = value1 + value2
    if next_candidates:
        for (key_2, key_1, key0), value_t in next_candidates.items():
            for (key_3, keyLink), value3 in overlap_dict.items():
                if keyLink == key_2 and key_3 not in DNA and key_3 != key_1:
                    score[key_3, key_2, key_1, key0] = value_t + value3
    if score:
        sorted_candidates = sorted(score.items(), key=lambda x: x[1], reverse=True)
        key = sorted_candidates[0][0]
        candidate = My_functions.building_DNA_upfront(key[-2], DNA)
        DNA, last_added_front = candidate + DNA, key[-2]
        score, candidates, next_candidates = {}, {}, {}
        if len(DNA) >= 30000:
            print("🛑 Reached 30kb limit — stopping assembly.")
            loop = False
    else:
        loop = False

print(DNA)
pyperclip.copy(DNA)
print(f"Final DNA is {len(DNA)} bp")

GAS = sum(1 for value in fasta_dict.values() if value in DNA)
print(f"GAS: {GAS}/{len(fasta_dict)}")