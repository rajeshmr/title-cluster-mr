from itertools import groupby
from operator import itemgetter
import sys
import json

def read_mapper_output(file, separator='\t'):
	for line in file:
		yield line.rstrip().split(separator, 1)

def main(separator='\t'):
	# input comes from STDIN (standard input)
	data = read_mapper_output(sys.stdin, separator=separator)
	for block, group in groupby(data, itemgetter(0)):
		try:
			t={}
			t[block] = []
			for blk,title in group:
				t[block].append(title)
			print json.dumps(t)
		except ValueError:
			pass

if __name__ == "__main__":
    main()