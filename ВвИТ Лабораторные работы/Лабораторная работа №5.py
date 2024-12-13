# Задание 1
class Book:

    title = "All for the Game"
    author = "Nora Sakavic"
    year = "2016"
    counter = 0

    def __init__(self):
        Book.counter += 1 # Считаем кол-во экземпляров

    def get_info(self):
        print(f"Название книги: {self.title}\nАтвор: {self.author}\nГод издания: {self.year}.")

obj_one = Book()
obj_one.get_info()
print(obj_one.counter)
obj_two = Book()
print(obj_two.counter)
obj_three = Book()
print(obj_three.counter)
print()

# Задание 2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        print(f"Радиус круга - {self.radius}")

    def set_radius(self, new_radius):
        self.radius = new_radius


obj_two = Circle(20)
obj_two.get_radius()
obj_two.set_radius(35)
print(f"Новый радиус круга - {obj_two.radius}")
print()

class Person:

     def __init__(self, dam):
         self.health = 100
         self.dam = dam


     def get_damage(self, health, dama):
         self.health = health - dama
         print(f"Стало - {self.health}")


