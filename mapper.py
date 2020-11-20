#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()    # remove leading and trailing whitespace
    words = line.split()   # split the line into words
    for word in words:
        print( '%s\t%s' % (word, 1))