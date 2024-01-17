
class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def print_info(self):
        print(f"Студент: {self.first_name} {self.last_name}")
        print(f"Номер студенческого билета: {self.student_id}")
        print(f"Курсы: {', '.join(self.courses)}")


s = Student("Кыял", "Максат уулу", "123456")
s.add_course("Информатика")
s.add_course("Физика")
s.print_info()  
s.remove_course("Математика")
s.print_info()  

class Library:
    def __init__(self):
        self.books = []  # пустой список

    def add_book(self, title, author):
        book = {"title": title, "author": author, "status": "доступна"}
        self.books.append(book)

    def remove_book(self, title, author):
        for book in self.books:
            if book["title"] == title and book["author"] == author:
                self.books.remove(book)
                return
        print("Книга не найдена")

    def g_book(self, title, author):
        for book in self.books:
            if book["title"] == title and book["author"] == author:
                if book["status"] == "доступна":
                    book["status"] = "выдана"
                    return
                else:
                    print("Книга уже выдана")
                    return
        print("Книга не найдена")

    def return_book(self, title, author):
        for book in self.books:
            if book["title"] == title and book["author"] == author:
                if book["status"] == "выдана":
                    book["status"] = "доступна"
                    return
                else:
                    print("Книга не выдана")
                    return
        print("Книга не найдена")

library = Library()

# китеп кошуу
library.add_book("Самый богатый человек в Вавилоне", "Джорджа Самюэля Клейсон")
library.add_book("Думай и богатей", "Наполеон Хилл")

# китеп беруу
library.g_book("Самый богатый человек в Вавилоне", "Джорджа Самюэля Клейсон")
library.g_book("Думай и богатей", "Наполеон Хилл")

# кайра беруу
library.g_book("Самый богатый человек в Вавилоне", "Джорджа Самюэля Клейсон")

# кайтаруу
library.return_book("Самый богатый человек в Вавилоне", "Джорджа Самюэля Клейсон")
library.return_book("Думай и богатей", "Наполеон Хилл")

# очуруу
library.remove_book("Думай и богатей", "Наполеон Хилл")

# жок китепти очуруу
library.remove_book(2006, "Разумный инвестор")
