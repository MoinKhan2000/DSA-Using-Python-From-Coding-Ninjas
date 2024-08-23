"""                     
MRO 
    --> MRO is concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.
    
    --> In python, the MRO is from bottom to top and left to right. This means that, first, the method is searched in the class of the object. If it's not found, it is searched in the immediate super class. In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer

"""


#   **************************************   Case 1  **************************************
class A:
    def method(self):
        print("A.method() called")


class B(A):
    def method(self):  # Method overriding
        print("B.method() called")


# b = B()
# b.method()  # B.method() called

# print(B.mro())
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

#   **************************************   Case 2  **************************************


class A:
    def process(self):
        print("A.process()")


class B:
    def process(self):
        print("B.process()")


class C(A, B):  # A is getting precedence form B
    pass


# obj = C()
# B.method() called
# obj.process()
# A.process()
# print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


#   **************************************   Case 3  **************************************
"""
             A        B
              \      /|
               \    / |
                \  /  | 
                  C   |
                  |   |
                  |   |
                   \ /
                    D
"""


class A:
    def process(self):
        print("A.process()")


class B:
    def process(self):
        print("B.process()")


class C(A, B):
    def process(self):
        print("C.process()")


class D(C, B):
    pass


# obj = D()
# B.method() called
# obj.process()
# C.process()
# print(D.mro())
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


#   **************************************   Case 4  **************************************
"""
                 A
                /  \    
               /    \ 
              /      \ 
             B        C
              \      /
               \    / 
                \  /  
                  D   
                  
                    
"""


class A:
    def process(self):
        print("A.process()")


class B(A):
    def process(self):
        print("B.process()")


class C(A):
    def process(self):
        print("C.process()")


class D(B, C):
    pass


# obj = D()
# obj.process()
# print(D.mro())

# As per inheritance, the most specific version must be taken first and then least specific (generic) version. So, calling process() from A, which is upper class of C, is not as C is direct super class of D. That means C is more specific than A. So method must come from C and not from A.

#   **************************************   Case 5  **************************************
"""
                  __A__
                  |   |
                  |   | 
                  |   B 
                  |   |
                  |   |
                   \ /
                    C
"""


class A:
    def process(self):
        print("A process()")


class B(A):
    def process(self):
        print("B process()")


# class C(A,B):
#     pass

# obj=C();
# obj.process()
# print(C.mro())
# Traceback (most recent call last):
#   File "d:\CN\DSA\3 Week\1 Module OOPS 2\8_Method_Resolution_Order.py", line 151, in <module>
#     class C(A,B):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B


class C(B, A):
    pass


obj = C()
obj.process()
# B process()
print(C.mro())
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
