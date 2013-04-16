import sys
import json
from fingerprint import FingerPrint


blkid = 0
f = FingerPrint()
for line in sys.stdin:
	blkid+=1
	data = json.loads(line)
	for k,v in data.iteritems():
		for title in v:
			print "\t".join([f.bigram_fingerprint_num(title),str(blkid),title])