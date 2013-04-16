import sys
import re
import string

BLOCK_SIZE = 6
regex = re.compile('[%s]' % re.escape(string.punctuation))
regex_s = re.compile(r'\W+')
for line in sys.stdin:
	pre = regex_s.sub(" ",regex.sub(" ",line.strip().lower()))
	start = 0
	end = BLOCK_SIZE
	for i in xrange(0,len(pre)):
		if end <= len(pre):
			print "%s\t%s" % (pre[start:end],line.strip())
			start+=1
			end+=1


