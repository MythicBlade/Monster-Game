import keras as ks
from numpy import array

class NeuralNet():
    def __init__(self,xdim, ydim, modelPath = ''):
        if modelPath == '':
            self.model = ks.Sequential([
                    ks.layers.Dense(xdim*ydim, activation='relu'),
                    ks.layers.Dense(xdim*ydim, activation='relu'),
                    ks.layers.Dense(4)])  #One output for each board position#
        else:
            self.model = ks.models.load_model(modelPath)
        self.model.compile(optimizer='adam', loss='mse')

    def modelEvaluation(self,boardState):
        # returns the networks evaluation of all four moves as a vector.
        return self.model.predict(boardState)[0]
    
    def updateModel(self,state, qValues):
        # updates the model with the new information provided
        self.model.train_on_batch(array([state]),array([qValues]))