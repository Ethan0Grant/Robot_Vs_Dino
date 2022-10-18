
class Robot:
    def __init__(self, name, health, attack_weapon):
        self.name = name
        self.health = health
        self.attack_weapon = attack_weapon
    
    def attack(self, dinosaur):
        dinosaur.lower_health(self.attack_weapon.attack_power)
        if dinosaur.health < 0:
            dinosaur.health = 0
        print ("{} attacked {} for {} damage with {}. {}'s health is now {}\n".format(self.name,dinosaur.name,self.attack_weapon.get_attack_power(),self.attack_weapon.name,dinosaur.name,dinosaur.health))
    def lower_health(self, amount):
        self.health = self.health - amount   

    def get_health(self):
        return self.health