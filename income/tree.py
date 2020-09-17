# This is an implementation of a decision tree 
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn import tree
import matplotlib.pyplot as plt
import math




def tune(train_x, train_y, test_x, test_y, depth):
	''' This is a function to tune the tree depth in an attempt to maximize the rate at which the decision tree correctly classifies wine '''

	results = []

	for i in range(1, depth):
		decision_tree = train_2(train_x, train_y, depth)
		pct_correct = test(decision_tree, test_x, test_y)
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

	classifier = tree.DecisionTreeClassifier(max_depth = 19)
	classifier = classifier.fit(x, y)

	return classifier

def train_2(x, y, depth):
	''' This is a function to train the decision tree on the parsed data '''

	classifier = tree.DecisionTreeClassifier(max_depth = depth)
	classifier = classifier.fit(x, y)

	return classifier

def test(classifier, test_x, test_y):
	''' ''' 

	total, correct = 0, 0

	for index, each in enumerate(test_x):
		total += 1
		result = classifier.predict([each])
		if result == test_y[index]:
			correct += 1

	return round(correct / total, 3)

