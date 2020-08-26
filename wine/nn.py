# This is an implementation of a neural network
# Zach Sirera - Fall 2020

# import files from the root directory
import data

# import the necessary external libraries
from sklearn.neural_network import MLPClassifier



def train(train_x, train_y):
	''' this is function to train a neural network '''

	classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 6, 5), random_state=1)
	classifier.fit(train_x, train_y)

	return classifier	



def tune():
	''' this is a function to tune the neural network by adjusting the size of the hidden layers '''
	pass
