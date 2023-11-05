# def sum1(num1, num2):
#     return num1 + num2
# print(sum1(1, 3))
class Human:
    head = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def tprint(self):
        print(self.name, self.age, self.head)
    def summ(self):
        self.age += 15
        print(self.name, self.age)
    def __str__(self):
        return f'{self.name}, {self.age}'
    def __len__(self):
        return len(self.name)
human = Human('beka', 20)
human2 = Human('erbol', 18)
human3 = Human('malik', 16)
# print(human.name, human.head)
# print(human2.name, human.head)
# print(human3.name, human.head)
# human.tprint()
# human2.tprint()
# human3.tprint()
# human.summ()
# human2.summ()
# human3.summ()
print(len(human))
