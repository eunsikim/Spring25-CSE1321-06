from arabic_reshaper import reshape
from bidi.algorithm import get_display

def main():
    message = "Hello World"

    # print(len(message))

    # x = 5
    # print(type(x))
    # print(type(str(x)))
    # print()

    # x = "Hello world"
    # print(type(x))
    # print(type(str(x)))

    message = "HELlO worlD" # Hello world
    print(message.capitalize())

    if message.isalpha():
        print("Your message is all alphabetic")
    else:
        print("Your message contains a number")


    message = "987123A!"

    if message.isalnum():
        print("Your message is all alphanumeric")
    else:
        print("Your message contains a non-alphanumeric character")


    message = "Hello World"

    print(message.replace("ello", "X"))

    message = message.replace("e", "i")
    message = message.replace("o", "e")

    print(message)

    print("ALL UPPERCASE".isupper())
    print("all lowercase".islower())


    text_to_be_reshaped = 'اللغة العربية رائعة'
    print(text_to_be_reshaped)
    print(get_display(reshape(text_to_be_reshaped)))



if __name__ == "__main__":
    main()