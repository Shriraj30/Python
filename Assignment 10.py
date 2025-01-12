from types import MethodType
class Student:
    pass

def printInfo(self):
    return f"Regno: {self.Regno}, Name: {self.Name}"

def create_student():
    s = Student()
    reg_no = input("Enter Registration Number: ")
    name = input("Enter Name: ")
    setattr(s, "Regno", reg_no)
    setattr(s, "Name", name)
    s.printInfo = MethodType(printInfo, s)
    return s

students = []
while True:
    student = create_student()
    students.append(student)
    print(student.printInfo())  

    another = input("Would you like to enter data for another student? (yes or no): ").strip().lower()
    if another != 'yes':
        break

print("\nAll Students' Information:")
for student in students:
    print(student.printInfo())
