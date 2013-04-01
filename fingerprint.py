import sys
import re
import string
from nltk import bigrams
import itertools


class FingerPrint(object):
	"""docstring for FingerPrint"""
	def __init__(self):
		super(FingerPrint, self).__init__()
		self.regex = re.compile('[%s]' % re.escape(string.punctuation))
		
	def fingerprint(self,text):
		fp = " ".join(sorted(self.regex.sub("",text.strip().lower()).split()))
		return fp

	def bigram_fingerprint(self,text):
		postproc = self.regex.sub("",text.lower().replace(" ",""))
		bigrms =  bigrams(postproc)
		b = []
		for bi in bigrms:
			b.append("".join(bi))
		return "".join(sorted(set(b)))