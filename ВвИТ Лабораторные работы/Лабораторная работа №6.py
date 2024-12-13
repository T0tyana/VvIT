# Задание 1
class UserAccount:
    def __init__(self, name, email, password):
        self.username = name
        self.email = email
        self.__password = password

    def _set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password_in):
        return self.__password == password_in


name = input('Введите имя пользователя: ')
email = input('Введите электронную почту: ')
password = input('Введите пароль: ')
obj = UserAccount(name, email, password)
print()

#?????????????????????
#obj.__password = 'banana'
#print(obj.__password)
#?????????????????????

# Замена пароля
new_password = input('Введите новый пароль: ')
obj._set_password(new_password)
print()

# Проверка пароля
print(obj.check_password('haski4'))
print(obj.check_password('Korgi55'))
print()



# Задание 2
class Vehicle:
    make = 'Geely'
    model = 'Atlas Pro'

    def get_info(self):
        print(f'Марка машины: {self.make}\nМодель машины: {self.model}')

class Car(Vehicle):
    fuel_type = '95 pulsar'

    def get_info(self):
        print(f"Марка: {self.make}\nМодель: {self.model}\nТип топлива: {self.fuel_type}")

obj_two = Car()
obj_two.get_info()