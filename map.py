import sys
import re
import string
from nltk import bigrams
from fingerprint import FingerPrint

f = FingerPrint()

for line in sys.stdin:
	cols = line.split("\t")
	try:
		print "%s\t%s\t%s" % (f.bigram_fingerprint_num(cols[2]),cols[0],cols[2])
	except:
		pass
	


	
