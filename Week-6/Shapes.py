def main():
    size = int(input("Enter a size: "))

    for i in range(size):
        for j in range(size):
            print(f"*", end="")
        print()

    print()
    stars = 1
    for i in range(size):
        for j in range(stars):
            print(f"*", end="")
        print()
        stars += 1

    print()

    s = size - 1 # Amount of spaces
    a = 1 # Amount of Asterisks
    for i in range(size):
        for j in range(s):
            print(f" ", end="")
        for j in range(a):
            print(f"*", end="")
        print()
        s -= 1
        a += 1

if __name__ == "__main__":
    main()