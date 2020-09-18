# This is the main driver for the Supervised Learning assignment in Georgia Tech CS 7641 
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


def train(train_x, train_y):
	''' this is a function to train all classifiers '''
	tree_clf = tree.train(train_x, train_y)
	svm_clf = svm.train(train_x, train_y)
	knn_clf = knn.train(train_x, train_y)
	nn_clf = nn.train(train_x, train_y)
	boost_clf = boost.train(train_x, train_y)

	return [tree_clf, svm_clf, knn_clf, nn_clf, boost_clf]

def tune(test_x, test_y, train_x, train_y):
	''' '''

	# tree_results = tree.tune(train_x, train_y, test_x, test_y, depth=40)
	knn_results = knn.tune(train_x, train_y, test_x, test_y, neighbors=30)
	print(knn_results)



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

	train_x, train_y, test_x, test_y  = data.main('adult_data.csv')
	
	classifiers = train(train_x, train_y)
	results = test(classifiers, test_x, test_y)
	print(results)

	#print(nn.tune(train_x, train_y, test_x, test_y, 1, 4))

	# tune(train_x, train_y, test_x, test_y)









		