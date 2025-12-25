from My_functions import read_fasta_file

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

fasta_dic = read_fasta_file(file_path)

string_s1 = list(fasta_dic.values())[0]
string_s2 = list(fasta_dic.values())[1]

Transitions_table = {
    "A": ["G"],
    "G": ["A"],
    "C": ["T"],
    "T": ["C"]
}

Transversions_table = {
    "A": ["C", "T"],
    "G": ["C", "T"],
    "C": ["A", "G"],
    "T": ["A", "G"]
}

Transitions_count = 0
Transversions_count = 0

for i in range(len(string_s1)):
    if string_s1[i] == string_s2[i]:
        continue
    if string_s2[i] in Transitions_table[string_s1[i]]:
        Transitions_count += 1
    if string_s2[i] in Transversions_table[string_s1[i]]:
        Transversions_count += 1

print(f"The transition/transversion ratio is: {Transitions_count/Transversions_count}")