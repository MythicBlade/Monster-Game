from numpy import random

class Entity():
    def __init__(self,xpos, ypos, symbol, number, reward, onehot = 0, artpath = ''):
        self.xpos = xpos
        self.ypos = ypos
        self.symbol = symbol
        self.number = number
        self.reward = reward
        self.artlpath = artpath
        self.onehot = onehot

    def update(self, direction, magnitude = 1):
        # updates the entity's position based on the direction given
        if direction == 0:
            self.ypos -= magnitude
        elif direction == 1:
            self.xpos -= magnitude
        elif direction == 2:
            self.ypos += magnitude
        elif direction == 3:
            self.xpos += magnitude

    def draw(self):
        # draws the entity
        # currently not implimented 
        pass


class Monster(Entity):
    def __init__(self, xpos, ypos, symbol, number, reward, onehot = 0, artpath=''):
        super().__init__(xpos, ypos, symbol, number, reward, onehot, artpath)
    
    def monsterAI(self):
        # returns the monsters evaluation of all four moves. In this case that is random
        return random.rand(4)