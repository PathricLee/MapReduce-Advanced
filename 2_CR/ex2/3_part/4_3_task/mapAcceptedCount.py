#!/usr/bin/python

import sys

def main():
	prev_owner_id = ''
	total_count = 0
	rowIdList = []
	for line in sys.stdin:
		line = line.strip()
		owner_id, rowId, count = line.split()
		count = int(count)
		if owner_id == prev_owner_id:
			total_count += count
			rowIdList.append(rowId)
		else:
			if prev_owner_id:
				emit(prev_owner_id, total_count, rowIdList)
			total_count = count
			rowIdList = []
			rowIdList.append(rowId)
			prev_owner_id = owner_id
	emit(prev_owner_id, total_count, rowIdList)

def emit(owner_user_id, total_count, rowIdList ):
	row_id_string = ','.join(rowIdList)
	delim = '\t'
	print owner_user_id + delim + str(total_count) + delim + row_id_string

if __name__ == '__main__':
        main()

