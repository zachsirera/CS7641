# This is an implementation of a k-nearest neighbors
# Zach Sirera - Fall 2020

# import files from the root directory
import data

# import the necessary external libraries
from sklearn.neighbors import KNeighborsClassifier




def tune(training_data, testing_data, k):
	''' this is a function to tune the knn classifier by tweaking k to maximize the success rate '''
	results = []

	train_x, train_y = data.parse(training_data)
	test_x, test_y = data.parse(testing_data)

	for i in range(10, k, 10):
		classifier = train(train_x, train_y, i)
		pct_correct = test(classifier, test_x, test_y)
		results.append({'k': i, 'success rate': round(pct_correct, 3)})

	return results



def train(folds_x, folds_y):
	''' this is the function to train the knn classifier '''

	folds = len(folds_x)
	classifiers = []
	fold_list = gen_fold_list(folds)

	for i in range(folds):

		training_x_folds = []
		training_y_folds = []

		for j in fold_list[i]: 	
			training_x_folds += folds_x[j]
			training_y_folds += folds_y[j]

		classifier = KNeighborsClassifier(n_neighbors = 400)
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