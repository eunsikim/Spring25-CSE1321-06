def mult_table(number):
    for x in range(13):
        print(f"{number} * {x} = {number * x}")

def main():
    number = 4
    mult_table(number)


if __name__ == "__main__":
    main()