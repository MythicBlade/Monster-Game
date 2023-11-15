import Game
import neural_net
import numpy as np



class Manager():
    def __init__(self):
        pass

    def playAsPerson(self):
        # Allows you to play the game
        game = Game.Game(15,15,15)
        game.printBoard()
        
        while game.gameEnding == 0:
            direction = self.getinput()
            game.updateGame(direction)
            game.printBoard()
        print(game.score)
        print('\nGame Over!\n')
        

    def getinput(self):
        # gets a valid input for direction
        # note this just means something that can be read a direction it doesn't check for walls
        validinputs = {'0':0, '1':1, '2':2, '3':3, 'w':0, 'a':1, 's':2, 'd':3}
        direction = input('type direction: ')
        while not (direction in validinputs):
            print('that is not a Valid direction')
            direction = input('type direction: ')
        return validinputs[direction]
        

    def trainAI(self, epochNumber, gamma, inEpsilon, epsilonDecay, minEpsilon, maxTurnCount, treasureCount, xdim, ydim, showGame = False, monsterExists = True):
        epsilon = inEpsilon
        model = neural_net.NeuralNet(xdim,ydim,)
        trainingStats = np.zeros(epochNumber)
        for n in range(epochNumber):
            game = Game.Game(xdim,ydim,treasureCount,monsterExists=monsterExists)
            if showGame:
                # show the game if the flag is set to do that
                game.printBoard()
            gameOver = False
            while not gameOver:
                if np.random.random() <= epsilon:
                    # exploration or random choices
                    choice = np.random.rand(4)
                else:
                    # exploitation or choosing the best options
                    choice = model.modelEvaluation(game.BoardState)
                # update epsilon
                epsilon = max(epsilon * epsilonDecay, minEpsilon)

                # update the game
                reward = game.updateGame(np.argmax(choice))
                # calculate the evaluation for our program to train on unless it won or died
                if game.gameEnding in [1,-1]:
                    gameReward = game.gameEnding
                else:
                    gameReward = reward + gamma + np.max(model.modelEvaluation(game.BoardState))
                # setup the q values for training
                choice[game.moveList[-1]] = gameReward
                # train the Model
                model.updateModel(game.lastBoardState, choice)
                # check if the game is over
                if game.turnCount >= maxTurnCount:
                    gameOver = True
                if game.gameEnding != 0:
                    gameOver = True
                if showGame:
                # show the game if the flag is set to do that
                    game.printBoard()
            #print out the score so we know how it's going
            print(f'The Score for game {n} was {game.score}.')
            trainingStats[n] = game.score
        return trainingStats
            
            
            
                


