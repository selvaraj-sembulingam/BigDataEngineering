#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove leading and trailing whitespace
	line = line.strip()
	# split the line into year and temp
	words = line.split(',')
	year = words[0].split('-')[2]
	temp = words[2]
	print '%s\t%s' % (year, temp)