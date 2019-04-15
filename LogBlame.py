#!/usr/bin/python -u

import sys
import re
import os

piddic = {}
timedic = {}

def statistic(time, pid, tag):
	if timedic.has_key(time) == False:
		timedic[time] = 1
	else:
		timedic[time] += 1

	if piddic.has_key(pid) == False:
		tagdic = {}
		piddic[pid] = tagdic
	else:
		tagdic = piddic[pid]

	if tagdic.has_key(tag) == False:
		tagdic[tag] = 1
	else:
		tagdic[tag] += 1

def output():
	countdic = {}
	total = 0;

	for key in piddic:
		tagdic = piddic[key]
		for key1 in tagdic:
			if countdic.has_key(key1) == False:
				countdic[key1] = 0
			countdic[key1] += tagdic[key1]

	for key in countdic:
		total += countdic[key]

	print ''
	print '-----------total line of logs: ', total, '----------------'

	for key, val in sorted(countdic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True):
		percent = float(val)/float(total)
		if percent < 0.01:
			break
		print key, val, 'percent: {:.2%}'.format(percent)

	total = 0
	for key in timedic:
		total += timedic[key]

	print ''
	print '----------- avg ', total/len(timedic), ' lines per second ------------'
	i = 0
	for key, val in sorted(timedic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True):
		percent = float(val)/float(total)
		print key, val, 'percent: {:.2%}'.format(percent)
		i += 1
		if i >= 10:
			break


def statistic_file(path):
	print 'calculating ' + path
	f = open(path)
	for line in f:
		chunk = re.sub(' +', ' ', line).split(' ')
		if len(chunk) < 6:
			continue
		#print line
		statistic(chunk[1].split('.')[0], chunk[2], chunk[5])
	f.close()

def statistic_dir(path):
	for f in os.listdir(path): 
		if os.path.isdir(path + '/' + f):
			statistic_dir(path + '/' + f)
		else:
			statistic_file(path + '/' + f)


if len(sys.argv) != 2:
	print "arguments error"
	exit()

path = sys.argv[1]

if os.path.exists(path) == False:
	print "file or dir does not exists"
	exit()

if os.path.isdir(path):
    statistic_dir(path)
elif os.path.isfile(path):
	statistic_file(path)
    

output()


