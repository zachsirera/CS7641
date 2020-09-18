# This is an implementation of a k-nearest neighbors
# Zach Sirera - Fall 2020

# import files from the root directory
import data

# import the necessary external libraries
from sklearn.neighbors import KNeighborsClassifier




def tune(train_x, train_y, test_x, test_y, neighbors):
	''' this is a function to tune the knn classifier by tweaking k to maximize the success rate '''
	results = []

	for i in range(10, neighbors):
		classifier = train_2(train_x, train_y, i)
		pct_correct = test(classifier, test_x, test_y)
		results.append({'k': i, 'success rate': round(pct_correct, 3)})

	return results



def train(x, y):
	''' this is the function to train the knn classifier '''

	classifier = KNeighborsClassifier(n_neighbors = 15)
	classifier.fit(x, y)

	return classifier


def train_2(x, y, k):
	''' this is the function to train the knn classifier '''

	classifier = KNeighborsClassifier(n_neighbors = k)
	classifier.fit(x, y)

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