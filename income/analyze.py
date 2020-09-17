# This is a program to aid in the analysis and presentation of the assignment
# Zach Sirera - Fall 2020

# import from root folder
import data

# Import the necessary external libraries
import matplotlib.pyplot as plt

def decision_tree_curve():
	''' this is a function to plot the success rate of the decision tree as the max depth is adjusted'''

	results = [{'depth': 1, 'success rate': 0.798}, {'depth': 2, 'success rate': 0.799}, {'depth': 3, 'success rate': 0.797}, 
	{'depth': 4, 'success rate': 0.798}, {'depth': 5, 'success rate': 0.799}, {'depth': 6, 'success rate': 0.799}, 
	{'depth': 7, 'success rate': 0.8}, {'depth': 8, 'success rate': 0.799}, {'depth': 9, 'success rate': 0.797}, 
	{'depth': 10, 'success rate': 0.8}, {'depth': 11, 'success rate': 0.8}, {'depth': 12, 'success rate': 0.798}, 
	{'depth': 13, 'success rate': 0.799}, {'depth': 14, 'success rate': 0.8}, {'depth': 15, 'success rate': 0.799}, 
	{'depth': 16, 'success rate': 0.799}, {'depth': 17, 'success rate': 0.798}, {'depth': 18, 'success rate': 0.8}, 
	{'depth': 19, 'success rate': 0.802}, {'depth': 20, 'success rate': 0.798}, {'depth': 21, 'success rate': 0.799}, 
	{'depth': 22, 'success rate': 0.798}, {'depth': 23, 'success rate': 0.798}, {'depth': 24, 'success rate': 0.799}, 
	{'depth': 25, 'success rate': 0.8}, {'depth': 26, 'success rate': 0.801}, {'depth': 27, 'success rate': 0.801}, 
	{'depth': 28, 'success rate': 0.796}, {'depth': 29, 'success rate': 0.796}, {'depth': 30, 'success rate': 0.799}, 
	{'depth': 31, 'success rate': 0.799}, {'depth': 32, 'success rate': 0.798}, {'depth': 33, 'success rate': 0.799}, 
	{'depth': 34, 'success rate': 0.799}, {'depth': 35, 'success rate': 0.799}, {'depth': 36, 'success rate': 0.798}, 
	{'depth': 37, 'success rate': 0.797}, {'depth': 38, 'success rate': 0.798}, {'depth': 39, 'success rate': 0.798}]

	x = []
	y = []

	for each in results:
		x.append(each['depth'])
		y.append(each['success rate'])

	plt.scatter(x, y)
	plt.title("Decision Tree Performance")
	plt.xlabel("Max Tree Depth")
	plt.ylabel("Test Data Success Rate")
	plt.show()

