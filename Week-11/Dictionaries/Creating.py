def main():
    # Creates an empty dictionary
    age = {}
 
    # Creates a dictionary with some key-value pairs
    ages = {
        "Alice": 30,
        "Bob": 40,
        "Charlie": 50,
    }

    # Creates a dictionary using dictionary comprehension
    numbers = {
        x: x ** 2 for x in range(10)
    }

    # Creates a dictionary using the dictionary constructor
    ages = dict(Alice = 30, Bob = 40, Charlie = 50)

if __name__ == "__main__":
    main()