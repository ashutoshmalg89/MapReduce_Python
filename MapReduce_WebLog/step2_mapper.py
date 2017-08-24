#!/usr/bin/env python

import Queue
import sys

from datetime import datetime, timedelta

count = 0
prev_date = None
curr_date = None
curr_website = None
next_website = None
next_day = None
data_queue=Queue.Queue()

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    in_website, in_date, avg_time = line.split('\t')
    conv_date = datetime.strptime(in_date, "%Y-%m-%d").date()
    if count == 0:
        curr_date = datetime.strptime(in_date, "%Y-%m-%d").date()
        curr_website = in_website
        count += 1
        data_queue.put(in_website + "|" + in_date + "|" + avg_time)

    else:
        next_day = curr_date + timedelta(days=1)
        if count == 1 or count == 2:
            if next_day == conv_date:
                curr_date = datetime.strptime(in_date, "%Y-%m-%d").date()
                data_queue.put(in_website + "|" + in_date + "|" + avg_time)
                count += 1
                if count == 3:
                    chksum = 0
                    var1 = 0
                    var2 = 0
                    var3 = 0
                    web1 = None
                    web2 = None
                    web3 = None
                    spike = 0
                    for i in data_queue.queue:
                        if chksum == 0:
                            var1 = float(i.split('|')[2])
                            web1 = i.split('|')[0]
                            chksum += 1
                        elif chksum == 1:
                            var2 = float(i.split('|')[2])
                            web2 = i.split('|')[0]
                            chksum += 1
                        elif chksum == 2:
                            var3 = float(i.split('|')[2])
                            web3 = i.split('|')[0]
                            chksum += 1
                    if web1 == web2 and web2 == web3:
                        if (2 * var1) <= var2 and (2 * var2) <= var3:
                            spike += 1
                            data_queue.get()
                            data_queue.all_tasks_done
                            count = 2
                            print('%s\t%s' % (web1, spike))
                        else:
                            count = 2
                            data_queue.get()
                            data_queue.all_tasks_done
                            # curr_date = datetime.strptime(in_date, "%Y-%m-%d").date()
                            # curr_website = in_website
                            # count += 1
                            # data_queue.put(in_website + "|" + in_date + "|" + avg_time)
                    else:
                        count = 0
                        data_queue.queue.clear()
                        data_queue.all_tasks_done
                        curr_date = datetime.strptime(in_date, "%Y-%m-%d").date()
                        curr_website = in_website
                        count += 1
                        data_queue.put(in_website + "|" + in_date + "|" + avg_time)
            else:
                count = 0
                data_queue.queue.clear()
                data_queue.all_tasks_done
                curr_date = datetime.strptime(in_date, "%Y-%m-%d").date()
                data_queue.put(in_website + "|" + in_date + "|" + avg_time)
                count += 1
