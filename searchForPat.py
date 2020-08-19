#!/usr/bin/python

import collections
import sys

def searchForPattern(long_string, pattern):
	if pattern == "":
		return "|".join(['0' for x in long_string] + ['0'])
	
	mydict = {} # initialize hash set
	
	for word in long_string:
		mydict[word] = 0 # initialize number of occurrences to 0
		i = 0
		while i < len(word) - len(pattern)+1: # loops through word using a sliding window
			if word[i: i+len(pattern)] == pattern:
				mydict[word] += 1
			i += 1
			
	res = [x for x in mydict.values()] 
	res += [sum(res)] # append sum of all occurrences to result
	return "|".join([str(x) for x in res]) # join result into correct format


for line in sys.stdin:
	splitted_input = line.split(';')
	pattern = splitted_input[0]
	long_string = splitted_input[1].split('|')
 
	print(searchForPattern(long_string, pattern))
	