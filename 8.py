'''
Полиморфизм — очень важная идея в программировании. 
Она заключается в использовании единственной 
сущности(метод, оператор или объект) для представления 
различных типов в различных сценариях использования.
'''

print('Полиморфизм оператора сложения')
num1 = 1
num2 = 2
print(num1 + num2)

str1 = "Python"
str2 = "Programming"
print(str1 + " " + str2)

print('Полиморфизм функций')
print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

print('Полиморфизм в классах')
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()