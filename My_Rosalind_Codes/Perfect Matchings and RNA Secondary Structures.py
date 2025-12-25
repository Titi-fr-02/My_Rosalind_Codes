import math
from My_functions import read_fasta_file

def number_perfect_matching(RNA):
    a, u, c, g = RNA.count('A'), RNA.count('U'), RNA.count('C'), RNA.count('G')
    if a == u and c == g:
        return math.factorial(a) * math.factorial(c)
    else:
        return 0

file_path = input("Enter file path: ").replace('"', '')
fasta_dict = read_fasta_file(file_path)

for key, value in fasta_dict.items():
    print(f"{key}: {number_perfect_matching(value)}")