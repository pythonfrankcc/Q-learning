#importing necessary dependencies

import keras
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense,Flatten
from keras.layers.convolutional import*
from keras.layers.pooling import *
#max pooling is done on a per layer basis 
#initializing both a dense layer and a convolutional layer to process the image
'''apply max pooling to get the most activated pixels,reduce complexity and also computational load'''
#remember to also use xavier initialization of weights to avoid the issue with exploding gradient or vanishing gradient
model_valid = Sequential([
	Dense(16, input_shape = (20,20,3), activation = 'relu'),# input layer with 3 nodes and a size of 20x20 followed by a dense layer with 16 nodes
	Dense(32,activation = 'relu',kernel_initializer = 'glorot_uniform'),#in situations where you want the randomly initiated weights to be by uniform distribution curve
	Conv2D(32,kernal_size = (3,3),activation = 'relu', padding = 'same'),#creation of a cnn with 32 nodes and a filter size of 3x3 and padding valid reduces the no of pixels while same makes sure that the picture remains the same size
	Conv2D(64,kernal_size = (5,5), activation = 'relu',padding = 'same'),#filter size is now 5x5
	MaxPooling2D(pool_size = (2,2), strides = 2, padding = 'valid'),
	Conv2D(128,kernal_size = (7,7),activation = 'relu',padding = 'same')#filter size is now 7x7
	Flatten(),#achieved by multiplying the dimensions the dimensions of the data from the conv layer by the no of filters in that layer
	Dense(2, activation ='softmax')
	])
#check for the model summary
 model_valid.summary()