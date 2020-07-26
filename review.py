#!/usr/bin/env python3

import sys

# read the data file and put it into several data structures

def read_as_string(filename):
	strings = []
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip()
			strings.append(line)
	return strings

def read_as_tuple(filename):
	tups = []
	with open(filename) as fp:
		for line in fp.readlines():
			(name, age) = line.split(',')
			tups.append((name,float(age)))
	return tups

def read_as_list(filename):
	stuff = []
	with open(filename) as fp:
		for line in fp.readlines():
			f = line.split(',')
			f[1] = int(f[1])
			stuff.append(f)
	return stuff

def read_as_dict(filename):
	table = {}
	with open(filename) as fp:
		for line in fp.readlines():
			(name, age) = line.split(',')
			table[name] = int(age)
	return table
			

# better to use argparse but this is an alternative way to get the file
if len(sys.argv) != 2:
	print(f'{sys.argv[0]} must include filename')
	sys.exit()
file = sys.argv[1]

dstr = read_as_string(file)
dtup = read_as_tuple(file)
dlist = read_as_list(file)
ddict = read_as_dict(file)
print(dstr)
print(dtup)
print(dlist)
print(ddict)

for (name, age) in dtup:
	print(f'{name} is {age} years old')

for a in dlist:
	print(f'{a[0]} is {a[1]} years old')

for name in ddict:
	print(f'{name} is {ddict[name]} years old')

for s in dstr:
	(name, age) = s.split(',')
	print(f'{name} is {age} year old')
