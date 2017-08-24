#!/usr/bin/env python

import sys

sum_spike = 0
current_website = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    website, spike = line.split('\t', 2)
    spike = int(spike)
    if current_website == website:
        sum_spike += spike
    else:
        if current_website:
            print('%s\t%s' % (current_website, sum_spike))
        current_website = website
        sum_spike = spike
if current_website == website:
    print('%s\t%s' % (current_website, sum_spike))

