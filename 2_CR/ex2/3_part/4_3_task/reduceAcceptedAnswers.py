#!/usr/bin/python
import sys
import re

def main():
	prev_row_id = ''
	prev_val = ''
        for line in sys.stdin:
                line = line.strip()
		row_id, val = line.split()
		if row_id == prev_row_id:
			if prev_val == 'ANSWER_ID':
				emit(val, row_id)
			else:
				emit(prev_val, prev_row_id)
		else:
			prev_row_id = row_id
			prev_val = val

def emit(val, row_id):
	print val + '\t' + row_id + '\t' + '1'

if __name__ == '__main__':
        main()

