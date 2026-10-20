class Student: 
    def __init__(self, id, name, grade): 
        self.id = id 
        self.name = name 
        self.grade = grade

    def display(self):
        print(f"ID: { self.id}, Name: {self.name}, Grade: {self.grade}")


class underGrad(Student): 

    def __init__(self, id, name, grade, major): 
        super().__init__(id, name, grade)
        self.major = major

    def display(self):
        super().display()
        print(f"Major: {self.major}")


class Grad(Student): 

    def __init__(self, id, name, grade, program): 
        super().__init__(id, name, grade)
        self.program = program

    def display(self): 
        super().display()
        print(f"Program: {self.program}")

john = underGrad(123,"John Doe", 98, "Computer Science")
alyssa = Student(456,"Alyssa Smith", 95)
michael = Grad(79,"Michael Johnson", 90, "Master of Science")

john.display()
alyssa.display()
michael.display()
