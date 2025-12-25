file_path = input("Enter the file path: ")
complement_table = str.maketrans('ATCG', 'TAGC')

with open(file_path, 'r') as file:
    sequence = file.read().replace('\n', '')
    reverse_complement = sequence.translate(complement_table)[::-1]

print(reverse_complement)