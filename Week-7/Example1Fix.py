def avg(sum, size):
    average = sum / size
    return average

def calculateFinalGrade(case, known_labs, known_assignments):
    # Default is worst case
    unknown_labs = 0
    unknown_assignments = 0
    unknown_midterm = 0
    unknown_final = 0

    if case == "best":
        unknown_labs = 800
        unknown_assignments = 500
        unknown_midterm = 100
        unknown_final = 100

    lab_avg = avg((known_labs + unknown_labs), 13)
    assignment_avg = avg((known_assignments + unknown_assignments), 7)

    finalGrade = (lab_avg * 0.1) + (assignment_avg * .4) + (unknown_midterm * .2) + (unknown_final * .3)

    return finalGrade

def main():
    Lab1 = 80
    Lab2 = 90
    Lab3 = 50
    Lab4 = 59
    Lab5 = 84
    Assignment1 = 90
    Assignment2 = 60

    lab_sum = Lab1 + Lab2 + Lab3 + Lab4 + Lab5
    asssignment_sum = Assignment1 + Assignment2

    best = calculateFinalGrade("best", lab_sum, asssignment_sum)
    worst = calculateFinalGrade("worst", lab_sum, asssignment_sum)

    print(f"Maximum possible final grade: {best}")

    print(f"Minimum possible final grade: {worst}")

    if True:
        x = 80

    print(x)

if __name__ == "__main__":
    main()