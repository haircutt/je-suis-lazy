#!/usr/bin/env python3

# TODO
# def global_align(col, row):

  # Initialize scoring matrix and traceback matrix
col = input("Seq A: ")
row = input("Seq B: ")
n = len(col) + 1
m = len(row) + 1

print(40 * '-')
print("Scoring Scheme: ")
gap = int(input("Gap penalty: "))
penalty = int(input("Penalty: "))

# intial values for scoring matrix
score_matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(1, n):
    score_matrix[i][0] = score_matrix[i-1][0] + gap

for j in range(1, m):
    score_matrix[0][j] = score_matrix[0][j-1] + gap

for row in score_matrix:
    print(row)
    print(40 * '-')

# fill in scoring matrix
for i in range(1, n):
    for j in range(1, m):
        if col[i-1] == row[j-1]:
            diag = score_matrix[i-1][j-1]
        else:
            diag = score_matrix[i-1][j-1] + penalty
        up = score_matrix[i-1][j] + gap
        left = score_matrix[i][j-1] + gap
        score_matrix[i][j] = max(diag, up, left)
for row in score_matrix:
    print(row)
   