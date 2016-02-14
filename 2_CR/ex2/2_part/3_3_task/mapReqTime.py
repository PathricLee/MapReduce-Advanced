#!/usr/bin/python
import sys
import datetime
import re

def main():
        for line in sys.stdin:
		site_counter = 1
                line = line.strip()
		#regex below describes the apace log file format
		log_content = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
		if len( log_content) == 7:
			try:
				host = log_content[0]
				req_time = log_content[3]
				req_time = req_time.split()[0] #throwing away the timezone info as we assume all timezones are same
				host_time = datetime.datetime.strptime(req_time,  "%d/%b/%Y:%H:%M:%S" )
				host_time_string = host_time.strftime("%Y%m%d%H%M%S")
				emit(host, host_time_string)
			except:
				#in case of format issues, we skip this line
				pass

def emit(host, req_time):
	print host + '\t' + req_time

if __name__ == '__main__':
        main()

