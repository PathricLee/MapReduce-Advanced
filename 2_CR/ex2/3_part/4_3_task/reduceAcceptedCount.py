#!/usr/bin/python

import sys

def main():
	prev_owner_id = ''
	total_count = 0
	row_id_list = ''
	for line in sys.stdin:
		line = line.strip()
		owner_id, count, row_id_string  = line.split()
		count = int(count)
		if owner_id == prev_owner_id:
			total_count += count
			row_id_list += ',' + row_id_string
		else:
			if prev_owner_id:
				emit(prev_owner_id, total_count, row_id_list)
			total_count = count
			row_id_list = row_id_string
			prev_owner_id = owner_id
	emit(prev_owner_id, total_count, row_id_list)

def emit(owner_user_id, total_count, row_id_list ):
	delim = '\t'
	print owner_user_id + delim + str(total_count) + delim + row_id_list

if __name__ == '__main__':
        main()

