#!/usr/bin/python
import os
import sys

#Combiner implemented to sum up on a file name level
def main():
	prev_file_name = ''
	prev_word = ''
	count = 0
        for line in sys.stdin:
                line = line.strip()
		word, file_name,_ = line.split('\t')
		if word==prev_word:
			if file_name == prev_file_name:
				count +=1
			else:
				if prev_file_name:
					emit(word, prev_file_name, count)
				#reset the params
				prev_file_name = file_name
				count =1
		else:
			if prev_word:
				emit(prev_word, prev_file_name, count)
			#reset the params
			prev_word = word
			prev_file_name = file_name
			count = 1
	#emit the last line
	emit (prev_word,prev_file_name, count)

def emit(word, file_name, count):
	print (word + '\t' + file_name + '\t' + str(count))

if __name__ == '__main__':
        main()

