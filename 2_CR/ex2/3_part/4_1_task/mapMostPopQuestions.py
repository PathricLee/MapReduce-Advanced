#!/usr/bin/python
import sys
import re
from xml.dom.minidom import parseString

#this job will parse the stackoverflow logs 
def main():
	most_pop_question_dict= {}
	max_size = 10

        for line in sys.stdin:
                line = line.strip()
		#Log content details######
		stack_contents = dict( parseString(line).documentElement.attributes.items())
		rowId = get_item(stack_contents, 'Id')
		post_type_id = get_item(stack_contents, 'PostTypeId')

		if post_type_id == '1': #question
			view_count = int(get_item(stack_contents, 'ViewCount'))
			if len(most_pop_question_dict.keys()) < max_size:
				most_pop_question_dict[rowId] = view_count
			elif view_count >= min(most_pop_question_dict.values()):
                               	del most_pop_question_dict[min(most_pop_question_dict.items(), key=lambda x: x[1])[0]]
                               	most_pop_question_dict[rowId] = view_count

	emit(most_pop_question_dict)

def get_item(my_dict, item):
	if item in my_dict.keys():
		return my_dict[item]

def emit(most_pop_question_dict):
        for item in most_pop_question_dict.keys():
                print str(most_pop_question_dict[item]) + '\t' + item

if __name__ == '__main__':
        main()

