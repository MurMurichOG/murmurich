# инкапсуляция, абстракция, git clone
# уровни защиты
# публичная(public)0. _ 'защищеная' (protected) , private __
# полиморфизм, наследование
# super()
class Bank:
    def __init__(self, fullname, money, key):
        self.fullname = fullname
        self.__money = money
        self._password = key
    def getpass(self):
        print(self._password)
    def setpass(self, p):
        self._password = p
    def __mon(self):
        money = int(input('enter amount '))
        self.__money += money
    def __str__(self):
        return f'{self.fullname}, {self.__money}, {self._password}'
    def mon1(self):
        self.__mon()
    @property
    def nameis(self):
        return self._password
    @nameis.setter
    def nameis(self, name):
        self._password = name
beka = Bank('bekbolo', 0, '2525')
# beka.mon1()
print(beka.nameis)
beka.nameis = '9998'
beka.getpass()
beka.setpass('1111')
beka.getpass()
# print(beka.money)
# beka._password = '1111'
# beka.age = 20
# print(dir(beka))
# print(beka._password)
# print(beka.age)
# print(beka)
# class Tea:
#     def __init__(self, name):
#         self.name = name
#     def start(self):
#         print('getting ready...')
#         self.__start2()
#         self.__cup()
#         self._stop()
#     def __start2(self):
#         print('boiling water...')
#     def __cup(self):
#         print('the water is boiling.')
#     def _stop(self):
#         print('ready-steady.')
#
# beko = Tea('beko')
# beko.start()
