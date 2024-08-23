class Student:
    schoolName = (
        "Anjuman Islamiya Urdu School Betul (M.P)"  # Static variables (Class VAriables)
    )
    enrollId = 124
    totalStudents = 0

    def __init__(self, name, id):
        self.name = name
        self.enrollId = id
        # Everytime whenever the new Student is created it will increment the totalStudents. Meke sure that it will increment if the Student is created using the constructor
        Student.totalStudents += 1

    def printDetails(self):
        print(
            "School Name :",
            self.schoolName,  # Instance Variables
            "\nStudent Name :",
            self.name,
            "\nStudent EnrollMent :",
            self.enrollId,
        )


s1 = Student("Moin Khan", "CS126")
s1.printDetails()
s2 = Student("Moin Khan", "CS126")
s2.printDetails()


s3 = Student
print(s3.enrollId)  # 124
# print(s3.name)  # Student have no attribute 'name'

print(Student.totalStudents)
# 2 s1 and s2 are created using constructor so output is 2 s3 is created without all info.

print(Student.__dict__)
print(Student.__dict__["totalStudents"])  # 2


"""  
Instance Variable : 1. Bound to Object
                    2. Declared inside the  __init()__ method
                    3. Not shared by every objects. Every Object has its own copy

Class  Variables :  1. Bound to the Class
                    2. Declared inside the class, but outside of any method
                    3. Shared by all objects of a class

"""
