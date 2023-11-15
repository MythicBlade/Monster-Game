from tensorflow import keras as ks
from numpy import array
from tensorflow import config
class NeuralNet():
    def __init__(self,xdim, ydim, modelPath = '',configPrint = False, verbose = 0):
        self.verbose = verbose
        if configPrint:
            print(f'Devices are {config.list_physical_devices("GPU")}')
        if modelPath == '':
            self.model = ks.Sequential([
                    ks.layers.Flatten(input_shape=(xdim,ydim)),
                    ks.layers.Dense(xdim*ydim, activation='relu'),
                    ks.layers.Dense(xdim*ydim, activation='relu'),
                    ks.layers.Dense(4)])  #One output for each board position#
        else:
            self.model = ks.models.load_model(modelPath)
        self.model.compile(optimizer='adam', loss='categorical_crossentropy')

    def modelEvaluation(self,boardState):
        # returns the networks evaluation of all four moves as a vector.
        return self.model.predict(array([boardState*0.3]),verbose = self.verbose)[0]
    
    def updateModel(self,state, qValues):
        # updates the model with the new information provided
        self.model.train_on_batch(array([state*0.3]),array([qValues]))