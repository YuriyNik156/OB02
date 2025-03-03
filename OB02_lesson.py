class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} кушает")

    def sing(self):
        print(f"{self.name} поет - чирик")

    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас птицы")

class Pigeon(Bird):
    def __init__(self, name, voice, color, favourite_food):
        super().__init__(name, voice, color)
        self.favourite_food = favourite_food

    def sing(self):
        print(f"{self.name} поет - курлык курлык")

    def wolk(self):
        print(f"{self.name} гуляет")

bird1 = Pigeon("Гоша", "Курлык", "Серый", "Хлебные крошки")

bird2 = Bird("Маша", "Чирик", "Коричневый")

bird1.sing()
bird1.info()
bird1.wolk()
