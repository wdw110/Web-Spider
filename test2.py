#encoding=utf-8

import re
import urllib
import urllib2
import requests

url = 'http://www.lottery.gov.cn/historykj/'
types = ['dlt','qxc'] #彩票类型：大乐透，七星彩

def getPage(pagNum,n,url):
	url += 'history_%d.jspx?_ltype=%s' % (pagNum,types[n])
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	res = response.read()
	return res

def getPageNum(content): #传入内容，获取共有多少页
	pattern = re.compile('<div class="page".*?<div>(.*?)&nbsp',re.S)
	result = re.search(pattern,content)
	Num = int(result.group(1).strip().split('/')[1].strip('页'))
	return Num

def getTitle(content):
	pattern = re.compile('<div class="result".*?<thead>.*?<tr>(.*?)</tr>.*?<tr>(.*?)</tr></thead>',re.S)
	result = re.search(pattern,content).group(1).strip()
	print result

def getContent(content):
	pattern = re.compile('<div class="result".*?<>(.*?)&nbsp',re.S)
	result = re.search(pattern,content)


content = getPage(1,0,url)
N = getPageNum(content)
print N
getTitle(content)



