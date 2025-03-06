def main():
    someString = input("Enter a string: ") # Hello

    stringLength = len(someString) # 4

    index = stringLength - 1 # 3

    # # 3, 2, 1, 0, -1
    while(index >= 0):
        print(someString[index], end="")
        index -= 1

if __name__ == "__main__":
    main()