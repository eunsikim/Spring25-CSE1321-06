def main():
    age1 = int(input("Enter age for student 1: "))
    age2 = int(input("Enter age for student 2: "))
    age3 = int(input("Enter age for student 3: "))
    age4 = int(input("Enter age for student 4: "))
    age5 = int(input("Enter age for student 5: "))
    age6 = int(input("Enter age for student 6: "))
    age7 = int(input("Enter age for student 7: "))
    age8 = int(input("Enter age for student 8: "))
    age9 = int(input("Enter age for student 9: "))
    age10 = int(input("Enter age for student 10: "))

    avg = age1 + age2 + age3 + age4 + age5 + age6 + age7 + age8 + age9 + age10;
    avg = avg / 10;

    print(f"The average age for this class is: {avg}");

if __name__ == "__main__":
    main()