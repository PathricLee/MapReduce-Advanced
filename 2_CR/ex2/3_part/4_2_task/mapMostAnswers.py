#!/usr/bin/python
import sys

def main():
	max_count = 0
	max_owner_id = ''
	max_post_list = ''
        for line in sys.stdin:
                line = line.strip()
		owner_user_id, count, post_list = line.split('\t')
		count = int(count)
		if count > max_count:
			max_owner_id = owner_user_id
			max_post_list = post_list
			max_count = count
	emit(max_owner_id, max_post_list, max_count)

def emit(owner_user_id, post_list, count):
	print owner_user_id + '\t' + post_list + '\t' + str(count)

if __name__ == '__main__':
        main()

