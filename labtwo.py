from peewee import SqliteDatabase, CharField, Model, ForeignKeyField, DateField, IntegerField
from random import choice, randint
from datetime import date
import sys

DB = SqliteDatabase('labtwo.sqlite')

class Clients(Model):
    name = CharField()
    city = CharField()
    address = CharField()

    class Meta:
        database = DB

class Orders(Model):
    client = ForeignKeyField(Clients)
    date = DateField()
    amount = IntegerField()
    description = CharField()

    class Meta:
        database = DB

NAMES = ["Татьяна", "Александр", "Анна", "Тимур"]
CITIES = ["Сургут", "Москва", "Санкт-Петербург", "Мурманск"]
ADDRESS = ["ул. Университетская, д. 13, кв. 15", "ул. Яузская, д. 47, кв. 295", "ул. Дворцовая Набережная, д. 38", "ул. Коминтернта, д. 392, кв. 2929"]

def main(argv):
    if len(argv) == 1 or argv[1].lower() not in ("init", "fill", "show"):
        print(
"""python 1.py [параметр]
Возможные параметры:
    init - создаёт базу данных, если не существует, иначе удаляет и создаёт заново.
    fill - заполняет таблицы случайными данными.
    show [таблица] - выводит данные из таблицы""")
        quit(1)

    command = argv[1].lower()

    DB.connect()

    if command == "init":
        if Orders.table_exists():
            print("Orders уже существует, удаляю")
            DB.drop_tables([Orders])
        if Clients.table_exists():
            print("Clients уже существует, удаляю")
            DB.drop_tables([Clients])
        print("Создаю Clients и Orders")
        DB.create_tables([Clients, Orders])
    elif command == "fill":
        for i in range(10):
            client = Clients.create(name=choice(NAMES), city=choice(CITIES), address=choice(ADDRESS))
            Orders.create(client=client, date=date(year=randint(2000, 2024), month=randint(1, 12), day=randint(1, 27)), amount=randint(1, 100), description="".join(choice("Случайное Описание")for i in range(20)))
        print("Заполнил таблицы случайными данными")
    elif command == "show":
        if len(argv) == 3:
            table_name = argv[2]
        else:
            print("Для show надо указать таблицу, пример:\npython 1.py show orders")
            DB.close()
            quit(1)
        if table_name == "orders":
            table = Orders
            print("Client | Date | Amount | Description")
            for i in table.select():
                print(f"{i.client} | {i.date} | {i.amount} | {i.description}")
        elif table_name == "clients":
            table = Clients
            print("Name | City | Address")
            for i in table.select():
                print(f"{i.name} | {i.city} | {i.address}")

    DB.close()

if __name__ == "__main__":
    main(sys.argv)