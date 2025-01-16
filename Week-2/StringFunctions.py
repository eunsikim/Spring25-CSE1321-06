def main():
    message = "Hello World"
    number = 1

    print(message + number)
    print(len(message))
    print(message.replace("Hello", "Good Bye"))
    print(message.upper())
    print(message.lower())
    print(message.isnumeric())
    print(message.split(" "))


if __name__ == "__main__":
    main()