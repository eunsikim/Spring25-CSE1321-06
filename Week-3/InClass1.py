def main():
    number = int(input("Enter a number: "))

    if number < 0 or number > 0:
        if number > 0:
            if number % 2 == 0:
                print("Your number is even.")
            else: # number % 2 == 1
                print("Your number is odd.")
        else: # number is < 0
            print("Your number is negative")
    else: # number == 0
        print("Your number is zero")

    if number > 0:
        if number % 2 == 0:
                print("Your number is even.")
        else:
                print("Your number is odd.")
    else: # number is either 0 or negative
        if number == 0:
            print("Your number is zero")
        else:
            print("Your number is negative")

if __name__ == "__main__":
    main()