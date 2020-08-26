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



def train(x, y):
	''' this is the function to train the knn classifier '''

	classifier = KNeighborsClassifier(n_neighbors = 400)
	classifier.fit(x, y)

	return classifier