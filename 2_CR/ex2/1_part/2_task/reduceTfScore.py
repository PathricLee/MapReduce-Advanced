#!/usr/bin/python

import sys
import math

marked_file_name = 'd1.txt'

def main():
	terms_file  = 'terms.txt'
	terms = []
	for line in file(terms_file):
		terms.append(line.strip())
	terms_seen = []
        for line in sys.stdin:
		num_files= 0
		tf_frequency = 0
		line = line.rstrip('\n')
		word, total_count, index_map = line.split(':')
		word = word.strip()
		#removing all the chars not required to break down this token further
		index_map = index_map.replace('{','').replace('}','').replace('(','')
		for file_index in index_map.split('),'):
			file_name, count = file_index.split(',')
			file_name = file_name.strip()
			num_files+=1
			if file_name == marked_file_name:
				tf_frequency = int(count.replace(')','').strip())
		idf_term = calc_idf(num_files)
		tf_idf_score = tf_frequency * idf_term
		terms_seen.append(word)
		emit(word, marked_file_name, tf_idf_score)
	
	#this will emit a zero score for any term which has not been encountered
	for term in terms:
		if term not in terms_seen:
			emit(term, marked_file_name, 0.0)

def calc_idf(num_files):
	''' calculate the idf value for the term based on the number of files in which its found '''
	N = 17.0
	return math.log10(N/(1+num_files))

def emit(word, file_name, tf_idf_score):
	''' print out the tf score for the terms to std out in the format required '''
	print word + ', ' + file_name + ' = ' + str(tf_idf_score)

if __name__ == '__main__':
        main()

