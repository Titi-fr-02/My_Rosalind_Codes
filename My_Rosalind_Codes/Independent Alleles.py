from scipy.stats import binom

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

with open(file_path, "r") as file:
    file_data = file.read().split()

k, N = int(file_data[0]), int(file_data[1])
t_individuals, g_prob = 2**k, 0.25

prob = 1 - binom.cdf(N - 1, t_individuals, g_prob)

print(round(prob, 3))