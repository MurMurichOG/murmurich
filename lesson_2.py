# классы - свойства

class Car:  # Супер класс,родительский класс
    car = True

    def __init__(self, marks='BMW', color='black', age=2013):
        self.marks = marks
        self.color = color
        self.age = age

    def age1(self):
        self.age += 3


a = Car('mers', 'white', 2090)




# print(a.age1())
# print(reversed(a.age))

# парадигмы ооп
# 4 наследование, полиморфизм , инкапсуляция, абстракция
# DRY

class Car2(Car):  # дочерний класс
    def __init__(self, marks='BMW', color='black', age=2013, speed=280):
        # Car.__init__(self,marks,color,age)
        super().__init__(marks, color, age)
        self.speed = speed

    def speed(self):
        print('run', self.marks)

    def age2(self):
        Car.age1(self)
        super().age1()
        self.age1()
        print(self.age)

    def age1(self):
        self.age += 4


a1 = Car2('msk', 'a', 1999)
# a1.speed()
a1.age1()
print(a1.age)
a1.age2()

# Car2.speed(a)