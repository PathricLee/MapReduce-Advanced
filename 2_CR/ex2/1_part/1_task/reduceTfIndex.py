#!/usr/bin/python

import sys

def main():
	prev_word = ''
	prev_file_name = ''
        for line in sys.stdin:
		line = line.strip()
		word,file_name, count = line.split('\t') 
		count = int(count)
		if prev_word == word:
			if prev_file_name == file_name:
				file_count_hash_map[file_name] += count
			else:
				file_count_hash_map[file_name] = count
				prev_file_name = file_name
			total_count += count
		else:
			if prev_word:
				emit(prev_word, total_count, file_count_hash_map)
			#reset the counters
			file_count_hash_map = {}
			total_count = count
			file_count_hash_map[file_name] = count
			prev_file_name = file_name
			prev_word = word	
	#last words
	emit(prev_word, total_count, file_count_hash_map)

def construct_file_string(file_name, file_word_count):
	return '('+ file_name +', ' + str(file_word_count) + ')'

def emit(word, count, file_count_hash_map):
	delim = ' :\t'
	emit_str = word + delim + str(count) + delim + '{'
	for file_name in sorted(file_count_hash_map):
		emit_str += construct_file_string(file_name, file_count_hash_map[file_name])
		emit_str += ', '
	emit_str = emit_str.rstrip(', ')
	emit_str += '}' 
	print emit_str

if __name__ == '__main__':
        main()

