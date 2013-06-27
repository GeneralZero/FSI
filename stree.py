import math

class STree(object):
	"""docstring for STree"""
	def __init__(self, string1):
		self.master_string = string1
		self.structure = []
		self.purge_list = []
		self.generate_structure()

	def generate_structure(self):		
		start =0
		length = len(self.master_string)
		end = len(self.master_string)
		while length >= 1:
			while start+length <= end:
				self.structure.append([self.master_string[start:start+length], True])
				start +=1
			length -=1
			start=0

	def purge_structure():
		i=0
		while self.structure[i] != None:
			del self.structure[i]
			i+=1

		for sub_string, valid in self.structure:

	def delete(self, index):
		self.delete_up(index)
		self.delete_down(index)

	def string_list(self):
		for num, x in enumerate(self.structure):
			print num , x[0]

	def delete_up(self, index):
		for x in self.parrents(index):
			self.structure[x][1] = False
			self.delete_up(x)

	def delete_down(self, index):
		for x in self.chrildren(index):
			self.structure[x][1] = False
			self.delete_down(x)

	def chrildren(self, index):
		p1 = index + self.get_level(index)
		p2 = index + self.get_level(index) + 1

		if (self.get_level(p1) != self.get_level(index) or self.get_level(p2) != self.get_level(index)):
			if self.get_level(p1) != self.get_level(index):
				if self.get_level(p2) != self.get_level(index):
					return [p1, p2]
				return [p1]
			else:
				return [p2]
		return None

	def get_level(self, index):
		return int(math.floor((math.sqrt(8 * index + 1) - 1) / 2) + 1)
		# It works from a derivation from the Quadratic equasion

	def parrents(self, index):
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

	def string_match(self, string2):
		match2 = generate_string(string2)

		matches = sorted(set(self.structure) & set(match2), key = len, reverse=True)

		count =0

		while count < len(matches):
			i=0
			while i < len(matches):
				if i != count and not matches[count].find(matches[i]) == -1:
					del matches[i]
				else:
					i+=1
			count +=1

		#print "\nIndex: ",  self.master_string.index(x), string2.index(x)
		return 100 * sum( [ len(x) / float(2*(abs(self.master_string.index(x) - string2.index(x))+1)*len(self.master_string)) + len(x) / float(2*(abs(self.master_string.index(x) - string2.index(x))+1)*len(string2)) for x in matches])
