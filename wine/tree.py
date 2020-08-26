# This is an implementation of a decision tree 
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn import tree
import matplotlib.pyplot as plt
import math



def main(training_data, testing_data):
	''' This is the function carry out the decision tree classifier '''

	train_x, train_y = parse(training_data)
	test_x, test_y = parse(testing_data)

	decision_tree = train(train_x, train_y, 2)
	visualize(decision_tree)



def main_2(training_data, testing_data, depth):
	''' This is the function carry out the decision tree classifier '''

	train_x, train_y = parse(training_data)
	test_x, test_y = parse(testing_data)

	decision_tree = train(train_x, train_y, depth)
	pct_correct = test(decision_tree, test_x, test_y)
	
	return pct_correct



def tune(training_data, testing_data, depth):
	''' This is a function to tune the tree depth in an attempt to maximize the rate at which the decision tree correctly classifies wine '''

	results = []

	for i in range(1, depth):
		pct_correct = main_2(training_data, testing_data, i)
		results.append({'depth': i, 'success rate': round(pct_correct, 3)})

	return results



def test(decision_tree, test_x, test_y):
	''' This is a function to determine how successful the classifier is at predicting quality '''

	correct = 0
	total = 0

	for index, each in enumerate(test_x):
		total += 1
		result = predict(decision_tree, each)
		if result == test_y[index]:
			correct += 1

	return correct / total



def visualize(classifier):
	''' this is a function to visualize the decision tree '''
	fn = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", 
	"total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]
	cn = ['3', '4', '5', '6', '7', '8', '9']
	tree.plot_tree(classifier, feature_names = fn, class_names = cn)
	plt.show()



def predict(classifier, sample):
	''' this is a function to use the existing classifier to predict an outcome based on a sample'''
	return classifier.predict([sample])



def train(x, y, depth):
	''' This is a function to train the decision tree on the parsed data '''

	classifier = tree.DecisionTreeClassifier(max_depth=depth)
	classifier = classifier.fit(x, y)

	return classifier



def parse(dataset):
	''' This is a function to parse the dataset dictionary and format it properly for the decision tree algorithm implementation '''

	x = []
	y = []

	for row in dataset:
		x.append([
			float(row["fixed acidity"]), 
			float(row["volatile acidity"]),
			float(row["citric acid"]),
			float(row["residual sugar"]),
			float(row["chlorides"]),
			float(row["free sulfur dioxide"]),
			float(row["total sulfur dioxide"]),
			float(row["density"]),
			float(row["pH"]),
			float(row["sulphates"]),
			float(row["alcohol"])
		])
		y.append(int(row["quality"]))

	return x, y