def knn_curve():
	results = [{'k': 10, 'success rate': 0.77}, {'k': 20, 'success rate': 0.782}, {'k': 30, 'success rate': 0.779}, {'k': 40, 'success rate': 0.774}, {'k': 50, 'success rate': 0.771}, {'k': 60, 'success rate': 0.768}, {'k': 70, 'success rate': 0.766}, {'k': 80, 'success rate': 0.764}, {'k': 90, 'success rate': 0.762}, {'k': 100, 'success rate': 0.761}, {'k': 110, 'success rate': 0.76}, {'k': 120, 'success rate': 0.759}, {'k': 130, 'success rate': 0.758}, {'k': 140, 'success rate': 0.757}, {'k': 150, 'success rate': 0.757}, {'k': 160, 'success rate': 0.756}, {'k': 170, 'success rate': 0.756}, {'k': 180, 'success rate': 0.756}, {'k': 190, 'success rate': 0.756}, {'k': 200, 'success rate': 0.756}, {'k': 210, 'success rate': 0.756}, {'k': 220, 'success rate': 0.756}, {'k': 230, 'success rate': 0.755}, {'k': 240, 'success rate': 0.755}, {'k': 250, 'success rate': 0.755}, {'k': 260, 'success rate': 0.755}, {'k': 270, 'success rate': 0.755}, {'k': 280, 'success rate': 0.755}, {'k': 290, 'success rate': 0.755}, {'k': 300, 'success rate': 0.754}, {'k': 310, 'success rate': 0.754}, {'k': 320, 'success rate': 0.754}, {'k': 330, 'success rate': 0.754}, {'k': 340, 'success rate': 0.754}, {'k': 350, 'success rate': 0.753}, {'k': 360, 'success rate': 0.753}, {'k': 370, 'success rate': 0.753}, {'k': 380, 'success rate': 0.753}, {'k': 390, 'success rate': 0.753}, {'k': 400, 'success rate': 0.753}, {'k': 410, 'success rate': 0.753}, {'k': 420, 'success rate': 0.752}, {'k': 430, 'success rate': 0.752}, {'k': 440, 'success rate': 0.752}, {'k': 450, 'success rate': 0.752}, {'k': 460, 'success rate': 0.752}, {'k': 470, 'success rate': 0.752}, {'k': 480, 'success rate': 0.752}, {'k': 490, 'success rate': 0.752}, {'k': 500, 'success rate': 0.752}, {'k': 510, 'success rate': 0.752}, {'k': 520, 'success rate': 0.752}, {'k': 530, 'success rate': 0.752}, {'k': 540, 'success rate': 0.752}, {'k': 550, 'success rate': 0.752}, {'k': 560, 'success rate': 0.752}, {'k': 570, 'success rate': 0.752}, {'k': 580, 'success rate': 0.752}, {'k': 590, 'success rate': 0.752}, {'k': 600, 'success rate': 0.752}, {'k': 610, 'success rate': 0.752}, {'k': 620, 'success rate': 0.752}, {'k': 630, 'success rate': 0.752}, {'k': 640, 'success rate': 0.752}, {'k': 650, 'success rate': 0.752}, {'k': 660, 'success rate': 0.752}, {'k': 670, 'success rate': 0.752}, {'k': 680, 'success rate': 0.752}, {'k': 690, 'success rate': 0.752}, {'k': 700, 'success rate': 0.752}, {'k': 710, 'success rate': 0.752}, {'k': 720, 'success rate': 0.752}, {'k': 730, 'success rate': 0.752}, {'k': 740, 'success rate': 0.752}, {'k': 750, 'success rate': 0.752}, {'k': 760, 'success rate': 0.752}, {'k': 770, 'success rate': 0.752}, {'k': 780, 'success rate': 0.752}, {'k': 790, 'success rate': 0.752}, {'k': 800, 'success rate': 0.752}, {'k': 810, 'success rate': 0.752}, {'k': 820, 'success rate': 0.752}, {'k': 830, 'success rate': 0.752}, {'k': 840, 'success rate': 0.752}, {'k': 850, 'success rate': 0.752}, {'k': 860, 'success rate': 0.752}, {'k': 870, 'success rate': 0.752}, {'k': 880, 'success rate': 0.752}, {'k': 890, 'success rate': 0.752}, {'k': 900, 'success rate': 0.752}, {'k': 910, 'success rate': 0.752}, {'k': 920, 'success rate': 0.752}, {'k': 930, 'success rate': 0.752}, {'k': 940, 'success rate': 0.752}, {'k': 950, 'success rate': 0.752}, {'k': 960, 'success rate': 0.752}, {'k': 970, 'success rate': 0.752}, {'k': 980, 'success rate': 0.752}, {'k': 990, 'success rate': 0.752}]

	x = []
	y = []

	for each in results:
		x.append(each['k'])
		y.append(each['success rate'])

	plt.scatter(x, y)
	plt.title("k-NN Performance")
	plt.xlabel("k")
	plt.ylabel("Test Data Success Rate")
	plt.show()

def quality_histogram():
	all_data = data.get_all_data('winequality-white.csv')
	y = []

	for each in all_data:
		y.append(int(each['quality']))

	print("3 ", round(y.count(3)/4898, 3))
	print("4 ", round(y.count(4)/4898, 3))
	print("5 ", round(y.count(5)/4898, 3))
	print("6 ", round(y.count(6)/4898, 3))
	print("7 ", round(y.count(7)/4898, 3))
	print("8 ", round(y.count(8)/4898, 3))
	print("9 ", round(y.count(9)/4898, 3))

	plt.hist(y, 7)
	plt.title("Quality Score Distribution")
	plt.show()


if __name__ == '__main__':
	decision_tree_curve()
	# quality_histogram()
	# knn_curve()