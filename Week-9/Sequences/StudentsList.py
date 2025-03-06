def main():
    students = [[], [], []]

    students[0].append("John")
    students[0].append("Doe")
    students[0].append(86.5)

    students[1].append("Jane")
    students[1].append("Smith")
    students[1].append(90)

    students[2].append("John")
    students[2].append("Smith")
    students[2].append(70)

    print(students[0])
    print(students[1])
    print(students[2])
    print()

    students[1][2] = 100
    print(students[1])
    print()

    for student in students:
        for value in student:
            print(value, end=", ")
        print()
    print()

    for student in students:
        print(f"Name: {student[0]} {student[1]}")
    print()

    del students[1]
    for student in students:
        print(f"Name: {student[0]} {student[1]}")


if __name__ == "__main__":
    main()
