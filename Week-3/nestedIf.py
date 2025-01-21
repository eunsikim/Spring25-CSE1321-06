def main():
    country = input("Enter your country of residence: ")

    if country == "US":
        age = int(input("How old are you?: "))

        if age >= 21:
            print("You are allowed to drink")
        else:
            print("You are not allowed to drink")
    else:
        print("Drinking laws unknown")

if __name__ == "__main__":
    main()
