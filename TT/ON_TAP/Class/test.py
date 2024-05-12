class Student:
    def __init__(self, id, name, birth_year, courses):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.courses = courses

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Birth Year: {self.birth_year}")
        print("Courses:")
        for course in self.courses:
            print(f"Course ID: {course['id']}, Course Name: {course['name']}, Course Hours: {course['hours']}")

class AI_Center:
    def __init__(self):
        self.students = []

    def add_student(self, id, name, birth_year, courses):
        student = Student(id, name, birth_year, courses)
        self.students.append(student)

    def save_students(self):
        with open('DSHV.txt', 'w') as f:
            for student in self.students:
                f.write(f"{student.id},{student.name},{student.birth_year},{student.courses}\n")

    def display_students(self):
        for student in self.students:
            student.display()

    def display_students_with_two_courses(self):
        for student in self.students:
            if len(student.courses) >= 2:
                student.display()

center = AI_Center()
center.add_student("123456789", "Nguyen Van A", 1990, [{"id": "CS101", "name": "Computer Science", "hours": 60}, {"id": "AI101", "name": "Artificial Intelligence", "hours": 60}])
center.save_students()
center.display_students()
center.display_students_with_two_courses()