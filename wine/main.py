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


def run(training_data, testing_data):
	''' this is a function to run all analyses required '''
	# tree.main(training_data, testing_data)
	svm.main(training_data, testing_data)
	# knn.main(training_data, testing_data)
	# nn.main(training_data, testing_data)
	# boost.main(training_data, testing_data)


if __name__ == '__main__':
	training_data, testing_data = data.main('winequality-white.csv')
	run(training_data, testing_data)
		