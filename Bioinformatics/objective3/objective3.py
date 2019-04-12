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


def WPGMA(file_name):
	matrix = np.genfromtxt(file_name, dtype=None, encoding="utf-8")  # this is an ndarray
	minimum = matrix[1][2]  # set the minimum as the first non-null value in the matrix
	print(matrix)

	start_index = 2

	for row in range(1, len(matrix)):
		for column in range(start_index, len(matrix)):  # this is so you check all values after the 0 diagonal
			if matrix[row][column] < minimum:
				minimum = matrix[row][column]
		start_index += 1

	print(minimum)

	return


WPGMA("matrix1.txt")
