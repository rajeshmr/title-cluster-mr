import sys
import re
import string
from nltk import bigrams
from fingerprint import FingerPrint

regex = re.compile('[%s]' % re.escape(string.punctuation))
f = FingerPrint()

for line in sys.stdin:
	cols = line.split("\t")
	# try:
	if cols[2] != "":
		print "%s\t%s\t%s" % (f.bigram_fingerprint(cols[2]),cols[2],cols[7])
	# except:
	# 	pass
	


	