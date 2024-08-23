# Covers slides


"""             PUBLIC          """
"""             UNLIKE OTHER LANGUAGES PYTHON DOES NOT NEED TO DECLARE THE PUBLIC PRIVATE AND PROTECTED KEYWORDDS WHLE DECLARING THE MEMBERS            """


class Geek:
    # Constructor
    def __init__(self, name, age):
        # Public data members
        self.geekName = name
        self.geekAge = age

    # Public member function
    def displayAge(self):
        # Accessing public data member
        print("Name :", self.geekName)
        print("Age :", self.geekAge)


# Creating object of the class
ob = Geek("Moin", 23)
# Accessing public data member outside the class methods
# print("Name :", ob.geekName)
# print("Age :", ob.geekAge)
# Calling a public member funciton of the class
# ob.displayAge()


"""             PROTECTED          """
""" The members of the class that are declared protected are only accessible to a class derived from it. Data members of a class are declared protected by adding a single '_' underscore symbol before the data members of that class"""


# Super Class
class Student:
    # Protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch
        # self._displayRollAndBranch()

    # protected member functions
    def _displayRollAndBranch(self):
        print("Name :", self._name)
        print("Roll No. :", self._roll)
        print("Branch Name :", self._branch)


# s1 = Student("Moin Khan", "CS126", "CSE")
# Name : Moin Khan
# Roll No. : CS126
# Branch Name : CSE

# s1._displayRollAndBranch()
# Name : Moin Khan
# Roll No. : CS126
# Branch Name : CSE

# print(s1._name)
# Name : Moin Khan


class Geek(Student):  # Geek became child class of Student(super class)
    # Constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):
        print("\n\tGeek Details")

        # accessing protected data members of super class
        print("Name :", self._name)

        # accessing protected member functions of super class
        Student._displayRollAndBranch(self)


# creating objects of the derived class
# obj = Geek("Moin Khan", "CS126", "Informatin Technology")
# obj.displayDetails()


"""             PRIVATE          """
"""         The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier. Data members of a class are declared private by adding double underscore '__' before the data members of that class          """


class Geek:
    # Private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):
        print("\nGeek Details")
        # accessing private data members of this class
        print("Name :", self.__name)
        print("Roll No. :", self.__roll)
        print("Branch :", self.__branch)

    # public member function
    def accessPrivateFunction(self):
        # accessing private member function
        self.__displayDetails()


# Creating an object
obj = Geek("Moin Khan", "CS126", "CYBER SECURITY")
obj.accessPrivateFunction()
# obj.__displayDetails()  # Attribute Error
