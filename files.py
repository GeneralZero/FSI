#!/usr/bin/env python
import subprocess as sub
import re
import sys
import os
import shutil
from stree import *

folder_ratio = 40
file_ratio = 70

def get_max_fuzz_ratio(input_location, output_locations):
	"""
	Match files with possoble directory
	"""
	maximize = [0]
	text_string = re.sub('\[(.*?)\]|\(.*?\)|720|1080|720p|1080p|HDTV|x264|-|_|', '', input_location[:-3])
	text_string = re.sub('\.', ' ', text_string.strip())
	#print text_string
	for output_location in output_locations:
		for (path, dirs, files) in os.walk(output_location):
			for direct in dirs :
				direct_string = re.sub('\[(.*?)\]|\(.*?\)', '', direct)
				direct_string = re.sub('_|\.', ' ', direct_string)
				matches = string_match(text_string, direct_string)
				if matches > folder_ratio and maximize[0] < matches: # partial_ratio
					#print "Partial Ratio\t\t\t\t", string_match(text_string, direct_string), text_string, direct_string
					#print
					maximize = [matches, os.path.join(path, direct)]
	if maximize != [0]:
		return maximize
	return [None, None]

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print "Usage: %s (search location) [destination locations]" % sys.argv[0]
		exit(-1)
	loc = [(lambda default, input: default if not os.path.isabs(sys.argv[1]) else input)(re.sub(r'~', os.environ['HOME'], s), os.path.abspath(re.sub(r'~', os.environ['HOME'], s))) for s in sys.argv[2:]]
	src_path = (lambda default, input: default if not os.path.isabs(sys.argv[1]) else input)(re.sub(r'~', os.environ['HOME'], sys.argv[1]), os.path.abspath(re.sub(r'~', os.environ['HOME'], sys.argv[1])))
	#Changes input to absolute directories and deals with ~ to home directory
	print src_path, os.path.exists(src_path)
	for s in loc:
		print s, os.path.exists(s)

	
'''
	for files in os.listdir(os.path.abspath(sys.argv[1])):
		rating, dest = get_max_fuzz_ratio(files, loc)
		if rating != None:
			print "\033[92m" + "Moving %s %s \033[0m" % (sys.argv[1]+files,  dest)
			shutil.move(sys.argv[1]+files, dest)
		else:
			print '\033[91m' + "Cant find a folder for %s \033[0m" % files
'''