class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades
    
    #Adds grades to the grades list - using .append in the method to add data to the list
    def add_grade(self, grade):
        self.grades.append(grade)

    #finds the average of the grades in the list, the if statement, prevents division by zero errors if the list is empty
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    #grades tuple - making grades to tuples and testing their immutability
    def grades_tuple(self):
        return tuple(self.grades)
    def test_immutability(self):
        try:
            grades_tuple_result = self.grades_tuple()
            grades_tuple_result[-1] = 9
        except TypeError as e:
            print(f'error: {e}')
            print(f'Tuples cannot be modified')

    #Displays information
    def display_info(self):
        print(f'Student Name: {self.name}, Email: {self.email}, Grades: {self.grades}')

#Here we are creating 3 students objects as instances of the student class, and providing related data
student1 = Student('John', 'john@example.com', [7, 8, 9, 10, 6])
student2 = Student('Sally', 'yllas@example.com', [4, 6, 7, 8, 5])
student3 = Student('Mike', 'kemi@exampmle.com', [10, 5, 10, 8, 7])

#Add two new grades to each student - calling the add_grade method to update the grades list
student1.add_grade(6)
student1.add_grade(10)
student1.display_info()

student2.add_grade(3)
student2.add_grade(9)
student2.display_info()

student3.add_grade(10)
student3.add_grade(1)
student3.display_info()

#Creating a dictionary and emails to student object
student_dict = {

    'john@example.com': student1,
    'yllas@example.com': student2,
    'kemi@example.com' : student3

}

#using .get() to pull student information from the dictionary
def get_student_by_email(email):
    return student_dict.get(email)

student_info = get_student_by_email('yllas@example.com')
student_info.display_info()

#create a set of all unique grades and print

all_grades = student1.grades + student2.grades + student3.grades #creates 1 list of all the grades
unique_grades = set(all_grades) #converts to a set
print(f'A set of all unique grades {sorted(unique_grades)}.') #prints ordered set

print(f'Student 1: {student1.grades}')
remove_last_grade = student1.grades.pop(-1)
print(f'Studnet 1: removed last grade {remove_last_grade}')

print(f'Student 2: {student2.grades}')
remove_last_grade = student2.grades.pop(-1)
print(f'Student 2: removed last grade {remove_last_grade}')

print(f'Student 3: {student3.grades}')
remove_last_grade = student3.grades.pop(-1)
print(f'Student 3: removed last grade {remove_last_grade}') 
#using len() to print the number of grades a student has
print(f'{student1.name} has {len(student1.grades)} grades reported')
print(f'{student2.name} has {len(student2.grades)} grades reported')
print(f'{student3.name} has {len(student3.grades)} grades reported')

#Display a grade tuple, Testing immutability - grades have been converted to tuples, a testing function has been created above, this will test the immutability
print(student1.grades_tuple())
student1.test_immutability()
