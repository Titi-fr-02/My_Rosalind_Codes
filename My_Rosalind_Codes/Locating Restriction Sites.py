import pyperclip

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

sequence = ""
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if not line.startswith('>'):
            sequence += line

length = len(sequence)
complement_table = str.maketrans('ATCG', 'TAGC')
result = []

for l in range(4, 13):
    for i in range(length - l + 1):
        substring = sequence[i:i+l]
        reverse_seq = substring.translate(complement_table)[::-1]
        if substring == reverse_seq:
            result.append((i + 1, l))

print("Result copied to clipboard:")
print('\n'.join(f"{pos} {l}" for pos, l in result))
pyperclip.copy('\n'.join(f"{pos} {l}" for pos, l in result))