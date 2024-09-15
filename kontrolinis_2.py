class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age) # <-- Papildytas kodas (užduoties 1 p.)
        self.enrolled_courses = [] # Užsiregistravusių kursuose sąrašas
        self.grades = {}  # Žodynas kursų pažymiams saugoti

    def enroll(self, course): # Funkcija registracijai į kursus. Funkcija patikrina ar yra įregistruotas kursas self.enrolled_courses sąraše. Jei ne, prideda kursą į sąrašą.
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self) # Kviečiama funkcija add.student, kuri tikrina ar yra įregistruotas studentas self.students sąraše. Jei ne, prideda studentą į sąrašą.

    def performance_report(self): # Funkcija studentų kursų rezulatų spausdinimui
        for course, grade in self.grades.items(): # <-- Pataisytas/papildytas kodas (užduoties 3 p.)
            print(f"Student: {self.name}, Course: {course.name}, Grade: {grade}") # <-- Papildytas kodas (užduoties 3 p.)

    def record_grade(self, course, grade): # Funkcija patikrina ar kursas yra įregistruotas elf.enrolled_courses sąraše. Jei yra, įrašo vertinimą į self.grades žodyną.
        if course in self.enrolled_courses:
            self.grades[course] = grade # <-- Pataisytas kodas (užduoties 2 p.)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age) # <-- Papildytas kodas (užduoties 1 p.)
        self.subject = subject
        self.courses = []

    def list_courses(self): # Funkcija grąžina mokytojui priskirtų kursų pavadinimų sąrašą
        course_names = [] # <-- # <-- Papildytas kodas (užduoties 4 p.)
        for course in self.courses: # <-- Papildytas kodas (užduoties 4 p.)
            course_names.append(course.name) # <-- Papildytas kodas (užduoties 4 p.)
        return course_names # <-- Pakeistas kodas (užduoties 4 p.)

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        self.lessons = [] # <-- Papildytas kodas (papildoma užduotis)
        teacher.courses.append(self)  # Funkcijos, kuri įtraukia į kursą mokytoją iškvietimas

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status): # Funkcija patikrina, ar studentas yra self.students sąraše. Jei yra, prideda lankomumo informaciją - datą, būseną.
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            attendance_status = [] # <-- Pakeistas kodas (užduoties 5 p.)
            for date, status in attendance_record: # <-- Papildytas kodas (užduoties 5 p.)
                attendance_status.append(f"{date}: {status}") # <-- Papildytas kodas (užduoties 5 p.)
            print(f"Student: {student.name}, Attendance: {attendance_status}")

    def add_lesson(self, lesson): # <-- Sukuriama papildoma funkcija (papildoma užduotis)
        self.lessons.append(lesson)

    def get_lessons(self): # <-- Sukuriama papildoma funkcija (papildoma užduotis)
        return self.lessons


class Lesson: # <-- Sukuriama papildoma klasė ir funkcijos (papildoma užduotis)
    def __init__(self, topic, date, materials):
        self.topic = topic
        self.date = date
        self.materials = materials


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)
lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"]) # <-- Perkelta prieš funkcijos iškvietimą (papildoma užduotis)
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"]) # <-- Perkelta prieš funkcijos iškvietimą (papildoma užduotis)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Add lessons to the course
math_course.add_lesson(lesson1) # <-- Iškviečiama funkcija (papildoma užduotis)
math_course.add_lesson(lesson2) # <-- Iškviečiama funkcija (papildoma užduotis)

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']

# Create a course and teacher
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)

# Add lessons to the course
math_course.add_lesson(lesson1)
math_course.add_lesson(lesson2)
math_course.get_lessons()

# Retrieve and print the list of lessons
lessons = math_course.get_lessons() # <-- Iškviečiama funkcija (papildoma užduotis)
for lesson in lessons:
    print(f"Topic: {lesson.topic}, Date: {lesson.date}, Materials: {lesson.materials}") # <-- Informacijos spausdininimas (papildoma užduotis)
