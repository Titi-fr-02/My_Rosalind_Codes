file_path = input("Enter the file path: ")
DNA_sequence = ()

with open(file_path, 'r') as file:
    sequence = file.read().replace('\n', '').replace('T','U')

print(sequence)