# This is the main driver for the Supervised Learning assingment in Georgia Tech CS 7641 
# Zach Sirera - Fall 2020


# import the various learners from the root folder
import boost
import knn
import nn
import svm
import tree

# import the csv reader
import data

# import the necessary external libraries
import time

def train(train_x, train_y):
	''' this is a function to train all classifiers '''
	tree_start = time.time()
	tree_clf = tree.train(train_x, train_y)
	print('Decision Tree - Training Time: ', round(time.time() - tree_start, 3), 's')

	svm_start = time.time()
	svm_clf = svm.train(train_x, train_y)
	print('SVM - Training Time: ', round(time.time() - svm_start, 3), 's')

	knn_start = time.time()
	knn_clf = knn.train(train_x, train_y)
	print('k-NN - Training Time: ', round(time.time() - knn_start, 3), 's')

	nn_start = time.time()
	nn_clf = nn.train(train_x, train_y)
	print('Neural Network - Training Time: ', round(time.time() - nn_start, 3), 's')

	boost_start = time.time()
	boost_clf = boost.train(train_x, train_y)
	print('Boosted Tree - Training Time: ', round(time.time() - boost_start, 3), 's')

	return [tree_clf, svm_clf, knn_clf, nn_clf, boost_clf]

	# 



def test(classifiers, test_x, test_y):
	''' this is a function to test the classifiers against the testing data set '''

	results = []
	
	models = ['Decision Tree', 'SVM', 'k-NN', 'Neural Network', 'Boosted Tree']

	for jindex, classifier in enumerate(classifiers):
		correct = 0
		total = 0
		elapsed_time = 0

		for index, each in enumerate(test_x):
			total += 1
			start_time = time.time()
			result = classifier.predict([each])
			elapsed_time += (time.time() - start_time)
			if result == test_y[index]:
				correct += 1

		results.append(round(correct / total, 3))

		print(models[jindex], ' - Mean Access Time: ', round(elapsed_time / len(test_x), 5), 's')

	return results


def learning_curve(train_x, train_y, test_x, test_y):

	counts = []
	curve = []
	models = ['tree', 'svm', 'knn', 'nn', 'boost']

	for i in range(1000, len(train_x), 200):
		counts.append(i)


	for each in counts:
		short_train_x = train_x[:each]
		short_train_y = train_y[:each]
		classifiers = train(short_train_x, short_train_y)
		results = test(classifiers, test_x, test_y)

		data = dict()
		data['size'] = each 

		for index, result in enumerate(results):
			data[models[index]] = result

		curve.append(data)

	return curve





if __name__ == '__main__':

	train_x, train_y, test_x, test_y  = data.main('winequality-white.csv')
	classifiers = train(train_x, train_y)
	results = test(classifiers, test_x, test_y)
	# print(results)

	#print(nn.tune(train_x, train_y, test_x, test_y, 1, 4))

	# print(learning_curve(train_x, train_y, test_x, test_y))










		