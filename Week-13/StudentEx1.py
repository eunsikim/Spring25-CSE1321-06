import random

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def printInfo(self):
        print(f"Name: {self.name}, GPA: {self.gpa}")

def main():
    names = ["Alice", "Bob", "Charlie", "John"]
    
    studentList = []

    for x in range(1000):
        studentList.append(Student(random.choice(names), random.randint(0, 4)))

    for student in studentList:
        student.printInfo()

if __name__ == "__main__":
    main()

