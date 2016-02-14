#!/usr/bin/python
import sys
import re

#this job will aggregate the number of site visits and http error codes
#will be used for task 3.1 and 3.2
def main():
        for line in sys.stdin:
		site_counter = 1
                line = line.strip()
		#regex below describes the apace log file format
		log_content = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
		try:
			#Log content details######
			host = log_content[0]
			#req_time = log_content[3]
			http_code = log_content[5]
			if http_code == '404':
				emit('HTTP_ERROR: ' + host)
			try:
				req_type, req_site, protocol = log_content[4].split()
			except:
				#format issue observed here
				req_type, req_site = log_content[4].split()
			##########################
			emit('SITE: ' + req_site)
		except:
			#in case of format issues, we skip this line
			pass

def emit(token):
	aggregate_token = 'LongValueSum: '
	print aggregate_token + token + '\t' + '1'

if __name__ == '__main__':
        main()

