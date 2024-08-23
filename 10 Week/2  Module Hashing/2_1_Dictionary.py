# There are total 3 ways to create dictionary

temp = dict({"Moin": 99, "Harshit": 83, "Priyanshu": 88})
print(temp, type(temp))
# {'Moin': 99, 'Harshit': 83, 'Priyanshu': 88} <class 'dict'>

temp = dict([("Moin", 99), ("Harshit", 83), ("Priyanshu", 88)])
print(temp, type(temp))
# {'Moin': 99, 'Harshit': 83, 'Priyanshu': 88} <class 'dict'>

temp = {"Moin": 99, "Harshit": 83, "Priyanshu": 88}
print(temp, type(temp))
# {'Moin': 99, 'Harshit': 83, 'Priyanshu': 88} <class 'dict'>

# Creating the dictionary from the keys only example creating dict from studentsArray
studentsArray = ["Alice", "Bob", "Charlie"]
studentsDict = dict.fromkeys(studentsArray)
print(studentsDict, type(studentsDict))
# {'Alice': None, 'Bob': None, 'Charlie': None} <class 'dict'>


studentsDict = dict.fromkeys(studentsArray)
studensDict = dict.fromkeys(studentsArray, 1)
print(studensDict, type(studentsDict))
# {'Alice': 1, 'Bob': 1, 'Charlie': 1} <class 'dict'>

temp1 = {"Moin": 99, "Harshit": 83, "Priyanshu": 88}
temp2 = temp1  # A reference of temp 1 is stored in temp2 if any changes are performed with the help of temp 2 it will also be reflected in the temp1 to overcome this issue we have a copy method to copy the whole object (dictionary)
del temp2["Moin"]
print(temp1)
# {'Harshit': 83, 'Priyanshu': 88}
print(temp2)
# {'Harshit': 83, 'Priyanshu': 88}

temp1 = {"Moin": 99, "Harshit": 83, "Priyanshu": 88}
temp2 = temp1.copy()
del temp2["Moin"]
print(temp1)
# {'Moin': 99, 'Harshit': 83, 'Priyanshu': 88}
print(temp2)
# {'Harshit': 83, 'Priyanshu': 88}
print(len(temp1))
# 3
print(len(temp2))
# 2
temp1 = {"Moin": 99, "Harshit": 83, "Priyanshu": 8}
print(max(temp1.values()))
# 99
print(min(temp1.values()))
# 8
