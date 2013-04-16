import sys
from Levenshtein import distance

DISTANCE = 15

cluster = []

cid = 0

for line in sys.stdin:
	cols = line.strip().split("\t")
	if len(cluster) == 0:
		cluster.append(cols)
	else:
		last = cluster[-1]
		if distance(last[0],cols[0]) <= DISTANCE:
			cluster.append(cols)
		else:
			print
			for c in cluster:
				if cid != 0:
					print "%s\t%s" % (cid,"\t".join(c))
			cluster = []
			cid+=1




	
