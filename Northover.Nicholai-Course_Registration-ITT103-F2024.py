class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee


class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0  # Track remaining balance

    def enroll(self, course): # Adds a course to the student’s list and updates their balance.
        if course in self.courses:
            raise ValueError("Student is already enrolled in this course.")
        self.courses.append(course)
        self.balance += course.fee

    def get_total_fee(self): # Calculates the total fees for all enrolled courses.
        return sum(course.fee for course in self.courses)


class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = {}

    def add_course(self, course_id, name, fee): #Adds a new course
        if any(course.course_id == course_id for course in self.courses):
            raise ValueError("Course ID already exists.")
        new_course = Course(course_id, name, fee)
        self.courses.append(new_course)

    def register_student(self, student_id, name, email): #: Registers a new student.
        if student_id in self.students:
            raise ValueError("Student ID already apart database.")
        new_student = Student(student_id, name, email)
        self.students[student_id] = new_student

    def enroll_in_course(self, student_id, course_id): #Enrolls a student in a specified course.
        if student_id not in self.students:
            raise ValueError("Student not found.")

        student = self.students[student_id]
        course = next((c for c in self.courses if c.course_id == course_id), None)

        if not course:
            raise ValueError("Course not found.")

        student.enroll(course)

    def calculate_payment(self, student_id, amount): #Processes payments.Requires at least 40% of the balance to confirm registration and updates the remaining balance.

        if student_id not in self.students:
            raise ValueError("Student not found.")

        student = self.students[student_id]

        if amount < 0.4 * student.balance:
            raise ValueError("Minimum payment is 40% of the balance.")

        student.balance -= amount

    def check_student_balance(self, student_id): #Displays the current balance of a specific student.
        if student_id not in self.students:
            raise ValueError("Student is not found.")

        return f"Current balance for {self.students[student_id].name}: ${self.students[student_id].balance:.2f}"

    def show_courses(self): #Lists all available course
        return [(course.course_id, course.name, course.fee) for course in self.courses]

    def show_registered_students(self): #List all registered students
        return [(student.student_id, student.name) for student in self.students.values()]

    def show_students_in_course(self, course_id): #Lists all students enrolled in a specific course.
        course_students = [
            (student.student_id, student.name)
            for student in self.students.values()
            if any(c.course_id == course_id for c in student.courses)
        ]

        return course_students


def main():
    system = RegistrationSystem()

    while True:
        print("\nMenu:")
        print("1. Add a new Course")
        print("2. Register a new Student")
        print("3. Enroll Student in a specific Course")
        print("4. Process Payments")
        print("5. Check Student Balance")
        print("6. List all available Courses")
        print("7. List all Registered Students")
        print("8. List all Students enrolled in Course")
        print("9. Exit")

        choice = input("Select an option: ")

        try:
            if choice == '1':
                course_id = input("Enter Course ID: ")
                name = input("Enter Course Name: ")
                fee = float(input("Enter Course Fee: "))
                system.add_course(course_id, name, fee)
                print(f"Course {name} added successfully.")

            elif choice == '2':
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                email = input("Enter Student Email: ")
                system.register_student(student_id, name, email)
                print(f"Student {name} registered successfully.")

            elif choice == '3':
                student_id = input("Enter Student ID: ")
                course_id = input("Enter Course ID: ")
                system.enroll_in_course(student_id, course_id)
                print(f"Student {student_id} enrolled in {course_id}.")

            elif choice == '4':
                student_id = input("Enter Student ID: ")
                amount = float(input("Enter Payment Amount: "))
                system.calculate_payment(student_id, amount)
                print(f"Payment of ${amount:.2f} processed.")

            elif choice == '5':
                student_id = input("Enter Student ID: ")
                balance_info = system.check_student_balance(student_id)
                print(balance_info)

            elif choice == '6':
                courses_info = system.show_courses()
                for c in courses_info:
                    print(f"ID: {c[0]}, Name: {c[1]}, Fee: ${c[2]:.2f}")

            elif choice == '7':
                students_info = system.show_registered_students()
                for s in students_info:
                    print(f"ID: {s[0]}, Name: {s[1]}")

            elif choice == '8':
                course_id = input("Enter Course ID: ")
                students_in_course_info = system.show_students_in_course(course_id)
                for s in students_in_course_info:
                    print(f"ID: {s[0]}, Name: {s[1]}")

            elif choice == '9':
                print("Exiting the system.")
                break

            else:
                print("Invalid option selected.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
