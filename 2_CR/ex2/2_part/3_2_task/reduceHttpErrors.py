#!/usr/bin/python
import sys
import re

def main():
	err_host_dict = {}
        for line in sys.stdin:
                line = line.strip()
		host, count = line.split()
		count = int(count)
		if len(err_host_dict.keys()) < 10:
			err_host_dict[host] = count
		elif count >= min(err_host_dict.values()):
			del err_host_dict[min(err_host_dict.items(), key=lambda x: x[1])[0]]
			err_host_dict[host] = count
	emit(err_host_dict)

def emit(err_host_dict):
	for item in err_host_dict.keys():
		print item + '\t' + str(err_host_dict[item])

if __name__ == '__main__':
        main()

