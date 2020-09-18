# This is an implementation of a boosted decision tree 
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn.ensemble import BaggingClassifier
from sklearn import tree



def train(train_x, train_y):
	''' This is the function carry out the boosted decision tree classifier '''

	classifier = BaggingClassifier(tree.DecisionTreeClassifier(max_depth = 19), max_samples=0.5, max_features=0.5)
	classifier.fit(train_x, train_y)

	return classifier