k = int(input("Enter the number of homozygous dominant individuals: "))
m = int(input("Enter the number of heterozygous individuals: "))
n = int(input("Enter the number of homozygous recessive individuals: "))
T = k + m + n
total_pairs = T * (T - 1)

dominant_pairs = (
    k * (k - 1) +
    k * m +
    k * n +
    m * k +
    m * (m - 1) * 0.75 +
    m * n * 0.5 +
    n * k +
    n * m * 0.5
)

prob = dominant_pairs / total_pairs
print(f"{prob:.5f}")