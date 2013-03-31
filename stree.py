import math

def chrildren(index):
	p1 = index + get_level(index)
	p2 = index + get_level(index) + 1

	if (get_level(p1) != get_level(index) or get_level(p2) != get_level(index)):
		if get_level(p1) != get_level(index):
			if get_level(p2) != get_level(index):
				return [p1, p2]
			return [p1]
		else:
			return [p2]
	return None

def get_level(index):
	return int(math.floor((math.sqrt(8 * index + 1) - 1) / 2) + 1)
	# It works from a derivation from the Quadratic equasion

def parrents(index):
	if index == 1:
		return [0]
	p1 = index - get_level(index)
	p2 = index - get_level(index) + 1

	if p1 > -1 and p2 > -1 and (get_level(p1) == get_level(index) - 1 or get_level(p2) == get_level(index) - 1):
		if get_level(p1) == get_level(index) - 1:
			if get_level(p2) == get_level(index)-1:
				return [p1, p2]
			return [p1]
		else:
			return [p2]
	return None

def generate_string(string):
	ret = []
	start =0
	length = len(string)
	end = len(string)
	while length >= 1:
		while start+length <= end:
			ret.append(string[start:start+length])
			start +=1
		length -=1
		start=0
	return ret

def string_match(string1, string2):
	match1 = generate_string(string1)
	match2 = generate_string(string2)

	matches = sorted(set(match1) & set(match2), key = len, reverse=True)

	count =0

	while count < len(matches):
		i=0
		while i < len(matches):
			if i != count and not matches[count].find(matches[i]) == -1:
				del matches[i]
			else:
				i+=1
		count +=1

	#print "\nIndex: ",  string1.index(x), string2.index(x)
	return 100 * sum( [ len(x) / float(2*(abs(string1.index(x) - string2.index(x))+1)*len(string1)) + len(x) / float(2*(abs(string1.index(x) - string2.index(x))+1)*len(string2)) for x in matches])