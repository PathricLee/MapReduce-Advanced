#!/usr/bin/python
import sys
import re
from xml.dom.minidom import parseString

def main():

        for line in sys.stdin:
                line = line.strip()
		#resetting the variables we are going to be reading in
		rowId = ''
		post_type_id = ''
		answer_id = ''
		#Log content details######
		stack_contents = dict( parseString(line).documentElement.attributes.items())
		rowId = get_item(stack_contents, 'Id')
		post_type_id = get_item(stack_contents, 'PostTypeId')
		#print stack_contents
		if post_type_id == '1':#question
			answer_id = get_item(stack_contents,'AcceptedAnswerId')
			if answer_id:
				emit(answer_id, 'ANSWER_ID')
		elif post_type_id == '2': #answer
			owner_id = get_item(stack_contents, 'OwnerUserId')
			if owner_id and rowId:
				emit(rowId, owner_id)
		del(stack_contents)

def get_item(my_dict, item):
	if item in my_dict.keys():
		return my_dict[item];

def emit(post_id, val):
	print post_id + '\t' + val

if __name__ == '__main__':
        main()

