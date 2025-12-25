file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

Dominant_chance = [1, 1, 1, 0.75, 0.5, 0]
Genotypes = ['AA_AA', 'AA_Aa', 'AA_aa', 'Aa_Aa', 'Aa_aa', 'aa_aa']
Genotypes_dominance_chances = dict(zip(Genotypes, Dominant_chance))
k = 2 #number of offsprings per pairs

with open(file_path) as file:
    proportion = file.read().split()
    Pop_proportion = dict(zip(Genotypes, [float(x) for x in proportion]))

offsprings = []

for i in Pop_proportion:
    a = Pop_proportion[i]
    b = Genotypes_dominance_chances[i]
    offspring = a * b * 2
    offsprings.append(offspring)

result = sum(offsprings)

print(result)
