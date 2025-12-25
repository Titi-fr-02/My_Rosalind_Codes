file_path = input('Enter your file path: ')
Word_occurrences = {}
with open(file_path, 'r') as file:
    words = ' '.join(file.readlines()).split()
    for word in words:
        if word in Word_occurrences:
            Word_occurrences[word] += 1
        else:
            Word_occurrences[word] = 1

for word in sorted(Word_occurrences):
    print(f"{word} {Word_occurrences[word]}")
