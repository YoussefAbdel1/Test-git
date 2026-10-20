class student: 
    def __init__(self, name, id, grade): 
        self.name = name 
        self.id = id
        self.grade = grade 

    def display_info(self): 
        print("Name:", self.name) 
        print("ID:", self.id) 
        print("Grade:", self.grade)


class graduateStudent(student): 
    def __init__(self, name, id, grade, program_title): 
        super().__init__(name, id, grade) 
        self.program_title = program_title 

    def display_info(self): 
        super().display_info() 
        print("Program Title:", self.program_title)


class undergraduateStudent(student):
    def __init__(self, name, id, grade, major): 
        super().__init__(name, id, grade) 
        self.major = major 

    def display_info(self): 
        super().display_info() 
        print("Major:", self.major)


studentJohn = student("John Doe", "12345", 56)
graduateStudentAlice = graduateStudent("Alice Smith", "67890", 89, "Masters of Science")
undergraduateStudentBob = undergraduateStudent("Bob Johnson", "54321", 75, "Electrical Engineering")

studentJohn.display_info()
graduateStudentAlice.display_info()
undergraduateStudentBob.display_info()
print("Is studentJohn an instance of student?", isinstance(studentJohn, student))
print("Is graduateStudentAlice an instance of student?", isinstance(graduateStudentAlice, student))
