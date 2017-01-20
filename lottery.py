#encoding=utf-8

import re
import sys
import urllib
import urllib2
import requests
import numpy as np

url = 'http://www.lottery.gov.cn/historykj/'
types = ['dlt','qxc'] #彩票类型：大乐透，七星彩
lot_arr = [20,18]
if len(sys.argv)>1:
	lot_id = int(sys.argv[1])
else:
	print '请输入彩票类型！'
	sys.exit()
lot = types[lot_id]
lot_len = lot_arr[lot_id]

def getPage(pagNum,n,url):
	url += 'history_%d.jspx?_ltype=%s' % (pagNum,types[n])
	while True:
		try:
			request = urllib2.Request(url)
			response = urllib2.urlopen(request,timeout=10)
		except urllib2.URLError as e:
			print '网络连接出现问题, 正在尝试再次请求!'
		else:
			break
	res = response.read()
	return res

def getPageNum(content): #传入内容，获取共有多少页
	pattern = re.compile('<div class="page".*?<div>(.*?)&nbsp',re.S)
	result = re.search(pattern,content)
	Num = int(result.group(1).strip().split('/')[1].strip('页'))
	return Num

def getTitle(content):
	pattern = re.compile('<div class="result".*?<thead>.*?<tr>(.*?)</tr>.*?<tr>(.*?)</tr>.*?</thead>',re.S)
	result = re.findall(pattern,content)
	removeth = re.compile('<th.*?>(.*?)</th>')
	removead = re.compile('<strong>|</strong>|<br />| ')
	ss = re.findall(removeth,result[0][0])
	res = [re.sub(removead,'',i) for i in ss]
	#print res

def getContent(content):
	pattern = re.compile('<div class="result".*?<thead>.*?<tr>(.*?)</tr>.*?<tr>(.*?)</tr>.*?</thead>',re.S)
	removetb = re.compile('<td.*?>(.*?)</td>')
	res = re.findall(removetb,content)
	m,n = len(res)/lot_len,lot_len
	res = np.array(res).reshape(m,n)
	result = np.delete(res,-4,1)
	return result

content = getPage(1,lot_id,url)
N = getPageNum(content)
getTitle(content)

filename = "data/lottery_%s.txt" % lot
with open(filename,'w') as f1:
	for i in range(1,N+1):
		print '正在爬取%s的数据的第%d页...' %(lot,i)
		content = getPage(i,lot_id,url)
		data = getContent(content)
		for j in range(len(data)):
			if lot_id==1:
				lot_data = '\t'.join(list(data[j][1]))
				data[j][1] = lot_data
			string = '\t'.join(data[j])
			f1.write(string+'\n')

