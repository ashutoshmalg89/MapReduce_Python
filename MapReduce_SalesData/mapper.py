#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    store, department, year,sales=line.split('\t')


    print('%s\t%s\t%s' % (department,year[0:4],sales))

