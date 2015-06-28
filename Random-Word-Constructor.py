import random

"""A Random Word Generator that uses a built-in algorithm that follows the syllable rules
in the English language. Useful for finding a creative name for a business or app."""
	

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
consensnts = [x for x in alphabet if x not in vowels]
starting_letters = ['c', 'd', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'y', 'z' ]

class Random_Word_Constructor (object):
	
	def __init__(self, maxlength):
		self.maxlength = maxlength
		self.dictionary = {}
		self.start = [x for x in alphabet if x != 'x' and x != 'u']
		self.word = ''
		self.word += self.start[random.randrange(len(self.start))]
		self.preceed_Vowel_letters = ['b', 'd', 'j', 'w', 'z', 'q']
		self.a = [x for x in alphabet if x != 'a' and x != 'h' and x != 'u']
		self.e = [x for x in alphabet if x != 'h']
		self.i = [x for x in alphabet if x != 'i' and x != 'h' and x != 'u' and x != 'y']
		self.o = [x for x in alphabet if x != 'a' and x != 'e' and x != 'i' and x != 'y']
		self.u = [x for x in consensnts if x != 'y' and x != 'u']
		self.y = ['o', 'a', 'e', 'u']
		self.cons_next = ['a', 'i', 'e', 'o', 'u', 't', 'r']
	def construct_word(self):
		while len(self.word) < self.maxlength:
			if len(self.word) >= 2:
				if self.word[-2] and self.word[-1] in vowels:
					self.word += consensnts[random.randrange(len(consensnts))]
				if self.word[-2] and self.word[-1] in consensnts:
					self.word += vowels[random.randrange(len(vowels))]
			if self.word[-1] in vowels:
				if self.word[-1] == 'a':
					self.word += self.a[random.randrange(len(self.a))]
				if self.word[-1] == 'e':
					self.word += self.e[random.randrange(len(self.e))]
				if self.word[-1] == 'i':
					self.word += self.i[random.randrange(len(self.i))]
				if self.word[-1] == 'o':
					self.word += self.o[random.randrange(len(self.o))]
				if self.word[-1] == 'u':
					self.word += self.u[random.randrange(len(self.u))]
			if self.word[-1] in consensnts:
				if self.word[-1] in self.preceed_Vowel_letters:
					self.word += vowels[random.randrange(len(vowels))]
				if self.word[-1] == 'y':
					self.word += self.y[random.randrange(len(self.y))]
				else:
					self.word += self.cons_next[random.randrange(len(self.cons_next))]
		self.word = self.word[0:self.maxlength]
		return self.word
	def add_to_dictionary(self):
		if self.word[0] in self.dictionary.keys():
			self.dictionary[self.word[0]].append(self.word)
			self.word = '' + self.start[random.randrange(len(self.start))]
		else:
			self.dictionary.update({self.word[0]:[self.word]})
			self.word = '' + self.start[random.randrange(len(self.start))]


def Random_Word(maxlength): #returns a single random word
	word = Random_Word_Constructor(maxlength)
	return word.construct_word()
def Random_Dictionary(entries, maxlength): #returns a dictionary of specificed number of entries, and prints them.
	word, count = Random_Word_Constructor(maxlength), 0
	while count < entries:
		word.construct_word()
		word.add_to_dictionary()
		count += 1
	for k, v in word.dictionary.items():
		print k, v 	
	



