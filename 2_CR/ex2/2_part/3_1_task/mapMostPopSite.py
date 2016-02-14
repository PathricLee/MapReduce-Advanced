#!/usr/bin/python
import sys
import re

#This will identify the top site inside this mapper
#only sends a single value to the reducer. so limiting the amount sent to reducer
def main():
	top_site_list = []
	top_site_count = 0
        for line in sys.stdin:
                line = line.strip()
		keyword, site, count = line.split()
		count = int(count)
		if keyword.strip() == 'SITE:':
			if count > top_site_count:
				top_site_list = []
				top_site_list.append(site)
				top_site_count = count
			elif count == top_site_count:
				top_site_list.append(site)

	emit(top_site_list, top_site_count)

def emit(top_site_list, top_site_count):
	for site in top_site_list:
		print site + '\t' + str(top_site_count)

if __name__ == '__main__':
        main()

