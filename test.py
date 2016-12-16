#encoding=utf-8

import urllib2

response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()

req = urllib2.Request('http://www.baidu.com')
res = urllib2.urlopen(req)
the_page = res.read()
#print the_page

from urllib2 import Request, urlopen, URLError, HTTPError  
  
old_url = 'http://www.baidu.com'  
req = Request(old_url)
response = urlopen(req)
print 'Info():'
print response.info()