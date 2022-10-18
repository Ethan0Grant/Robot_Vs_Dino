class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, robot):
        robot.lower_health(self.attack_power)
        if robot.health < 0:
            robot.health = 0
        print("{} scratched {}, dealing {} damage. {}'s health is now {}\n".format(self.name, robot.name, self.attack_power, robot.name, robot.health))
                                                                                 
   
                                                                                 
    def lower_health(self, amount):
        self.health = self.health - amount

    def get_health(self):
        return self.health