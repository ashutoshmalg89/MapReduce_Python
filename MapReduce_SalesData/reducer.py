#!/usr/bin/env python

import sys

sum_sales = 0
current_combo = None
combo = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    department, year, sales = line.split('\t', 2)
    sales=float(sales)
    combo = str(str(department) +':'+ str(year))
    if current_combo == combo:
        sum_sales += sales
    else:
        if current_combo:
            if sum_sales>25000000:
                print('%s\t%s\t%s' % (current_combo.split(':')[0],current_combo.split(':')[1], sum_sales))
        sum_sales = sales
        current_combo = combo

