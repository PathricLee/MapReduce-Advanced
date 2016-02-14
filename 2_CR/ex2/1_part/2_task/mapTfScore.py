#!/usr/bin/python
import sys

def main():
	#prepare the terms list
	terms = []
	term_file_name = 'terms.txt'
	for line in file(term_file_name):
		terms.append(line.strip())


        for line in sys.stdin:
                line = line.rstrip('\n')
		word = line.split(':\t')[0].strip()
		if word in terms:
			print line

if __name__ == '__main__':
        main()

