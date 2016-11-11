#encoding=utf-8

import re
import urllib
import urllib2

page = 2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
headers = {  
   'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
}  

try:
	request = urllib2.Request(url,headers=headers)
	response = urllib2.urlopen(request)
	#print response.read()
except urllib2.URLError as e:
	if hasattr(e,'code'):
		print e.code
	if hasattr(e,'reason'):
		print e.reason

content = response.read().decode('utf-8')
pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
items = re.findall(pattern,content)
for item in items:
	print item[0],item[1],item[2]

