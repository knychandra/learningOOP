class Hero:
    # creating init method
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.damage = damage

    # creating a method called attack
    def attack(self,enemy):
        enemy.health -= self.damage
        print(self.name, 'attacked', enemy.name)
        print(enemy.name +'\'s health now: ' + str(enemy.health))

shadow_fiend = Hero('Shadow Fiend', 100, 10)
mirana = Hero('Mirana', 50, 10)

# printing object(shadow_fiend)'s name
print(shadow_fiend.name)
# printing object(mirana)'s name
print(mirana.name)

# running a method called attack
shadow_fiend.attack(mirana)
