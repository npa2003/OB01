class Warrior ():
    def __init__(self, name, power, endurance, hair_color): #name — переменная с именем, power — сила, endurance — выносливость, hair_color — цвет волос.
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2 # добавляем выносливости персонаж отдыхает и восстанавливается

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1 # добавляем ему силу

    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance -= 6 # после удара выносливость уменьшается

    def info(self): # информация о воине
        print('Информация о воине:')
        print(f"Имя         - {self.name}")
        print(f"Цвет волос  - {self.hair_color}")
        print(f"Сила        - {self.power}")
        print(f"Выносливость- {self.endurance}")


war1 = Warrior("Стёпа", 76, 54, "Коричневый")
print(war1)
print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_color)

war2 = Warrior( "Егор", 45, 23, "Блондин")

print(war1.endurance)
war1.sleep()
print(war1.endurance)

war1.info()
war2.info()
