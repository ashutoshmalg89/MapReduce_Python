#!/usr/bin/env python

import sys

sum_time = 0.0
current_website = None
current_day= None
website = None
final_sum=0.0
count = 1
combo = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    in_website, in_date, in_time = line.split('\t', 2)
    in_time=float(in_time)
    combo = str(str(in_website) + ':' + str(in_date))
    if current_website == combo:
        sum_time += in_time
        count += 1
    else:
        sum_time = sum_time/count
        if current_website:
            print('%s\t%s\t%s' % (current_website.split(':')[0], current_website.split(':')[1], sum_time))
        sum_time = in_time
        current_website = combo
	count = 1



