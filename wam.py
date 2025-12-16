#!/usr/bin/env python3

# UNSW WAM --> sum of (grade * no. units) / total units

#Format: 

import sys
import math


total_units = 0
linecount = 0 # not needed, but im releasing all my anger at the world into my code
total_grade = 0 

for line in sys.stdin:
    total_units += int(line.split()[1])
    total_grade += float(line.split()[0]) * float(line.split()[1])
    linecount += 1
if linecount == 0:
    print("Nothing inputted. Don't waste my time.")
    sys.exit(0)
if linecount == 1:
    print("You are stupid and your wam is the only grade you've received thus far")
    sys.exit(0)
# TODO: error checking + testing files

print(f" You current WAM is {total_grade} divide by {total_units}")

print(format(total_grade / total_units, '.3f'))
