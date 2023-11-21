class Bank:
    def __init__(self, name, money, balance2):
        self._name = name
        self._balance = money
        self.balance2 = balance2
    def moneyX(self):
        balance = int(input('enter your addon: '))
        self._balance += balance
    def _kill(self):
        self._balance = 0
    def __jackpot(self):
        self._balance *= 10
    def _jackpot(self):
        self.__jackpot()
    def _add(self):
        self._balance += self.balance2
    def get_balance(self):
        return self._balance
a = Bank('Murat', 0, 120)
a.moneyX()
a._kill()
a._jackpot()
a._add()
print(a._name)
print(a.get_balance())
class calc:
    def __init__(self, a, b, sign):
        self.a = a
        self.b = b
        self.sign = sign
    def a1(self):
        self.a = int(input('Enter first number: '))
    def b1(self):
        self.b = int(input('Enter second number: '))
    def sign1(self):
        self.sign = input('Enter sign: ')
    def __add__(self, other):
        return calc(self.a + other.b, self.b, self.sign)
    def __sub__(self, other):
        return calc(self.a - other.b, self.b, self.sign)
    def __mul__(self, other):
        return calc(self.a * other.b, self.b, self.sign)
    def __truediv__(self, other):
        return calc(self.a / other.b, self.b, self.sign)
equation = calc(0, 0, 'O')
equation.a1()
equation.b1()
equation.sign1()
if equation.sign == '+':
    result = equation + equation
elif equation.sign == '-':
    result = equation - equation
elif equation.sign == '*':
    result = equation * equation
elif equation.sign == '/':
    result = equation / equation
print(result.a)