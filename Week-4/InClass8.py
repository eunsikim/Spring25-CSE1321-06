def main():
    number1 = float(input("Enter a number: "))
    op = input("Enter an operation: ")
    number2 = float(input("Enter a number: "))

    match op:
        case "+":
            print(number1 + number2)
        case "-":
            print(number1 - number2)
        case "*":
            print(number1 * number2)
        case "/":
            print(number1 / number2)

if __name__ == "__main__":
    main()