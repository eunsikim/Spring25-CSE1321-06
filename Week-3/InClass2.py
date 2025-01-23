def main():
    age = int(input("How old are you?: "))

    if age >= 18: # If age is greater than or equal to 18, then...
        print("You are elegible to vote.")
    else:
        print("You are not elegible to vote.")

if __name__ == "__main__":
    main()