# This is an implementation of a support vector machine 
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def main(train_x, train_y):

	svm = train(train_x, train_y)
	
	return svm



def train(x, y):
	''' This is a function to train the classifier '''

	classifier = make_pipeline(StandardScaler(), SVC(gamma='auto'))
	classifier.fit(x, y)

	return classifier



