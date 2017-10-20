# coding=utf8
import time
i=0
start = time.time()
with open('/Users/huangkaijie/log/log20171010') as f:
    for line in f:
        if i<20:
            print line
        i += 1
print time.time() - start
print i