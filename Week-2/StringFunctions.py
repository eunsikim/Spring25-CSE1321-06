def main():
    message = "Hello World"
    number = 1

    print(message)

    # We are not changing message
    print(len(message))
    print(message.replace("Hello", "Goodbye"))
    print(message.upper())
    print(message.lower())
    print(message.isnumeric())
    print(message.split(" "))

    # We are changing the value of message
    message = message.upper()

    print(message)


if __name__ == "__main__":
    main()