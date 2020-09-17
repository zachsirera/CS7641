# This is an implementation of a support vector machine 
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC





def train(folds_x, folds_y):
	''' This is a function to train the classifier '''

	folds = len(folds_x)
	classifiers = []
	fold_list = gen_fold_list(folds)

	for i in range(folds):

		training_x_folds = []
		training_y_folds = []

		for j in fold_list[i]: 	
			training_x_folds += folds_x[j]
			training_y_folds += folds_y[j]


		classifier = make_pipeline(StandardScaler(), SVC(gamma='auto'))
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
