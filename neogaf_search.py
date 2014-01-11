#! /usr/bin/env python
'''Personal Interest helping myself to search the thread title in the Neogaf Forum
by Zhizhuo Ding'''
import sys,urllib2
import re

def find_key_word(key,src):
	#ignore the case
	k = key.lower()
	s = src.lower()
 	if s.find(k) != -1 :
 		return True
 	else:
 		return False

#user determine the keyword and the number of pages they want to search
# query = "Nintendo"
# maxPage = 10
query = str(sys.argv[1])
maxPage = int(sys.argv[2])

#the reg formula and build the regObject
reg = r'(<a class="threadbit-title" href="(.*)" id=".*">(?P<title>.*)</a>)'
p = re.compile(reg)

#component for url
prev = r"http://www.neogaf.com/forum/"
page = r"&order=desc&page="
home = r"http://www.neogaf.com/forum/forumdisplay.php?f=2"
url = home

current_page = 1

rec = []
while current_page<=maxPage:
	#start get first page
	req = urllib2.Request(url)
	#get the feedback
	fd = urllib2.urlopen(req)
	#get all the useful data from the page
	alldata= fd.read()
	datalist = p.findall(alldata)

	#iterate all titles found in the page
	for i in datalist:
		if find_key_word(query,i[2]):
			rec.append( (current_page,i[2], prev+i[1]) )
	#change the url to the next page
	current_page += 1
	url = home+page+str(current_page)

if rec:	
	for i in rec:
		print i
		#sys.stdout.write(i)
else:
	print "Can't find the topic"
	#sys.stdout.write("Can't find the topic")