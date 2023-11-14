from tensorflow import keras as ks
from numpy import array

class NeuralNet():
    def __init__(self,xdim, ydim, modelPath = '',onehot = True):
        if modelPath == '':
            if onehot:
                self.model = ks.Sequential([
                        ks.layers.InputLayer(input_shape=(15,15,3)),
                        ks.layers.Dense(xdim*ydim, activation='relu'),
                        ks.layers.Dense(xdim*ydim, activation='relu'),
                        ks.layers.Dense(4)])  #One output for each board direction
            else:
                self.model = ks.Sequential([
                        ks.layers.InputLayer(input_shape=(15,15)),
                        ks.layers.Dense(xdim*ydim, activation='relu'),
                        ks.layers.Dense(xdim*ydim, activation='relu'),
                        ks.layers.Dense(4)])  #One output for each board direction
        else:
            self.model = ks.models.load_model(modelPath)
        self.model.compile(optimizer='adam', loss='mse')

    def modelEvaluation(self,boardState):
        # returns the networks evaluation of all four moves as a vector.
        eval= self.model.predict(array([boardState]))[0]
        return eval[0]

    def updateModel(self,state, qValues):
        # updates the model with the new information provided
        self.model.train_on_batch(array([state]),array([qValues]))