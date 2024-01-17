from abc import ABC, abstractmethod

class GeeksPeople(ABC):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    @abstractmethod
    def __str__(self):
        pass

class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"Студент {self.student_id} учится в группе {self.group_where_study}")

    def __str__(self):
        return f"Студент: {self.name} ({self.student_id}), Email: {self.email}, Phone: {self.phone}"

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f"Учитель {self.teacher_id} преподаёт в группе {self.group_where_teach}")

    def __str__(self):
        return f"Учитель: {self.name} ({self.teacher_id}), Почта: {self.email}, Телефон: {self.phone}"

class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id

    def create_group(self):
        print(f"Админ {self.admin_id} создаёт новую группу")

    def __str__(self):
        return f"Админ: {self.name} ({self.admin_id}), Почта: {self.email}, Телефон: {self.phone}"

class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)

    def mentor_info(self):
        print(f"Mentor {self.name} ({self.teacher_id}) mentors in group {self.group_where_teach}")

    def __str__(self):
        return f"Mentor: {self.name} ({self.student_id}, {self.teacher_id}), Почта: {self.email}, Телефон: {self.phone}"

student1 = Student("Кыял", "kyial@gmail.com", "123456789", "s 123", "Компьюиорное инженерия")
teacher1 = Teacher("Максат", "maksat@gmail.com", "987654321", "T 456", "Математика")
admin1 = Admin("Админ", "admin@gmail.com", "555666777", "A789")
mentor1 = Mentor("Ментор", "mentor@gmail.com", "111222333", "M123", "Ментор", "T789", "Учитель")

print(student1)
student1.study()

print(teacher1)
teacher1.teach()

print(admin1)
admin1.create_group()

print(mentor1)
mentor1.study()
mentor1.teach()
mentor1.mentor_info()
