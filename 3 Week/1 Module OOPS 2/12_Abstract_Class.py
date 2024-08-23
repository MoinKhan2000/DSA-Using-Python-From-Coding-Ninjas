""" 
ABSTRACT CLASS - This enforce the child classes to define a abstractClassMethod otw it will throw an error.
"""
from abc import ABC, abstractclassmethod


class Animal(ABC):
    @abstractclassmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


h = Human()
s = Snake()
d = Dog()
l = Lion()

# h.move()
# s.move()
# d.move()
# l.move()


# **************************************************************************
class DBConnection(ABC):
    @abstractclassmethod  # this is a decorator for the method below
    def createConnection(self):
        pass

    @abstractclassmethod
    def runQuery(self, query):
        pass


class SQLConnection(DBConnection):
    def createConnection(self):
        print("establishing SQL connection")

    def runQuery(self, query):
        print(f"running sql query '{query}' ")


class MongoConnection(DBConnection):
    def createConnection(self):
        print("establishing mongo db connection")

    def runQuery(self, query):
        print(f"running mongo query '{query}' ")


# db=DBConnection() # Cannot create object of the Abstract Class


db1 = SQLConnection()
db1.createConnection()
db1.runQuery("select * from table")


db1 = MongoConnection()
db1.createConnection()
db1.runQuery("select * from table")
