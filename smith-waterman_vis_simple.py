#!/usr/bin/env python3

#hopefully visualise the smith-waterman local alignment --> 2D matrix

import sys

#TODO: set score for match, mismatch, gap penalties open + extended
#TODO: take in 2 sequences --> ONLY ACTG bc its DNA

match = int(input("Match score: "))
mismatch = int(input("Mismatch score: "))
open_pen = int(input("Open penalty: "))
extended_pen = int(input("Extend penalty: "))