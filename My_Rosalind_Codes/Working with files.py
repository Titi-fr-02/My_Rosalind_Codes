file_path = input('Enter your file path: ')
output_path = input('Enter your output file path: ')
if not output_path.endswith("\\"):
    output_path += "\\"
output_file = output_path + "output.txt"
even_lines = []

with open(file_path, 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if (i + 1) % 2 == 0:
        even_lines.append(line)

with open(output_file, 'w') as file:
    file.writelines(even_lines)

print(f'Your file has been saved to: {output_path}')