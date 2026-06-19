class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)


s = Student("Arun", 101)
t = Teacher("Meera", "Mathematics")

s.display()
print()
t.display()

class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, language):
        Employee.__init__(self, name)
        self.language = language


class Tester(Employee):
    def __init__(self, name, tool):
        Employee.__init__(self, name)
        self.tool = tool


class TeamLead(Developer, Tester):
    def __init__(self, name, language, tool):
        Developer.__init__(self, name, language)
        Tester.__init__(self, name, tool)

    def display(self):
        print("Employee Name:", self.name)
        print("Programming Language:", self.language)
        print("Testing Tool:", self.tool)


tl = TeamLead("Sree", "Python", "Selenium")
tl.display()