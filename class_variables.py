# class variables = share data among all instances of a class

class Student:
    num_students = 0
    class_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

# print(student1.name)
# print(student1.age)

# access class variable using class name
# print(Student.class_year)

# print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
