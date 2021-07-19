#!/usr/bin/env python

import sys

current_year = None
current_max = 0
year = None

# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# spliting the data on the basis of tab we have provided in mapper.py
	year, temp = line.split('\t', 1)
	# convert temp (currently a string) to int
	try:
		temp = int(temp)
	except ValueError:
		# temp was not a number, so silently
		# ignore/discard this line
		continue
	
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: year) before it is passed to the reducer
	if current_year == year:
		current_max = max(current_max,temp)
	else:
		if current_year:
			# write result to STDOUT
			print '%s\t%s' % (current_year, current_max)
		current_year = year
		current_max = temp
		
# do not forget to output the last year if needed!
if current_year == year:
	print '%s\t%s' % (current_year, current_max)
