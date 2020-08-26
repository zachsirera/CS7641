# This is an implementation of a support vector machine 
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def main(training_data, testing_data):

	train_x, train_y = parse(training_data)
	test_x, test_y = parse(testing_data)

	svm = train(train_x, train_y)
	results = test(svm, test_x, test_y)
	print(results)



def predict(classifier, sample):
	''' this is a function to use the existing classifier to predict an outcome based on a sample'''
	return classifier.predict([sample])



def test(classifier, x, y):
	''' This is a function to determine how successful the classifier is at predicting quality '''

	correct = 0
	total = 0

	for index, each in enumerate(x):
		total += 1
		result = predict(classifier, each)
		if result == y[index]:
			correct += 1

	return round(correct / total, 3)


def train(x, y):
	''' This is a function to train the classifier '''

	classifier = make_pipeline(StandardScaler(), SVC(gamma='auto'))
	classifier.fit(x, y)

	return classifier



def parse(dataset):
	''' This is a function to parse the dataset dictionary and format it properly for the svm implementation '''

	x = []
	y = []

	for row in dataset:
		x.append([
			float(row["fixed acidity"]), 
			float(row["volatile acidity"]),
			float(row["citric acid"]),
			float(row["residual sugar"]),
			float(row["chlorides"]),
			float(row["free sulfur dioxide"]),
			float(row["total sulfur dioxide"]),
			float(row["density"]),
			float(row["pH"]),
			float(row["sulphates"]),
			float(row["alcohol"])
		])
		y.append(int(row["quality"]))

	return x, y