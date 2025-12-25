def main():
    s = input("Enter the string s: ")
    a, b, c, d = map(int, input("Enter the waited integers a b c d: ").split())

    first_slice = s[a:b + 1]
    second_slice = s[c:d + 1]

    print(first_slice, second_slice)

if __name__ == '__main__':
    main()