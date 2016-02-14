#!/usr/bin/python
import sys
import datetime

#This will identify the top site inside this mapper
#only sends a single value to the reducer. so limiting the amount sent to reducer
def main():
	prev_host = ''
	num_visits = 0
        for line in sys.stdin:
		line = line.strip()
		host, req_time = line.split()
		host_time = datetime.datetime.strptime(req_time, "%Y%m%d%H%M%S")
		if host == prev_host:
			max_host_time = host_time
			num_visits +=1
		else:
			if prev_host:
				emit_time_diff(prev_host, min_host_time, max_host_time, num_visits)
			#reset the params
			min_host_time = max_host_time = host_time
			prev_host = host
			num_visits = 0
	#last line
	emit_time_diff(prev_host, min_host_time, max_host_time, num_visits)

def emit_time_diff(host, min_host_time, max_host_time, num_visits):
	if num_visits == 0:
		#converting it back to the original date format
		print host + '\t' + min_host_time.strftime("%d/%b/%Y:%H:%M:%S") + " -0400"
	else:
		time_diff = max_host_time - min_host_time
		print host + '\t' + str(time_diff.total_seconds())

if __name__ == '__main__':
        main()

