import re
class Student:
    def __init__(self):
        self.RegNo = None
        self.Name = None

    def setRegNo(self, reg_no):
        self.RegNo = reg_no

    def setName(self, name):
        self.Name = name

    def getRegNo(self):
        return self.RegNo

    def getName(self):
        return self.Name

class Exam:
    def __init__(self):
        self.Examno = None
        self.Pattern = None
        self.Semister = None

    def setData(self, exam_no, pattern, semister):
        self.Examno = exam_no
        self.Pattern = pattern
        self.Semister = semister

    def getData(self):
        return {
            "Examno": self.Examno,
            "Pattern": self.Pattern,
            "Semister": self.Semister
        }

class Result(Student, Exam):
    def __init__(self):
        super().__init__()
        self.Phy_marks = 0
        self.Maths_marks = 0
        self.Chem_marks = 0

    def setMarks(self, phy, maths, chem):
        self.Phy_marks = phy
        self.Maths_marks = maths
        self.Chem_marks = chem

    def getMarks(self):
        return {
            "Physics": self.Phy_marks,
            "Maths": self.Maths_marks,
            "Chemistry": self.Chem_marks
        }


    def calResultGrade(self):
        total = self.Phy_marks + self.Maths_marks + self.Chem_marks
        avg = total / 3

        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

def get_student_details():
    student = Result()

    while True:
        reg_no = input("Enter the registration number (numbers only): ")
        if re.match(r'^\d+$', reg_no):  
            student.reg_no = reg_no
            break
        else:
            print("Invalid input. Please enter numbers only.")

    while True:
        name = input("Enter the student name (letters and spaces only): ")
        if re.match(r'^[A-Za-z\s]+$', name):  
            student.name = name
            break
        else:
            print("Invalid input. Please enter letters and spaces only.")

    exam_no = input("Enter the exam number: ")
    pattern = input("Enter the exam pattern: ")
    semister = input("Enter the semester: ")

    phy_marks = float(input("Enter Physics marks: "))
    maths_marks = float(input("Enter Maths marks: "))
    chem_marks = float(input("Enter Chemistry marks: "))

    student = Result()

    student.setRegNo(reg_no)
    student.setName(name)
    student.setData(exam_no, pattern, semister)

    student.setMarks(phy_marks, maths_marks, chem_marks)

    return {
        "Student Name": student.getName(),
        "Reg No": student.getRegNo(),
        "Exam Details": student.getData(),
        "Marks": student.getMarks(),
        "Grade": student.calResultGrade()
    }

student_info = get_student_details()

for key, value in student_info.items():
    print(f"{key}: {value}")
