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

		self.dic = dic
		self.path = path
		self.output = output_name
		self.number = 0

		self.text = []

	def load_file(self):
		'''
			load_file: load input file and make it into a list of strings
		'''
		with open(self.path, 'r') as f:
			lines = f.readlines()
		lines = lines[0].split('.')
		self.text = lines

	def make_number_list(self):
		'''
			make_number_list: transter the text into prefered form and return a
		'''

		file = open(self.output, 'w')
		for line in self.text:
			seperate_line = nltk.word_tokenize(line)
			
			if not seperate_line:
				continue
			# Number one
			elif seperate_line[0] == 'Number' and seperate_line[1] != 'next':
				self.number = self.dic[seperate_line[1]]
				# make capitalize
				seperate_line[2][0].upper()
				sentence = ' '.join(seperate_line[2:])
				file.write('\n' + str(self.number) + '.' + sentence + '\n')
			# Number next
			elif seperate_line[0] == 'Number' and seperate_line[1] == 'next':
				self.number += 1
				seperate_line[2][0].upper()
				sentence = ' '.join(seperate_line[2:])
				file.write(str(self.number) + '.' + sentence + '\n')
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