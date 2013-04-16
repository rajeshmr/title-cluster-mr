import MySQLdb as mdb
import sys
import re
import string
from Levenshtein import distance

regex = re.compile('[%s]' % re.escape(string.punctuation))
regex_s = re.compile(r'\W+')
BLOCK_SIZE = 6
con = mdb.connect('localhost', 'root', '', 'clustering');
with con:
	cur = con.cursor(mdb.cursors.DictCursor)
	for line in sys.stdin:
		#feed titles 
		try:
			cols = line.split("\t")
			if cols[2].strip() != "":
				sql = """INSERT INTO `clustering`.`titles` (`id`, `pid`, `title`) VALUES (NULL, '%s', '%s');""" % (cols[0].strip(),re.escape(cols[2].strip()))
				cur.execute(sql)
		except:
			pass
	
	# Calculate blocks
	sql = """ SELECT * FROM `titles` """
	cur.execute(sql)
	titles = cur.fetchall()
	for title in titles:
		pre = regex_s.sub(" ",regex.sub(" ",title['title'].strip().lower()))
		start = 0
		end = BLOCK_SIZE
		for i in xrange(0,len(pre)):
			if end <= len(pre):
				bid = 0
				try:
					sql = """SELECT * FROM `blocks` WHERE `block` like '%s'""" % pre[start:end]
					cur.execute(sql)
					blk = cur.fetchone()
					if blk:
						sql = """ INSERT INTO `clustering`.`block_title_mapping` (`id`, `bid`, `tid`) VALUES (NULL, '%d', '%d'); """ % (blk['id'],title['id'])
						cur.execute(sql)
					else:
						print "else"
						sql = """ INSERT INTO `clustering`.`blocks` (`id`, `block`) VALUES (NULL, '%s'); """ % pre[start:end]
						cur.execute(sql)
						bid = cur.lastrowid
						sql = """ INSERT INTO `clustering`.`block_title_mapping` (`id`, `bid`, `tid`) VALUES (NULL, '%d', '%d'); """ % (bid,title['id'])
						cur.execute(sql)
					start+=1
					end+=1
				except e:
					print e
					break

	# get title for every block
	sql = """ SELECT COUNT(*) AS `rows`, `block` FROM `blocks` GROUP BY `block` ORDER BY `block` """
	cur.execute(sql)
	blkkwds = cur.fetchall()
	for kw in blkkwds:
		sql = """ select t.title,t.id,b.block from titles t join  block_title_mapping m on m.tid = t.id join blocks b on b.id = m.bid and b.block like '%s' """ % kw['block']
		cur.execute(sql)
		titles = cur.fetchall()
		for title in titles:
			print title['title'] 
		print


