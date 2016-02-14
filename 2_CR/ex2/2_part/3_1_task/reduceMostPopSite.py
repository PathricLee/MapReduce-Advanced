#!/usr/bin/python

import sys

def main():
	top_site_list = []
	top_site_count = 0
        for line in sys.stdin:
		line = line.strip()
		site, count = line.split()
		count = int(count)
		if count > top_site_count:
			top_site_list = []
			top_site_list.append(site)
			top_site_count = count
		elif count == top_site_count:
			top_site_list.append(site)
		
	emit(top_site_list, top_site_count)

#handles the case where more than one site is top
def emit(top_site_list, top_site_count):
	for site in top_site_list:
		print site + '\t' + str(top_site_count)

if __name__ == '__main__':
        main()
