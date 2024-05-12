class student_data():
    def __init__(self, ID, name, birth_year, course):
        self.ID = ID
        self.name = name
        self.birth_year = birth_year
        self.course = course
    def display(self):
        print(f"ID: {self.ID}, Name: {self.name}, Birth Year: {self.birth_year}")
        print("Courses:")
        for course in self.course:
            print(f"Course ID: {course['id_course']}, Course Name: {course['name']}, Course Hours: {course['hours']}")

class Center():
    def __init__(self):
        self.students = []
    def add_student(self, ID, name, birth_year, course):
        student = student_data(ID, name, birth_year, course)
        self.students.append(student)
    def save_student(self):
        # print(self.students)
        with open('DSHV.txt', 'w') as f:
            for i in self.students:
                # print(f"{i.ID},{i.name},{i.birth_year},{i.course}\n")
                f.write(f"{i.ID},{i.name},{i.birth_year},{i.course}\n")
        f.close()    
    def display(self):
        for student in self.students:
            student.display()
    def display_students_with_two_courses(self):
        for student in self.students:
            if len(student.course) >= 2:
                student.display()
                
Center = Center()
n = int(input("Enter number of students: "))
for i in range(n):
    print("Student {0}".format(i+1))
    ID = input("Enter ID: ")
    name = input("Enter name: ")
    birth_year = int(input("Enter birth year: "))
    course = []
    m = int(input("Enter number of courses: "))
    for j in range(m):
        id_course = input("Enter course ID: ")
        name_course = input("Enter course name: ")
        hours = int(input("Enter course hours: "))
        course.append({"id_course": id_course, "name": name_course, "hours": hours})
    Center.add_student(ID, name, birth_year, course)
Center.save_student()
print("List of students")
Center.display()
print("List of students with at least 2 courses")
Center.display_students_with_two_courses()
       