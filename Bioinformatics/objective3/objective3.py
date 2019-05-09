import time
import numpy as np
import matplotlib as plt
import networkx as nx

# ignore first row
# ignore first item in every row afterwards
# in fact, i can start my iteration from the first item after the 0
# and that means i can ignore the last row
# ^^ in order to find my min value and do the stuff from there
# it would be good for me to keep track of the row and column i am in so as to remember which species i'm looking at
# row index --> species on top
# column index --> species along side
# and then just concatenate the headings (and obviously do all the appropriate calculations)

# calculation: (distance(a, c) + distance(b, c))/2
# could store all values in an array and add to matrix afterwards


def find_minimum(matrix):
	minimum = matrix[1][2]  # set the minimum as the first non-null value in the matrix
	start_index = 2

	for row in range(1, len(matrix)):
		for column in range(start_index, len(matrix)):  # this is so you check all values after the 0 diagonal
			if matrix[row][column] < minimum:
				minimum = matrix[row][column]
		start_index += 1

	return minimum


def WPGMA(file_name):
	matrix = np.genfromtxt(file_name, dtype=None, encoding="utf-8")  # this is an ndarray
	print(matrix)

	while len(matrix) > 3:
		# find the minimum val in the matrix
		# reduce the matrix by squishing the row and column together and recalculating distances
		# print out the reduced matrix

		# use np.delete for deleting rows and columns. good stuff

		minimum = find_minimum(matrix)
		position = np.where(matrix == minimum)  # finds the position(s) of the min value in the matrix

		# position[0] --> first (x,y) coords --> x = position[0][0], y = position[0][1]
		header = matrix[0][position[0][0]] + matrix[0][position[0][1]]

		array = []
		for i in range(len(matrix)-1):
			if matrix[position[0][0]][i+1] == '0':
				continue
			elif i+1 == position[0][1]:
				continue
			else:
				distance = (float(matrix[position[0][0]][i+1]) + float(matrix[position[0][1]][i+1]))/2
				array.append(str(distance))
		array.insert(0, header)

		# deletes the rows and columns of the selected species
		# max and min so that the correct rows/cols are deleted as the matrix indices will change
		# 0 denotes a row being deleted, 1 denotes a column being deleted
		matrix = np.delete(matrix, max(position[0]), 0)
		matrix = np.delete(matrix, max(position[0]), 1)
		matrix = np.delete(matrix, min(position[0]), 0)
		matrix = np.delete(matrix, min(position[0]), 1)

		# adds new row and column of zeroes to end of matrix
		matrix = np.append(matrix, [array], axis=0)
		array.append('0')
		array = np.transpose([array])
		matrix = np.append(matrix, array, axis=1)

		# labels the new species
		matrix[len(matrix)-1][0] = header
		matrix[0][len(matrix)-1] = header

		print(matrix)

	return


WPGMA("matrix1.txt")
