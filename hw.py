class SuperHero:
    people = 'people'
    fly = False
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def double(self):
        self.health_points *= 2
    def tprint(self):
        print(self.name)
    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'
    def __len__(self):
        return len(self.catchphrase)
class earth(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
    def square(self):
        self.health_points = self.health_points ** 2
        self.fly = True
    def tprint(self):
        print(self.name)
    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'
    def __len__(self):
        return len(self.catchphrase)
class air(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
    def square(self):
        self.health_points = self.health_points ** 2
        self.fly = True
    def tprint(self):
        print(self.name)
    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'
    def __len__(self):
        return len(self.catchphrase)
class villain(air):
    people = 'monster'
    def gen_x(self):
        pass
    def crit(self):
        self.damage = self.damage ** 2
    def tprint(self):
        print(self.name)
    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'
    def __len__(self):
        return len(self.catchphrase)
Hero = SuperHero('Mark', 'Mirage', 'Fire bending', 100, "Where there's smoke, there's fire.")
Hero.tprint()
Hero.double()
print(str(Hero))
print(len(Hero))
Hero2 = air('Angela', 'Angel', 'Air bending', 100, 'Time to fly!', 10)
Hero2.tprint()
Hero2.square()
print(str(Hero2))
print(len(Hero2))
Hero3 = earth('Ben', 'The Rock', 'Earth bending', 100, 'Eruption!', 2)
Hero3.tprint()
Hero3.square()
print(str(Hero3))
print(len(Hero3))
Villain = villain('Dan', 'Ghost', 'Shapeshifting', 100, 'Good night.', 1)
Villain.tprint()
Villain.square()
print(str(Villain))
print(len(Villain))