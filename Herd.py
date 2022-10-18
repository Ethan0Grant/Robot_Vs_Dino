class Herd:
    def __init__(self, dinos):
        self.dinos = []
        for dino in dinos:
            self.dinos.append(dino)

            

    def remove_dead(self):
        for dino in self.dinos:
          if dino.get_health() < 1:
            self.dinos.remove(dino)           

