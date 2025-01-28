def main():
    menuOrder = input("What would you like to order? ")

    match menuOrder:
        case "burger":
            print("You ordered a burger")
        case "fries":
            print("You ordered fries")
        case "drink":
            print("You ordered a drink")

if __name__ == "__main__":
    main()