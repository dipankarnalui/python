#print 10 lines before the string_to_search
'''
import commands

filename = "dcmscript.log"
string_to_search = "Telemetry Event is notifyFlushLogs"

extract  = (commands.getstatusoutput("grep -C 10 '%s' %s"%(string_to_search,filename)))[1]

print(extract)
'''

import collections
import itertools
import sys

with open('dcmscript.log') as f:
    before = collections.deque(maxlen=10)
    for line in f:
        if 'Telemetry Event is notifyFlushLogs' in line:
            sys.stdout.writelines(before)
            sys.stdout.write(line)
            sys.stdout.writelines(itertools.islice(f, 10))
            break
        before.append(line)