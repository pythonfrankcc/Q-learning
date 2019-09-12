#use of docstrings as a compliance with pep 8 standards
'''creation of a sequential ANN model'''


#import necessary dependencies
import keras
from keras.models import Sequential
from keras import backend as K 
from keras.layers.core import Dense
from keras.layers import Activation
from keras.optimizers import Adam
from keras.metrics import categorical_cross entropy 

#creating a variable called model and setting it to an instance of a sequential object
model = Sequential(layers)

#dense layers are the regular hidden layers found between the input and output

layers = [
     Dense(16, input_shape = (1,), activation = 'relu'),#input layer with one nodes and the dense layer with 16 nodes
     Dense(32, activation = 'relu'),#hidden layer with 32 nodes
     Dense(2, activation = 'sigmoid')#creating the output layer with only two nodes
]

#compiling the model
'''Adam is a special case of the SGD optimizer and lr is the learning rate attached to the optimizer'''
model.compile(
	Adam(lr = 0.001),
	loss = 'sparse_categorical_crossentropy',
	metrics = ['accuracy']#since the problem at hand is a supervised learning task
	)

#fitting the model
model.fit(
	scaled_train_samples,#numpy array with training samples
	train_labels,#numpy array with labels
	validation_split = 0.2,#splittig 0.2% of the training data to be used as validation data
	batch_size = 10,#no of training samples passed as the input per iteration
	epochs = 20,# no of times the full dataset is going to be passed through the neural net
	shuffle = True,#data should be shuffled before being passed into the network to avoid overfitting
	verbose = True #indicates how much logging information we get to see
	)
