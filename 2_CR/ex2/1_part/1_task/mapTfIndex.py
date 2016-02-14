#!/usr/bin/python
import os
import sys

def main():
	counter = 0
	file_name = os.environ["mapreduce_map_input_file"]
	#file_name = '~/ExtremeComputing/ex1/1_part/1_task/small/d1.txt'
	file_name = file_name.split("/")[-1]
        for line in sys.stdin:
                line = line.strip()
		for word in line.split():
			emit(word, file_name)

def emit(word, file_name):
	print (word + '\t' + file_name + '\t' + '1')

#main() func is a recurring feature in all my code
#I like functions better than running the code like a script
#More readable for a human
if __name__ == '__main__':
        main()

