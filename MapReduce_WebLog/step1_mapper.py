#!/usr/bin/env python

import sys

from datetime import datetime

def time_in_secs(timedelta):
    return (timedelta.microseconds + 0.0 + ( timedelta.seconds + timedelta.days * 24 * 3600) * 10 ** 6) / 10 ** 6

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    website, starttime, endtime = line.split('\t')

    day = datetime.strptime(starttime, "%Y-%m-%d %H:%M:%S").date()
    starttime=datetime.strptime(starttime,"%Y-%m-%d %H:%M:%S")
    endtime=datetime.strptime(endtime,"%Y-%m-%d %H:%M:%S")

    time_spent= endtime - starttime

    print('%s\t%s\t%s' % (website, day, time_in_secs(time_spent)))

