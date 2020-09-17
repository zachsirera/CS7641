# This is an implementation of a boosted decision tree 
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn.ensemble import BaggingClassifier
from sklearn import tree



def train(folds_x, folds_y):
	''' This is the function carry out the boosted decision tree classifier '''

	folds = len(folds_x)
	classifiers = []
	fold_list = gen_fold_list(folds)

	for i in range(folds):

		training_x_folds = []
		training_y_folds = []

		for j in fold_list[i]: 	
			training_x_folds += folds_x[j]
			training_y_folds += folds_y[j]

		classifier = BaggingClassifier(tree.DecisionTreeClassifier(max_depth = 2), max_samples=0.5, max_features=0.5)
		classifier.fit(training_x_folds, training_y_folds)
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