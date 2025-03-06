def main():
    numbers = [3, 5, 2, 7]

    length = len(numbers)

    for i in range(length):
        # At the end of each iteration we can assume
        # the last item in the list is in order
        # hence, we iterate -1 times for each iteration
        # of the outer loop.
        for index in range(length - i - 1):
            # Check if the current number is higher
            # than the next one, if so swap them
            if numbers[index] > numbers[index + 1]:
                #Swap
                temp = numbers[i]
                numbers[i] = numbers[index + 1]
                numbers[index + 1] = temp

    print(numbers)      

if __name__ == "__main__":
    main()
