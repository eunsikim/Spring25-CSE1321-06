def main():
    Lab1 = 80
    Lab2 = 90
    Lab3 = 69
    Lab4 = 59
    Lab5 = 84
    Assignment1 = 90
    Assignment2 = 60

    # Best Case: Remaining Labs, Assignment, midterm, and final are 100
    lab_sum = Lab1 + Lab2 + Lab3 + Lab4 + Lab5 + 800
    assignment_sum = Assignment1 + Assignment2 + 500
    midterm = 100
    final = 100

    lab_avg = lab_sum / 13
    assignment_avg = assignment_sum / 7
    finalGrade = (lab_avg * 0.1) + (assignment_avg * .4) + (midterm * .2) + (final * .3)
    print(f"Maximum possible final grade: {finalGrade}")

    # Worst Case: Remaining Labs, Assignment, midterm, and final are 0
    lab_sum = Lab1 + Lab2 + Lab3 + Lab4 + Lab5
    assignment_sum = Assignment1 + Assignment2
    midterm = 0
    final = 0

    lab_avg = lab_sum / 13
    assignment_avg = assignment_sum / 7
    finalGrade = (lab_avg * 0.1) + (assignment_avg * .4) + (midterm * .2) + (final * .3)
    print(f"Minimum possible final grade: {finalGrade}")

if __name__ == "__main__":
    main()