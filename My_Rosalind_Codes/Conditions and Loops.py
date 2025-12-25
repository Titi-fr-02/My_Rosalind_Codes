def main():
    a, b = map(int, input("Enter the waited integers a and b: ").split())
    somme = 0

    for i in range(a, b + 1):
        if i % 2 == 1:
            somme += i
    print(somme)

if __name__ == '__main__':
    main()