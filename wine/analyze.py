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
	quality_histogram()