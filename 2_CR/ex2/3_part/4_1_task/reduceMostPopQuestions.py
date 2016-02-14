#!/usr/bin/python

import sys

def main():
        most_pop_question_dict = {}
	max_size = 10
        for line in sys.stdin:
                line = line.strip()
                view_count, rowId = line.split()
                view_count = int(view_count)
                if len(most_pop_question_dict.keys()) < 10:
                        most_pop_question_dict[rowId] = view_count
                elif view_count >= min(most_pop_question_dict.values()):
                        del most_pop_question_dict[min(most_pop_question_dict.items(), key=lambda x: x[1])[0]]
                        most_pop_question_dict[rowId] = view_count
        emit(most_pop_question_dict)

def emit(most_pop_question_dict):
        for item in sorted(most_pop_question_dict, key=most_pop_question_dict.get, reverse=True):
                print item + ',\t' + str(most_pop_question_dict[item])


if __name__ == '__main__':
        main()

