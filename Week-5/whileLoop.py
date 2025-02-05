def main():
    number = 3

    guess = 0

    while guess != number:
        guess = int(input("Guess number between 1 to 10: "))

        if guess != number:
            print("Incorrect, try again!")
        
        print()

    print(f"Correct guess! the number was {number}")

if __name__ == "__main__":
    main()