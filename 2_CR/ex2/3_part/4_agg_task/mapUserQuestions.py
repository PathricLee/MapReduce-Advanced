#!/usr/bin/python
import sys
from xml.dom.minidom import parseString

#this job will parse the stackoverflow logs 
#output from this job will be used for 4.2 and 4.3
def main():
	most_pop_question_dict= {}
	max_size = 10

        for line in sys.stdin:
                line = line.strip()
		#resetting the variables we are going to be reading in
		rowId = ''
		post_type_id = ''
		owner_user_id = ''
		answer_id = ''
		parent_id = ''
		#Log content details######
		stack_contents = dict( parseString(line).documentElement.attributes.items())

		rowId = get_item(stack_contents, 'Id')
		post_type_id = get_item(stack_contents, 'PostTypeId')
		
		if not rowId or not post_type_id:
			raise ValueError

		if post_type_id == '2': #answer
			owner_user_id = get_item(stack_contents, 'OwnerUserId')
			parent_id = get_item(stack_contents, 'ParentId')
			if owner_user_id and parent_id:
				emit(owner_user_id, parent_id, post_type_id)
		del(stack_contents)


def get_item(my_dict, item):
	if item in my_dict.keys():
		return my_dict[item];

def emit(owner_user_id, post_id, post_type_id):
	delim = '\t'
	print owner_user_id + delim + post_id  + delim + '1'

if __name__ == '__main__':
        main()

