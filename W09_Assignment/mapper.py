#!/usr/bin/env python

import sys

for line in sys.stdin: # look through data that is piped into this program
    values = line.strip().split() #split the line into values
    # For each value, its it's numeric , emit the value and count of 1
    for value in values:
        try:
            float(value)
            #print(f"{value}\t1")
            print('%.2f\t%s' %(float(value),1)) #output
        except ValueError:
            # Skip non-numeric values
            continue

