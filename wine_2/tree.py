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



def train(folds_x, folds_y):
	''' This is a function to train the decision tree on the parsed data '''

	folds = len(folds_x)
	classifiers = []
	fold_list = gen_fold_list(folds)

	for i in range(folds):

		training_x_folds = []
		training_y_folds = []

		for j in fold_list[i]: 	
			training_x_folds += folds_x[j]
			training_y_folds += folds_y[j]

		classifier = tree.DecisionTreeClassifier(max_depth = 2)
		classifier = classifier.fit(training_x_folds, training_y_folds)
		classifiers.append(classifier)

	return validate(classifiers, folds_x, folds_y)


def validate(classifiers, folds_x, folds_y):
	''' '''

	results = []

	for jindex, classifier in enumerate(classifiers):
		correct = 0
		total = 0

		for index, each in enumerate(folds_x[jindex]):
			total += 1
			result = classifier.predict([each])
			if result == folds_y[jindex][index]:
				correct += 1

		results.append(round(correct / total, 3))

	return classifiers[results.index(max(results))]


def gen_fold_list(k):

	a = []

	for i in range(k):
		b = []
		for j in range(k):
			if i != j:
				b.append(j)
		a.append(b)

	return a

