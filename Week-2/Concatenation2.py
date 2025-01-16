def main():
    intNumber = 123
    floatNumber = 3.14
    text1 = "Hello"
    text2 = "World"
    fullText = "Hello " + "World " + str(intNumber)
    print(text1 + " " + text2 + " " + str(123))
    print(text1 + " world " + str(floatNumber))
    print(fullText)

if __name__ == "__main__":
    main()