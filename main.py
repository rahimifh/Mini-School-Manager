#============================================================
#    MINI SCHOOL MANAGER 
#    Concepts  used: variable, data type, list, dictionary,
#                 class, input, print, for loop, while loop
#============================================================



#------------------ VARIABLE & DATA TYPES --------------
APP_NAME = "Mini School Manager"  # str
MAX_GRADES = 5                    # int
PASS_MARK = 10.0                  # float
IS_OPEN =   True                  # bool


class Student:
    """
        A student object.
    """
    def __init__(self, name:str, age:int):
        self.name = name    #str
        self.age = age      #int
        self.grades = []    # list grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self)->float:
        #empty list is "falsy"
        if not  self.grades:
            return 0.0     
        return sum(self.grades)/len(self.grades)

    def passed(self):
        return self.average() >= PASS_MARK

    def to_dict(self):
        """Return the student as a dictionary."""
        return {
            "name": self.name,
            "age": self.age,
            "grades": round(self.average(), 2),
            "passed": self.passed(),
        }

    def __str__(self):
        return f"{self.name} age: {self.age} - avg {self.average()}"




class School:
    """
        Holds a list of Student objects.
    """
    def __init__(self, name):
        self.name = name
        self.students = [] #list of student objects

    def add_student(self, name, age):
        self.students.append(Student(name, age))

    def find(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None
        
    def report(self):
        if not self.students:
            print("No student yet. ")
            return
        print(f"\n--- {self.name} report ---")
        for i, student in enumerate(self.students, start=1): 
            status = ""
            #status = "PASS" if student.passed() else "FAIL"
            if student.passed(): 
                status = "PASS"
            else:
                status = "FAIL"
            print(f"{i}. {student} -> {status}")




def add_student_flow(school):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be enpty.")
        return 
    age = int(input("Age: "))
    school.add_student(name, age)
    print(f"Added {name}.")

def add_grade_flow(school):
    name = input("student name: ").strip()
    student = school.find(name)
    if student is None:
        print("Student not found.")
        return 
    if len(student.grades) >= MAX_GRADES:
        print(f"Grade limit ({MAX_GRADES}) reached.")
        return
    grade = float(input("Grade (0 - 20): "))
    student.add_grade(grade)
    print(f"{grade} added to {student.name}.")

def show_student_flow(school):
    name = input("Student name: ").strip()
    student  = school.find(name)
    if student is None:
        print("Student not found.")
        return 
    data = student.to_dict()
    for key, value in data.items():
        print(f" {key}: {value}")   

def remove_student_flow(school):
    name = input("Student name: ").strip()
    student  = school.find(name)
    if student is None:
        print("Student not found.")
        return 
    for student in school.students:
        if student.name.lower() == name.lower():
            school.students.remove(student)
            print(f"Removed {student.name}.")
            return
    print("Student not found.")

    
        


def main():
    school = School("Buali School")
    menu = {
        "1": ("Add a student", add_student_flow),
        "2": ("Add a grade", add_grade_flow),
        "3": ("Show report", lambda school: school.report()),
        "4": ("Show one student", show_student_flow),
        "5": ("Remove a student", remove_student_flow),
        "0": ("Quit",  None),
    }

    print(f"========= {APP_NAME} ==========")

    running = True
    while running:
        print("\nMenu: ")
        #For loop over a dict
        for key, (lable, _) in menu.items(): 
            print(f" {key}) {lable}")

        choice = input("your choice: ").strip()

        if choice == "0":
            running = False
            print("Goodbye!")
            continue

        entry = menu.get(choice)
        if entry is None:
            print("Unknown choice, try again.")
            continue
        entry[1](school)

if __name__ == "__main__":
    main()