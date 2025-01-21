def main():
    phone_battery = float(input("What is your phone battery percentage?: "))

    if phone_battery == 100:
        print("Your phone is fully charged")
    elif phone_battery > 50:
        print("Your phone is more than half charged")
    elif phone_battery > 30:
        print("You should look for a charger")
    elif phone_battery > 0:
        print("Your phone battery is critically low")
    else:
        print("Your phone does not have enough battery to function")

if __name__ == "__main__":
    main()