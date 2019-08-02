from statistics import *

class GradeBook:
    def __init__(self):
        self.book = {}

    def addGrade(self, student, grade):
        if student in self.book:
            self.book[student].append(grade)
        else:
            self.book[student] = [grade]

    def getStudentAvg(self, student):
        if student in self.book:
            return mean(self.book[student])
        else:
            return -1   #need a better way to show student not found

    def removeStudent(self, student):
        if student in self.book:
            del self.book[student]
            return True
        else:
            return False   #need a better way to show student not found
        
    def alphabetize(self):
        sorted(self.book)

    def getAll(self):
        return self.book
        
def displayGUI():
    print("Please select one of the following options:\n",
          "[1] - Add grade\n",
          "[2] - Get student average\n",
          "[3] - Remove Student\n",
          "[4] - Exit\n")

def main():
    gb = GradeBook()

    print("Welcome to Gradebook!\n")
    while(1):
        displayGUI()

        userChoice = input("Option selected: ")
        
        if userChoice == "1":
            name = input("Student name: ")
            grade = input("Grade: ")
            
            try:    #In case user does not input a number for a grade
                gb.addGrade(name, int(grade))
                gb.alphabetize()
                print("Gradebook: ", gb.getAll(), "\n")
            except ValueError as t:
                print("Invalid grade. Please try again.\n")
        elif userChoice == "2":
            name = input("Student name: ")
            mean = gb.getStudentAvg(name)
            
            if mean != -1:
                print(name, "'s average is ", mean, ".\n")
            else:
                print("Student is not in the system.\n")
        elif userChoice == "3":
            name = input("Student name: ")
            
            if gb.removeStudent(name):
                print("Student successfully removed.")
            else:
                print("Student is not in the system.")

            print("Gradebook: ", gb.getAll(), "\n")
        elif userChoice == "4":
            print("Closing Gradebook.\n")
            break
        else:
            print("Invalid option. Option must be a number 1-4. Please try again.\n")

main()
