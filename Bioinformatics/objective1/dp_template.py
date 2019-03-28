#!/usr/bin/python
import time
import sys
import numpy as np
from enum import Enum


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

# ------------------------------------------------------------
# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it


def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

# -------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Initialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment
# and its score should be called best_score.

# +4 for a matching pair of ’A’ bases,
# +3 for a matching pair of ’C’ bases,
# +2 for a matching pair of ’G’ bases,
# +1 for a matching pair of ’T’ bases,
# -3 for a mismatching pair of bases,
# -2 for a gap.

# (rows, columns)
scoring_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=int)  # remember to include the gaps
backtrack_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=int)
base_scores = {"A": 4, "C": 3, "G": 2, "T": 1}


class Direction(Enum):
    DIAGONAL = 1
    UP = 2
    LEFT = 3


# these loops initialise the first row and column of the scoring + backtrack matrix when matching against gaps
# i.e. the whole pattern of -2, -4, -6, etc.
start_score = time.time()
for i in range(1, len(seq2) + 1):
    scoring_matrix[0, i] = scoring_matrix[0, i-1] - 2
    backtrack_matrix[0, i] = Direction.LEFT.value

for j in range(1, len(seq1) + 1):
    scoring_matrix[j, 0] = scoring_matrix[j-1, 0] - 2
    backtrack_matrix[j, 0] = Direction.UP.value

# direction = ("D", "U", "L")

# the actual process of filling in the scoring matrix
# going row by row
for row in range(1, len(seq1) + 1):
        for column in range(1, len(seq2) + 1):
            # need to compare bases
            # where i am in the matrix is where i need to look in the string to compare bases
            if seq1[row-1] != seq2[column-1]:
                diagonal = scoring_matrix[row-1, column-1] - 3
            else:
                diagonal = scoring_matrix[row-1, column-1] + base_scores[seq1[row-1]]
                # if seq1[row-1] == "A":
                #     diagonal = scoring_matrix[row-1, column-1] + 4
                # elif seq1[row-1] == "C":
                #     diagonal = scoring_matrix[row-1, column-1] + 3
                # elif seq1[row-1] == "G":
                #     diagonal = scoring_matrix[row-1, column-1] + 2
                # else:
                #     diagonal = scoring_matrix[row-1, column-1] + 1

            up = scoring_matrix[row - 1, column] - 2
            left = scoring_matrix[row, column-1] - 2
            scores = (diagonal, up, left)
            scoring_matrix[row, column] = max(scores)
            backtrack_matrix[row, column] = Direction(scores.index(max(scores)) + 1).value

stop_score = time.time()

# need to find the optimal alignment now
# start in bottom right of backtracking matrix and follow the directions
# diagonal - match/mismatch
# up - letter on the side (seq1) against a gap
# left - letter on the top (seq2) against a gap

row = len(seq1)
column = len(seq2)
alignment1 = []
alignment2 = []

start_backtrack = time.time()

while backtrack_matrix[row, column] != 0:
    if backtrack_matrix[row, column] == Direction.DIAGONAL.value:
        alignment1.insert(0, seq1[row-1])
        alignment2.insert(0, seq2[column-1])
        row -= 1
        column -= 1
    elif backtrack_matrix[row, column] == Direction.UP.value:
        alignment1.insert(0, seq1[row-1])
        alignment2.insert(0, "-")
        row -= 1
    else:
        alignment1.insert(0, "-")
        alignment2.insert(0, seq2[column-1])
        column -= 1

best_score = scoring_matrix[len(seq1), len(seq2)]

best_alignment = ("".join(alignment1), "".join(alignment2))

stop_backtrack = time.time()

# -------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start
time_taken_score = stop_score - start_score
time_taken_backtrack = stop_backtrack - start_backtrack

print("Time taken to score: "+str(time_taken_score))
print("Time taken to backtrack: "+str(time_taken_backtrack))

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
# displayAlignment(best_alignment)

# -------------------------------------------------------------
