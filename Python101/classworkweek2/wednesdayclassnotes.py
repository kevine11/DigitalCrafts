###### Continued from tuesday COMPOSITION

# class Student(object):

#     def __init__(self, firstName, lastName, campus):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.campus = campus

#     def printStudent(self):
#         print(f"{self.firstName}, {self.lastName}, {self.campus}")

# # Sabrina = Student("Sabrina", "Goldfarb", "Houston")

# # Alfie = Student("Alfie", "Sanchez", "Houston")

# # Michael = Student("Michael", "Dao", "Houston")

# # Cindy = Student("Cindy", "Smith", "Atlanta") 

# class Campus:
#     def __init__(self):
#         self.student = []

#     def addStudent(self, firstName, lastName, campus):
#         temp = Student(firstName, lastName, campus)
#         self.student.append(temp)

#     def showCurrentStudent(self):
#         for studentObject in self.student :
#             print(f"{studentObject.firstName}, {studentObject.lastName}, {studentObject.campus}")

# management = Campus()

# management.addStudent("Sabrina", "Goldfarb", "Houston")
# management.addStudent("Alfie", "Sanchez", "Houston")
# management.addStudent("Michael", "Dao", "Houston")
# management.addStudent("Cindy", "Smith", "Atlanta")

# # print(management.showCurrentStudent)
# management.showCurrentStudent

######## BANKING APP