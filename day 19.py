class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def display(self):
        print("Employee name:",self.name)
        print("Salary:",self.salary)
name=input("Enter employee name:")
salary=float(input("Enter salary:"))
m=Manager(name,salary)
m.display()

# Base class
class School:
    def __init__(self, school_name):
        self.school_name = school_name


# Derived class
class Teacher(School):
    def __init__(self, school_name, subject):
        super().__init__(school_name)
        self.subject = subject


# Derived class
class HeadTeacher(Teacher):
    def __init__(self, school_name, subject, experience):
        super().__init__(school_name, subject)
        self.experience = experience

    def display(self):
        print("School Name:", self.school_name)
        print("Subject:", self.subject)
        print("Experience:", self.experience, "years")


# Main program
school = input("Enter school name: ")
subject = input("Enter subject: ")
experience = int(input("Enter experience (years): "))

h = HeadTeacher(school, subject, experience)
h.display()
    
class Camera:
    def take_photo(self):
        print("Photo taken")


class MusicPlayer:
    def play_music(self):
        print("Music is playing")


class Smartphone(Camera, MusicPlayer):
    pass


# Object creation
phone = Smartphone()

# Calling methods
phone.take_photo()
phone.play_music()
        