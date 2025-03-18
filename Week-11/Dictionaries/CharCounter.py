def main():
    word = "apple"

    charCount = {}

    for char in word:
        if char in charCount:
            print("Operation")
            charCount[char] += 1
        else:
            print("Operation")
            charCount[char] = 1

    print(charCount)

if __name__ == "__main__":
    main()