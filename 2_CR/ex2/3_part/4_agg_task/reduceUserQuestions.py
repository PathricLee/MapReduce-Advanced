#!/usr/bin/python

import sys

def main():
	#set of vars for the answer section
	prev_owner_id_a = ''
	post_id_list_a = []
	total_count_a = 0
        for line in sys.stdin:
                line = line.strip()
                owner_user_id, post_id, count = line.split()
                count = int(count)
                if owner_user_id == prev_owner_id_a:
                	total_count_a += count
                        post_id_list_a.append(post_id)
                else:
                	if prev_owner_id_a:
                        	emit(prev_owner_id_a, post_id_list_a, total_count_a)
                        post_id_list_a = []
			post_id_list_a.append(post_id)
                        total_count_a = count
                        prev_owner_id_a = owner_user_id

	#last lines
	emit(owner_user_id, post_id_list_a, total_count_a)


def emit(owner_user_id, post_id_list, total_count):
	post_id_string = ','.join(post_id_list)
	delim = '\t'
	print owner_user_id + delim + str(total_count) + delim + post_id_string

if __name__ == '__main__':
        main()

