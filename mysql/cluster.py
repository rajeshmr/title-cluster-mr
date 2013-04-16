import MySQLdb as mdb
import sys
import re
import string
from Levenshtein import distance

BLOCK_SIZE = 6
con = mdb.connect('localhost', 'root', '', 'clustering');
with con:
	cur = con.cursor(mdb.cursors.DictCursor)
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