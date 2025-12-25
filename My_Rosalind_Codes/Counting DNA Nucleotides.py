file_path = input("Enter the file path: ")
Nucleotides_occurences = {}
with open(file_path, 'r') as file:
    sequence = file.read().replace('\n', '')
    letters = list(sequence)
    for letter in letters:
        if letter in Nucleotides_occurences:
            Nucleotides_occurences[letter] += 1
        else:
            Nucleotides_occurences[letter] = 1
for letter in sorted(Nucleotides_occurences):
    print(letter, Nucleotides_occurences[letter])
