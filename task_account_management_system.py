# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников
# на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять
# пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных
# сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют
# добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

# Создание класса User с атрибутами
class User():
    def __init__(self, id, name, access_level = "сотрудник"):
        self.__id = id
        self.__name = name
        self.__access_level = access_level

    # Создание функции get для получения информации из приватных атрибутов
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Создание метода __str__ для вывода информации в виде строки
    def __str__(self):
        return f"ID: {self.__id}; имя: {self.__name}; уровень доступа: {self.__access_level}"

# создание дочернего класса Admin
class Admin(User):
    def __init__(self, id, name, access_level = "администратор"):
        super().__init__(id, name, access_level)

    # Просмотр списка сотрудников
    def view_users(self):
        return User

    # Добавление новых сотрудников
    def add_user(self, users_list, id, name):
        new_user = User(id, name)
        users_list.append(new_user)
        print(f"Пользователь {name} успешно добавлен(а). ")

    # Удаление сотрудников
    def remove_user(self, users_list, id):
        for user in users_list[ : ]:
            if user.get_id() == id:
                users_list.remove(user)
                print(f"Пользователь с ID: {id} успешно удален(а). ")
                return
        print(f"Пользователь с ID {id} не найден. ")

# Создание списка сотрудников
users = []

admin = Admin(101, "Анна Иванова")

admin.add_user(users, 102, "Борис Смирнов")
admin.add_user(users,103, "Виктория Кузнецова")
admin.add_user(users,104, "Глеб Федоров")
admin.add_user(users,105, "Дарья Соколова")
admin.add_user(users,106, "Егор Морозов")

# Итерация для вывода списка сотрудников
for user in users:
    print(user)

admin.remove_user(users, 104)

for user in users:
    print(user)