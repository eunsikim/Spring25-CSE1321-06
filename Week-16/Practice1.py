def main():
    loop = True
    numbers = []
    while True:
        user_input = input("Enter a number (s to stop): ")

        if user_input == "s":
            break
        else:
            user_input = int(user_input)

        numbers.append(user_input)
    
    size = len(numbers)

    sum = 0
    for number in numbers:
        sum += number

    average = sum / size

    print(f"Average: {average}")



if __name__ == "__main__":
    main()