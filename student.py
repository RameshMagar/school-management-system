
from book import Book
class Student:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

n = int(input("Enter number of students"))
student = []

for i in range(n):
    x = input("Enter name: ")
    y = input("Enter address: ")
    stud = Student(x, y)
    student.append(stud)
# boo=Book("02","Romeo & Juliet","William Shakespear","3rd")
# disp = map(lambda stud: stud.getName() + " " + stud.getAddress(), student)
# print(list(disp))
# boo.getAuthor()
# print(boo.getAuthor())