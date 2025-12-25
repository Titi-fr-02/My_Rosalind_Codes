from My_functions import read_fasta_file
import pyperclip

file_path = input("Enter file path: ")
file_path = file_path.replace('"', '')

fasta_dic = read_fasta_file(file_path)

string_s = list(fasta_dic.values())[0]
string_t = list(fasta_dic.values())[1]

Coordinates = []
pos = 0

for i in range(len(string_s)):
    if pos > len(string_t) - 1:
        break
    if string_s[i] == string_t[pos]:
        Coordinates.append(f"{i + 1}")
        pos += 1
    else:
        pass

print(' '.join(Coordinates))
pyperclip.copy(' '.join(Coordinates))