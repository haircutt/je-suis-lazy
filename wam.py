#!/usr/bin/env python3

# UNSW WAM --> sum of (grade * no. units) / total units

#Format: 

import sys
import math

calc = {}

total_units = 0

total_grade = 0 

for line in sys.stdin:
    total_units += int(line.split()[1])
    total_grade += float(line.split()[0]) * float(line.split()[1])


print(f" You current WAM is {total_grade} divide by {total_units}")

print(format(total_grade / total_units, '.3f'))




