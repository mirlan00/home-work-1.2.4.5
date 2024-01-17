import sqlite3

connect = sqlite3.connect('transport_car.db')
cursor = connect.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,   
            marka VARCHAR(255),
            model VARCHAR(255),
            year INTEGER ,
            description TEXT,
            status TEXT DEFAULT 'На обслуживании'
        );''')
connect.commit()


# Добавление нового автомобиля на обслуживание
def add_car(marka, model, year, description):
    connect = sqlite3.connect('transport_car.db')
    cursor = connect.cursor()
    cursor.execute('''
        INSERT INTO cars (marka, model, year, description) VALUES (?, ?, ?, ?)
    ''', (marka, model, year, description))
    connect.commit()
    

def update_cars(car_id, marka, model, year, description, status):
    connect = sqlite3.connect('transport_car.db')
    cursor = connect.cursor()
    cursor.execute('''
        UPDATE cars SET marka=?, model=?, year=?, description=?, status=? WHERE id=?
    ''', (marka, model, year, description, status, car_id))
    connect.commit()

def all_cars():
    connect = sqlite3.connect('transport_car.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM cars WHERE status="На обслуживании"')
    cars = cursor.fetchall()
    connect.close()
    return cars

def complect_cars():
    connect = sqlite3.connect('transport_car.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM cars WHERE status="Готово к выдаче"')
    cars = cursor.fetchall()
    connect.close()
    return cars

def main():

    while True:
        print("1 - Добавить Авто, 2 - Обновить информацию об автомобиле , 3 - Посмотреть авто , 4 - Просмотр завершенных авто , 5 - выйти ")

        commands = input("Выберите действие : ")

        if commands == '1':
            marka = input("Марка : ")
            model = input("Модель : ")
            year = int(input("Год выпуска: "))
            description = input("Описание работ: ")
            add_car(marka, model, year, description)
            print("Автомобиль добавлен ")

        elif commands == '2':
            car_id = int(input("Введите номер автомобиля для обновления: "))
            marka = input("Марка автомобиля: ")
            model = input("Модель автомобиля: ")
            year = int(input("Год выпуска: "))
            description = input("Описание работ: ")
            status = input("Новый статус: ")
            update_cars(car_id, marka, model, year, description, status)
            print("Информация об автомобиле обновлена")

        elif commands == '3':
            cars = all_cars()
            print("Список автомобилей на обслуживании:")
            for car in cars:
                print(car)

        elif commands == '4':
            completed_cars = complect_cars()
            print("Список завершенных автомобилей:")
            for car in completed_cars:
                print(car)

        elif commands == '5':
        
            break
        else:
            print("Незнакомая команда пожалуйста выберите действие")
main()

