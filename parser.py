import argparse
import nltk

class Parser:

	'''
		Parser: A class object that helps doctors to transfer text into prefered strings
		Args:
			dic: dictionary that keys are words one to nine and values are number 1 - 9
			path: input file path
			output_name: output file name
	'''
	def __init__(self, dic, path, output_name):

		self.dic_ = dic
		self.path_ = path
		self.output_ = output_name
		self.number_ = 0

		self.text_ = []

	def load_file(self):
		'''
			load_file: load input file and make it into a list of strings
		'''
		with open(self.path_, 'r') as f:
			lines = f.readlines()
		lines = lines[0].split('.')
		self.text_ = lines

	def make_number_list(self):
		'''
			make_number_list: transter the text into prefered form and return a
		'''

		file = open(self.output_, 'w')
		for line in self.text_:
			seperate_line = nltk.word_tokenize(line)
			
			if not seperate_line:
				continue
			# Number one
			elif seperate_line[0] == 'Number' and seperate_line[1] != 'next':
				self.number_ = self.dic_[seperate_line[1]]
				# make capitalize
				if not seperate_line[2].isupper():
					seperate_line[2] = seperate_line[2].capitalize()
				sentence = ' '.join(seperate_line[2:])
				file.write('\n' + str(self.number_) + '.' + sentence + '\n')
			# Number next
			elif seperate_line[0] == 'Number' and seperate_line[1] == 'next':
				self.number_ += 1
				if not seperate_line[2].isupper():
					seperate_line[2] = seperate_line[2].capitalize()
				sentence = ' '.join(seperate_line[2:])
				file.write(str(self.number_) + '.' + sentence + '\n')
			# description sentences
			else:
				file.write(line)
		file.close()



if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Short sample app')

	parser.add_argument('input', help='input file path')
	parser.add_argument('output', help='output file name')
	
	results = parser.parse_args()
	input_path = results.input
	output_name = results.output

	dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
	'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

	p = Parser(dic, input_path, output_name)
	p.load_file()
	p.make_number_list()