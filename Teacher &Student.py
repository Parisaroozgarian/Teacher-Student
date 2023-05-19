class students:
    def __init__(self,name,family):
        self.name=name
        self.family=family
        self.marks=[]

    def showmarks(self):
        print(self.name+","+self.family)
        print(self.marks)

class Teacher:
    def __init__(self, code):
        self.code=code
        self.stud=''

    def setmark(self, student, m):
        self.stud = student
        self.stud.marks.append(m)
        student.showmarks()

    def showstudentname(self):
        print(self.stud.name)

    def setnamestudent(self,name):
        self.stud.name=name

student1=students('Joy','ClassB')
t1=Teacher(1)
t1.setmark(student1,19)
t1.setnamestudent('Ahmed')
student1.showmarks()
