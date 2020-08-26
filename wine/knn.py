# This is an implementation of a k-nearest neighbors
# Zach Sirera - Fall 2020

# import files from the root directory
import data

# import the necessary external libraries
from sklearn.neighbors import KNeighborsClassifier


def main(training_data, testing_data):
	''' This is the function carry out the knn classifier '''

	train_x, train_y = data.parse(training_data)
	test_x, test_y = data.parse(testing_data)

	knn = train(train_x, train_y, 50)
	results = test(knn, test_x, test_y)
	print(results)


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



def predict(classifier, sample):
	''' this is a function to use the existing classifier to predict an outcome based on a sample'''
	return classifier.predict([sample])



def train(x, y, k):
	''' this is the function to train the knn classifier '''

	classifier = KNeighborsClassifier(n_neighbors = k)
	classifier.fit(x, y)

	return classifier



def test(classifier, x, y):
	''' this is the function to test the knn classifier '''

	correct = 0
	total = 0

	for index, each in enumerate(x):
		total += 1
		result = predict(classifier, each)
		if result == y[index]:
			correct += 1

	return round(correct / total, 3)