def main():
    fahrenheit = input("Enter a temperature in Fahrenheit: ")

    match fahrenheit:
        case fahrenheit if fahrenheit >= 100:
            print("Stay inside")
        case fahrenheit if fahrenheit >= 90:
            print("Be careful due to heat")
        case fahrenheit if fahrenheit >= 80:
            print("It is hot, but not extreme")
        case fahrenheit if fahrenheit >= 70:
            print("Pack a picnic")
        case _:
            print("Take a jacket")

if __name__ == "__main__":
    main()