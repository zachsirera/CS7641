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


def train(folds_x, folds_y):
	''' this is a function to train all classifiers '''
	tree_clf = tree.train(folds_x, folds_y)
	svm_clf = svm.train(folds_x, folds_y)
	knn_clf = knn.train(folds_x, folds_y)
	nn_clf = nn.train(folds_x, folds_y)
	boost_clf = boost.train(folds_x, folds_y)

	return [tree_clf, svm_clf, knn_clf, nn_clf, boost_clf] # 



def test(classifiers, test_x, test_y):
	''' this is a function to test the classifiers against the testing data set '''

	results = []

	for classifier in classifiers:
		correct = 0
		total = 0

		for index, each in enumerate(test_x):
			total += 1
			result = classifier.predict([each])
			if result == test_y[index]:
				correct += 1

		results.append(round(correct / total, 3))

	return results



if __name__ == '__main__':

	train_x, train_y, test_x, test_y  = data.main('winequality-white.csv')
	folds_x = data.generate_folds(4, train_x)
	folds_y = data.generate_folds(4, train_y)
	classifiers = train(folds_x, folds_y)
	results = test(classifiers, test_x, test_y)
	print(results)











		