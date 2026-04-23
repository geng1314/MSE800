class Student:
    def set_data(self, name, age, sid):
        self.name = name
        self.age = age
        self.student_id = sid


def collect_students():
    students = []
    for i in range(3):
        sid = input("id: ")
        name = input("name: ")
        age = input("age: ")
        
        student = Student()
        student.set_data(name, age, sid)
        students.append(student)
    return students

def display(students):
    sorted_students = sorted(students, key=lambda s: s.age)
    for s in sorted_students:
        print(f"name: {s.name}, age: {s.age}, id: {s.student_id}")

if __name__ == "__main__":
    collect_data = collect_students()
    print("Students sorted by age:")
    display(collect_data)
