def twoSum(nums, target):
    numbers = {}
    indexes = []

    for i, n in enumerate(nums):
        if n in numbers:
            indexes.append(i)
            indexes.append(numbers[n])
            break
        else:
            numbers[target - n] = i

    return indexes


print(twoSum([2,3,4], 7))