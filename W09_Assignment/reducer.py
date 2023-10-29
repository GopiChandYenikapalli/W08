#!/usr/bin/env python


from operator import itemgetter
import sys

total_value = 0
count = 0

for line in sys.stdin:
    value, num = line.strip().split('\t')

    try:
        total_value += float(value)
        count += int(num)
    except ValueError:
        continue

if count != 0:
    average = total_value / count
    print('AVERAGE = %.2f' % average)