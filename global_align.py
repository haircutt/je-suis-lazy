#!/usr/bin/env python3

# TODO
def global_align(col, row):

  # Initialize scoring matrix and traceback matrix
  col = input("Seq A: ")
  row = input("Seq B: ")
  n = len(col) + 1
  m = len(row) + 1

  print(40 * '-')
  print("Scoring Scheme: ")
  gap = input("Gap penalty: ")
  penalty = input("Penalty: ")

  score_matrix = [[0 for j in range(m)] for i in range(n)]


   