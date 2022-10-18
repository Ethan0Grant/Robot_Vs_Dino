import Robot
import Dinosaur
import Weapon
import Fleet
import Herd
import random

class Battlefield:
    def __init__(self):
       self.team = None
       self.fleet = None
       self.herd = None
       self.weapons = None
       self.game_state = None
       self.winner = None
       self.rnames = ["Zorg", "Zig", "Zag", "B222B2B2B22", "R2D2", "Toaster", "Easybake-Oven", "USB I found in the street"]
       self.dnames = ["T-Rex", "Stegosaurus", "Velociraptor", "Spinosaurus", "Giganotosaurus", "Utahraptor"]
       self.wnames = ["Brick","Stick", "Orbital Strike", "Your Grandma's Purse", "An actual crayon", "Duct tape","McDonald's Coffee", "A stolen cane", "Hotpockets"]

                       

 
    def pregame_setup(self):
        
        section0 = random.randint(0, len(self.rnames) - 4)
        section1 = random.randint(0, len(self.rnames) - 4)
        section2 = random.randint(0, len(self.rnames) - 4)
        self.rnames = self.rnames[section0:section0 + 3]
        self.dnames = self.dnames[section0:section1 + 3]
        self.weapons = [Weapon.Weapon(wname, random.randint(0, 50)) for wname in self.wnames]
        self.herd = Herd.Herd([Dinosaur.Dinosaur(dname, random.randint(50, 100), random.randint(0, 50)) for dname in self.dnames])
        self.fleet = Fleet.Fleet([Robot.Robot(rname, random.randint(50, 100), random.choice(self.weapons)) for rname in self.rnames])
        
        
    
    def display_welcome(self):
        print("    -------------------------------------------------------    \n" +
              "    ///////////////////////////////////////////////////////    \n" +
              "    -------------------------------------------------------    \n" +
              "    [----] WELCOME TO ROBOT VS DINO BATTLE SIMULATOR [----]    \n" +
              "    -------------------------------------------------------    \n" +
              "    ///////////////////////////////////////////////////////    \n" +
              "    -------------------------------------------------------    \n" + 
              dinoart
              )
                                                  
    
    
    def display_winner(self):
        print("----------------------\n"+
              "  {} WON THE GAME!\n".format(self.winner) + 
              "----------------------\n")


   
    def battle_phase(self):
        while self.herd.dinos and self.fleet.bots:
              self.herd.dinos[0].attack(self.fleet.bots[0])
              self.fleet.remove_dead()
              if not self.fleet.bots:
                break
              self.fleet.bots[0].attack_weapon = random.choice(self.weapons)
              self.fleet.bots[0].attack(self.herd.dinos[0])
              self.herd.remove_dead()
        if self.herd.dinos:
          self.winner = "DINOSAURS"
       
        elif self.fleet:
          self.winner = "ROBOTS" 
        
        else:
          self.winner = "NOBODY"

              
         
         
         
          

    
    def run_game(self):
        self.display_welcome()
        self.pregame_setup()
        self.battle_phase()
        self.display_winner()













































dinoart = """
                                                                                                    ░░                  
                                                                                                  ▒▒▓▓██▒▒              
                                                                                                ▓▓▓▓▓▓▓▓▓▓░░▒▒  ░░      
                                                                                            ▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓  
    ░░▒▒░░                                                        ░░▒▒▒▒▒▒▒▒░░          ▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒
  ▒▒▒▒▒▒▒▒▒▒                                            ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓  ░░▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒
▒▒      ▒▒▒▒▓▓▓▓░░                                ░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░
          ░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░            ██  ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒░░▒▒░░▓▓▓▓░░
              ░░▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒░░░░░░▒▒▒▒░░▓▓▒▒██▓▓  ░░░░░░░░  
                  ░░▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░▓▓▒▒▒▒▓▓░░            
                        ▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒▓▓▒▒░░░░░░▒▒▓▓▒▒░░▒▒░░            
                            ▒▒▒▒░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░▒▒▒▒              
                                ░░▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒░░▒▒      ░░░░▒▒▒▒▒▒▒▒              
                                        ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░            ░░░░░░░░▒▒▒▒            
                                        ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒  ▒▒██              ░░░░░░▒▒░░              
                                        ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▒▒▓▓▒▒▒▒▓▓                ░░▒▒▒▒░░░░            
                                      ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓████▓▓▓▓██▓▓░░  ▒▒▒▒▒▒▓▓                ▒▒▒▒▒▒░░            
                                    ██▓▓▓▓▓▓▓▓▓▓    ▒▒▒▒      ▓▓▓▓▓▓▓▓██      ▓▓  ▒▒▓▓                                  
                                    ▓▓▓▓▓▓▓▓▓▓▓▓              ▓▓▓▓▓▓▓▓██        ░░  ▓▓                                  
                                  ░░▓▓▓▓▓▓██▓▓              ▒▒▓▓▓▓▓▓██              ▓▓                                  
                                  ▓▓▓▓████░░                ▒▒▓▓▓▓▓▓▓▓                                                  
                                ░░██▓▓██                    ░░▓▓▓▓▓▓                                                    
                                ▓▓▓▓██▓▓                    ▓▓▓▓▓▓                                                      
                                ▓▓▓▓▓▓██                    ▓▓▓▓▓▓                                                      
                                ▓▓▓▓▓▓▓▓                    ▓▓▓▓▓▓                                                      
                                ▒▒▓▓██▓▓                  ░░▓▓▓▓▓▓                                                      
                                ▓▓▓▓▓▓▓▓▒▒                ░░▓▓▓▓▓▓░░                                                    
                              ░░▓▓▓▓▓▓▓▓██                  ░░▓▓▓▓▓▓▓▓░░                                                
                                ▓▓▓▓▒▒▓▓▓▓▓▓▓▓              ░░▓▓██▓▓▓▓▓▓▓▓▒▒                                            
                              ░░▓▓░░▒▒▒▒▒▒▓▓▒▒░░          ░░░░████▒▒▓▓▓▓▓▓▓▓▓▓                                          
                              ▒▒▓▓░░▒▒▓▓██▓▓░░                ░░▓▓▓▓▓▓▓▓██▓▓▒▒░░                                        
                              ░░██░░                            ░░░░░░▓▓██░░                                            
"""