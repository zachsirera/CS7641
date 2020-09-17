# This is an implementation of a neural network
# Zach Sirera - Fall 2020

# import files from the root directory
import data

# import the necessary external libraries
from sklearn.neural_network import MLPClassifier



def train(folds_x, folds_y):
	''' this is function to train a neural network '''

	folds = len(folds_x)
	classifiers = []
	fold_list = gen_fold_list(folds)

	for i in range(folds):

		training_x_folds = []
		training_y_folds = []

		for j in fold_list[i]: 	
			training_x_folds += folds_x[j]
			training_y_folds += folds_y[j]

		classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 6, 5), random_state=1)
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




def tune(train_x, train_y, test_x, test_y, min_layer, max_layer):
	''' this is a function to tune the neural network by adjusting the size of the hidden layers '''
	
	results = []

	for i in range(min_layer, max_layer):
		for j in range(min_layer, max_layer):
			for k in range(min_layer, max_layer):
				classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(i, j, k), random_state=1)
				classifier.fit(train_x, train_y)

				total = 0
				correct = 0

				for index, each in enumerate(test_x):
					total += 1
					result = classifier.predict([each])
					if result == test_y[index]:
						correct += 1

				results.append({'layers': (i, j, k), 'success': round(correct / total, 3)})

	return results

def gen_fold_list(k):

	a = []

	for i in range(k):
		b = []
		for j in range(k):
			if i != j:
				b.append(j)
		a.append(b)

	return a

