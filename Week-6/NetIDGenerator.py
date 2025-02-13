def main():
    first_name = input("Enter first name: ").lower()
    last_name = input("Enter last name: ").lower()

    first_letter = ""
    ln_letters = ""

    for c in first_name:
        first_letter = c
        break

    print(first_letter)

if __name__ == "__main__":
    main()