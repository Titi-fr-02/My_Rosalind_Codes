file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

with open(file_path, "r") as file:
    s = file.readline().strip()
    t = file.readline().strip()

distance = 0
for i in range(len(s)):
    if s[i] != t[i]:
        distance += 1

print(distance)