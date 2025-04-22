def listSum(numbers):
    incIndex = 0
    decIndex = len(numbers) - 1
    half = int(len(numbers) / 2)

    for x in range(half):
        print(numbers[incIndex] + numbers[decIndex])

        incIndex += 1
        decIndex -= 1


def main():
    numbers = [2,3,4,5,11,13,15,17]

    listSum(numbers)



if __name__ == "__main__":
    main()