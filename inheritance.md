#####from first page we write this code

from people import Student
from people import Teacher

student1 = Student("John","Brown",22)
teacher1 = Teacher("Alex","White",57)

student1.print_first_name()
student1.print_info()

teacher1.print_first_name()
teacher1.print_info()

#####from second page we write this code

     class person:
    def __init__(self,first_name , last_name , age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def print_first_name(self):
        print("my first name is: " + self.first_name)


    def print_last_name(self):
        print("my last name is: " + self.last_name)


    def print_info(self):
        print(" my full name is:" + self.first_name + " " + self.last_name)





    class Student(person):

    def print_info(self):
        print("I am a student. my full name is:" +self.first_name + " " + self.last_name)



    class Teacher(person):

    def print_info(self):
        print("I am a teacher. my full name is:" +self.first_name + " " + self.last_name)

