def main():
    print("[Starting While Loop]")
    counter = 0
    while True:
        print(f"\nIteration #{counter}")
        choice = input("skip or exit: ")

        counter += 1

        if choice == "skip":
            print("\tSkipping to next iteration")
            continue
        elif choice == "exit":
            break
        
        for x in range(3):
            print(f"\t\tOperation #{x}")

    print("[While Loop Terminated]")


if __name__ == "__main__":
    main()