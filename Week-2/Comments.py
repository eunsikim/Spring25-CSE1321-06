def main():
    """
        This program takes two integer number
        input from the user, and prints the
        sum of the two numbers.
    """
    # Get the two numbers from the user
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    sum = num1 + num2 # Add two numbers
    # Print the sum
    print("The sum of the two numbers is", sum)

if __name__ == "__main__":
    main()