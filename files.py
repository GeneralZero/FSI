import subprocess as sub
import re
import os
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
	return None

loc = ['/media/Server_RAID_5/tv', '/media/Server_RAID_5/anime']

for files in os.listdir('/home/generalzero/Downloads/torrents/'):
	print files
	print get_max_fuzz_ratio(files, loc)
	print 
