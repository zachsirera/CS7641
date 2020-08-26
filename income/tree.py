# This is an implementation of a decision tree 
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn import tree
import matplotlib.pyplot as plt
import math




def tune(training_data, testing_data, depth):
	''' This is a function to tune the tree depth in an attempt to maximize the rate at which the decision tree correctly classifies wine '''

	results = []

	for i in range(1, depth):
		pct_correct = main_2(training_data, testing_data, i)
		results.append({'depth': i, 'success rate': round(pct_correct, 3)})

	return results



def visualize(classifier):
	''' this is a function to visualize the decision tree '''
	fn = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", 
	"total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]
	cn = ['3', '4', '5', '6', '7', '8', '9']
	tree.plot_tree(classifier, feature_names = fn, class_names = cn)
	plt.show()



def train(x, y):
	''' This is a function to train the decision tree on the parsed data '''

	classifier = tree.DecisionTreeClassifier(max_depth = 2)
	classifier = classifier.fit(x, y)

	return classifier

