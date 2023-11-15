import numpy as np
import entitys
from json import dump
from color import Colors

class Game():
    def __init__(self, xdim, ydim, treasurecount, seed = None, debugMode = False,monsterExists = True):
        # seed the rng for saving or use the provided seed
        if seed == None:
            self.seed = np.random.seed(np.random.randint(100000000))
        else:
            self.seed = seed
        # set up the attributes of this game now that rng is set
        self.xdim = xdim
        self.ydim = ydim
        self.treasureCount = treasurecount
        self.BoardState = np.zeros((self.xdim,self.ydim),dtype = int)
        self.lastBoardState = np.zeros((self.xdim,self.ydim),dtype = int)
        self.moveList = []
        self.turnCount = 0
        self.debugmode = debugMode
        self.monsterExists = monsterExists
        self.score = 0 
        self.gameEnding = 0
        self.symbolDict = {0:'.'}
        #set up the entity lists
        self.entityList = []
        self.entityLocationList = [] #This is only used for making the starting board its afterwards we can ignore it
        
        #set up the treasures
        for n in range(self.treasureCount):
            pos = self.randomEmptyLocation()
            treasure = entitys.Entity(pos[0],pos[1],f'{Colors.YELLOW}T{Colors.END}',3,0.1)
            self.entityList.append(treasure)
            self.entityLocationList.append(pos)
        
        #set up the player
        pos = self.randomEmptyLocation()
        self.player = entitys.Entity(pos[0],pos[1],f'{Colors.BLUE}{Colors.BOLD}H{Colors.END}',1,0)
        self.entityList.append(self.player)
        self.entityLocationList.append(pos)

        #set up the Monster
        
        if self.monsterExists:
            pos = self.randomEmptyLocation()
            self.monster = entitys.Monster(pos[0],pos[1],f'{Colors.RED}M{Colors.END}',2,-1)
            self.entityList.append(self.monster)
            self.entityLocationList.append(pos)

        # Update the boardstate
        self.updateBoardstate()
        # make the dictionary of entity symbols
        self.entitySymbolDict()


    def randomEmptyLocation(self):
        # returns a tuple in (x,y) format from a random empty position on the board
        # throws an error if there are no spaces left
        location = (np.random.randint(self.xdim), np.random.randint(self.ydim))
        assert (len(self.entityLocationList) <= (self.xdim * self.ydim)), 'There are too many Entities'
        while location in self.entityLocationList:
            location = (np.random.randint(self.xdim), np.random.randint(self.ydim))
        return location

    def updateBoardstate(self):
        # makes an updates boardstate using the data from entities
        # the 
        self.lastBoardState = self.BoardState
        self.BoardState = np.zeros((self.xdim,self.ydim),dtype = int)
        for a in self.entityList:
            self.BoardState[a.xpos][a.ypos] = a.number
    
    def entitySymbolDict(self):
        # creates a dictionary of numbers and the corresponding symbols for entities
        for a in self.entityList:
            if a.number not in self.symbolDict:
                self.symbolDict[a.number] = a.symbol

    def printBoard(self):
        #prints out the board to terminal
        for y in range(self.ydim):
            line = []
            for x in range(self.xdim):
                line.append(self.symbolDict[self.BoardState[x][y]])
                line.append(' ')
            print(''.join(line))

    def collisionCheck(self):
        # returns the reward of any colliding entities and index of the entity itself in format (reward, index) or (0,0) if nothing is colliding
        i = 0
        for e in self.entityList:
            if (self.player.xpos == e.xpos) and (self.player.ypos == e.ypos) and (e.number != 1): #check if index is the same and the entity isn't the player
                return (e.reward, i)
            i += 1
        return (0,0)

    def checklegalmoves(self, xpos, ypos):
        # returns the 
        eval = np.ones(4)
        if xpos == 0:
            eval[1] = 0
        elif xpos == self.xdim - 1:
            eval[3] = 0
        if ypos == 0:
            eval[0] = 0
        elif ypos == self.ydim - 1:
            eval[2] = 0
        return eval

    def updateGame(self, direction):
        #moves player if not near wall
        if self.checklegalmoves(self.player.xpos, self.player.ypos)[direction] == 1:
            self.player.update(direction)
        if self.monsterExists:
            #moves monster
            self.monster.update(np.argmax(self.monster.monsterAI() * self.checklegalmoves(self.monster.xpos,self.monster.ypos)))
        #check collision
        collision = self.collisionCheck()
        if collision[0] == -1:
            self.gameEnding = -1
        if collision[0] == 0.1:
            self.score += 1
            del self.entityList[collision[1]]
            if len(self.entityList) <= 2:
                self.gameEnding = 1
        self.moveList.append(direction)
        self.turnCount += 1
        self.updateBoardstate()
        return collision[0]
    
    def saveGame(self):
        # saves the game as a json file
        dict = {'seed': self.seed,'dimensions':(self.xdim,self.ydim),'treasure count': self.treasureCount,'moves':self.moveList}
        dump(dict,'Monster Game 2\saves')
        
