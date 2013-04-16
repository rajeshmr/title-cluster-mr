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
		self.remnum = re.compile('[\d]+')
	def clean(self,text):
		return " ".join(set(text.strip().lower().split()))
	
	def fingerprint(self,text):
		fp = " ".join(sorted(self.regex.sub("",self.clean(text)).split()))
		return fp

	def bigram_fingerprint(self,text):
		postproc = self.regex.sub("",self.clean(text).replace(" ",""))
		bigrms =  bigrams(postproc)
		b = []
		for bi in bigrms:
			b.append("".join(bi))
		return "".join(sorted(set(b)))

	def bigram_fingerprint_num(self,text):
		postproc = self.regex.sub("",self.remnum.sub("num",self.clean(text)).replace(" ",""))
		bigrms =  bigrams(postproc)
		b = []
		for bi in bigrms:
			b.append("".join(bi))
		return "".join(sorted(set(b)))