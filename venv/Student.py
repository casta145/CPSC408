class Student:

    def __init__(self, first_name, last_name, gpa, major, faculty_advisor):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.major = major
        self.faculty_advisor = faculty_advisor

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getGpa(self):
        return self.gpa

    def getMajor(self):
        return self.major

    def getFacultyAdivsor(self):
        return self.faculty_advisor

    def getStudentTuple(self):
        return self.getFirstName(), self.getLastName(), self.gpa, self.getMajor(), self.faculty_advisor