def main():
    word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz".lower()

    charCount = []

    for x in range(26):
        charCount.append(0)

    for char in word:
        if char == 'a':
            charCount[0] += 1
            print("Operation")
        elif char == 'b':
            charCount[1] += 1
            print("Operation")
        elif char == 'c':
            charCount[2] += 1
            print("Operation")
        elif char == 'd':
            charCount[3] += 1
            print("Operation")
        elif char == 'e':
            charCount[4] += 1
            print("Operation")
        elif char == 'f':
            charCount[5] += 1
            print("Operation")
        elif char == 'g':
            charCount[6] += 1
            print("Operation")
        elif char == 'h':
            charCount[7] += 1
            print("Operation")
        elif char == 'i':
            charCount[8] += 1
            print("Operation")
        elif char == 'j':
            charCount[9] += 1
            print("Operation")
        elif char == 'k':
            charCount[10] += 1
            print("Operation")
        elif char == 'l':
            charCount[11] += 1
            print("Operation")
        elif char == 'm':
            charCount[12] += 1
            print("Operation")
        elif char == 'n':   
            charCount[13] += 1
            print("Operation")
        elif char == 'o':
            charCount[14] += 1
            print("Operation")
        elif char == 'p':
            charCount[15] += 1
            print("Operation")
        elif char == 'q':
            charCount[16] += 1
            print("Operation")
        elif char == 'r':
            charCount[17] += 1
            print("Operation")
        elif char == 's':
            charCount[18] += 1
            print("Operation")
        elif char == 't':
            print("Operation")
            charCount[19] += 1
        elif char == 'u':
            print("Operation")
            charCount[20] += 1
        elif char == 'v':
            print("Operation")
            charCount[21] += 1
        elif char == 'w':
            charCount[22] += 1
            print("Operation")
        elif char == 'x':
            charCount[23] += 1
            print("Operation")
        elif char == 'y':
            charCount[24] += 1
            print("Operation")
        elif char == 'z':
            charCount[25] += 1
            print("Operation")

    print(charCount)

if __name__ == "__main__":
    main()