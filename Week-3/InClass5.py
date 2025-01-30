def main():
    userChoice = input("What color is the traffic light: ")

    # Validate input
    if userChoice == "Green":
        print("Go")
    elif userChoice == "Red":
        print("Stop")
    elif userChoice == "Yellow":
        howClose = input("How close your are from the traffic light (Close/Far): ")
        if howClose == "Close":
            print("Proceed with caution")
        elif howClose == "Far":
            print("Prepare to stop")
        else:
            print("Invalid Choice")
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()