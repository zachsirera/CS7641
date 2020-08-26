# This is a program to aid in the analysis and presentation of the assignment
# Zach Sirera - Fall 2020

# import from root folder
import data

# Import the necessary external libraries
import matplotlib.pyplot as plt

def decision_tree_curve():
	''' this is a function to plot the success rate of the decision tree as the max depth is adjusted'''

	results = [{'depth': 1, 'success rate': 0.528}, {'depth': 2, 'success rate': 0.589}, {'depth': 3, 'success rate': 0.573}, 
	{'depth': 4, 'success rate': 0.541}, {'depth': 5, 'success rate': 0.572}, {'depth': 6, 'success rate': 0.531}, 
	{'depth': 7, 'success rate': 0.532}, {'depth': 8, 'success rate': 0.525}, {'depth': 9, 'success rate': 0.489}, 
	{'depth': 10, 'success rate': 0.444}, {'depth': 11, 'success rate': 0.46}, {'depth': 12, 'success rate': 0.446}, 
	{'depth': 13, 'success rate': 0.423}, {'depth': 14, 'success rate': 0.409}, {'depth': 15, 'success rate': 0.408}, 
	{'depth': 16, 'success rate': 0.404}, {'depth': 17, 'success rate': 0.384}, {'depth': 18, 'success rate': 0.396}, 
	{'depth': 19, 'success rate': 0.387}, {'depth': 20, 'success rate': 0.393}, {'depth': 21, 'success rate': 0.394}, 
	{'depth': 22, 'success rate': 0.411}, {'depth': 23, 'success rate': 0.398}, {'depth': 24, 'success rate': 0.41}, 
	{'depth': 25, 'success rate': 0.412}, {'depth': 26, 'success rate': 0.4}, {'depth': 27, 'success rate': 0.419}, 
	{'depth': 28, 'success rate': 0.392}, {'depth': 29, 'success rate': 0.41}, {'depth': 30, 'success rate': 0.397}, 
	{'depth': 31, 'success rate': 0.407}, {'depth': 32, 'success rate': 0.408}, {'depth': 33, 'success rate': 0.393}, 
	{'depth': 34, 'success rate': 0.401}, {'depth': 35, 'success rate': 0.408}, {'depth': 36, 'success rate': 0.42}, 
	{'depth': 37, 'success rate': 0.407}, {'depth': 38, 'success rate': 0.413}, {'depth': 39, 'success rate': 0.411}, 
	{'depth': 40, 'success rate': 0.407}]

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
	results = [{'k': 10, 'success rate': 0.457}, {'k': 20, 'success rate': 0.476}, {'k': 30, 'success rate': 0.494}, 
	{'k': 40, 'success rate': 0.476}, {'k': 50, 'success rate': 0.514}, {'k': 60, 'success rate': 0.498}, {'k': 70, 'success rate': 0.512}, 
	{'k': 80, 'success rate': 0.509}, {'k': 90, 'success rate': 0.502}, {'k': 100, 'success rate': 0.507}, {'k': 110, 'success rate': 0.523}, 
	{'k': 120, 'success rate': 0.512}, {'k': 130, 'success rate': 0.511}, {'k': 140, 'success rate': 0.51}, {'k': 150, 'success rate': 0.509}, 
	{'k': 160, 'success rate': 0.512}, {'k': 170, 'success rate': 0.517}, {'k': 180, 'success rate': 0.507}, {'k': 190, 'success rate': 0.505}, 
	{'k': 200, 'success rate': 0.516}, {'k': 210, 'success rate': 0.523}, {'k': 220, 'success rate': 0.521}, {'k': 230, 'success rate': 0.523}, 
	{'k': 240, 'success rate': 0.529}, {'k': 250, 'success rate': 0.528}, {'k': 260, 'success rate': 0.53}, {'k': 270, 'success rate': 0.537}, 
	{'k': 280, 'success rate': 0.535}, {'k': 290, 'success rate': 0.541}, {'k': 300, 'success rate': 0.532}, {'k': 310, 'success rate': 0.532}, 
	{'k': 320, 'success rate': 0.53}, {'k': 330, 'success rate': 0.535}, {'k': 340, 'success rate': 0.535}, {'k': 350, 'success rate': 0.539}, 
	{'k': 360, 'success rate': 0.541}, {'k': 370, 'success rate': 0.541}, {'k': 380, 'success rate': 0.546}, {'k': 390, 'success rate': 0.546}, 
	{'k': 400, 'success rate': 0.547}, {'k': 410, 'success rate': 0.546}, {'k': 420, 'success rate': 0.544}, {'k': 430, 'success rate': 0.543}, 
	{'k': 440, 'success rate': 0.539}, {'k': 450, 'success rate': 0.54}, {'k': 460, 'success rate': 0.539}, {'k': 470, 'success rate': 0.538}, 
	{'k': 480, 'success rate': 0.539}, {'k': 490, 'success rate': 0.541}, {'k': 500, 'success rate': 0.534}, {'k': 510, 'success rate': 0.537}, 
	{'k': 520, 'success rate': 0.538}, {'k': 530, 'success rate': 0.541}, {'k': 540, 'success rate': 0.541}, {'k': 550, 'success rate': 0.538}, 
	{'k': 560, 'success rate': 0.533}, {'k': 570, 'success rate': 0.531}, {'k': 580, 'success rate': 0.532}, {'k': 590, 'success rate': 0.539}, 
	{'k': 600, 'success rate': 0.537}, {'k': 610, 'success rate': 0.529}, {'k': 620, 'success rate': 0.539}, {'k': 630, 'success rate': 0.542}, 
	{'k': 640, 'success rate': 0.532}, {'k': 650, 'success rate': 0.542}, {'k': 660, 'success rate': 0.536}, {'k': 670, 'success rate': 0.529}, 
	{'k': 680, 'success rate': 0.53}, {'k': 690, 'success rate': 0.526}, {'k': 700, 'success rate': 0.528}, {'k': 710, 'success rate': 0.53}, 
	{'k': 720, 'success rate': 0.53}, {'k': 730, 'success rate': 0.531}, {'k': 740, 'success rate': 0.532}, {'k': 750, 'success rate': 0.527}, 
	{'k': 760, 'success rate': 0.528}, {'k': 770, 'success rate': 0.531}, {'k': 780, 'success rate': 0.528}, {'k': 790, 'success rate': 0.527}, 
	{'k': 800, 'success rate': 0.53}, {'k': 810, 'success rate': 0.532}, {'k': 820, 'success rate': 0.528}, {'k': 830, 'success rate': 0.529}, 
	{'k': 840, 'success rate': 0.529}, {'k': 850, 'success rate': 0.529}, {'k': 860, 'success rate': 0.529}, {'k': 870, 'success rate': 0.531}, 
	{'k': 880, 'success rate': 0.532}, {'k': 890, 'success rate': 0.53}, {'k': 900, 'success rate': 0.531}, {'k': 910, 'success rate': 0.53}, 
	{'k': 920, 'success rate': 0.531}, {'k': 930, 'success rate': 0.527}, {'k': 940, 'success rate': 0.53}, {'k': 950, 'success rate': 0.529}, 
	{'k': 960, 'success rate': 0.53}, {'k': 970, 'success rate': 0.529}, {'k': 980, 'success rate': 0.528}, {'k': 990, 'success rate': 0.528}]

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
	# decision_tree_curve()
	# quality_histogram()
	# knn_curve()