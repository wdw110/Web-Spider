#encoding=utf-8

import re
import sys
import socket
import urllib
import urllib2
import requests
import numpy as np
from bs4 import BeautifulSoup

if len(sys.argv)>1:
	lot_id = int(sys.argv[1])
else:
	print '请输入彩票类型！'
	sys.exit()

class Lottery(object):
	"""docstring for Lottery"""
	def __init__(self):
		self.url = 'http://www.lottery.gov.cn'
		self.types = ['dlt','qxc'] #彩票类型：大乐透，七星彩
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

	def getPage(self, pagNum):
		label = self.types[lot_id] #彩票类型
		url = self.url + '/historykj/history_%d.jspx?_ltype=%s' % (pagNum,label)
		try:
			request = urllib2.Request(url, headers=self.headers)
			response = urllib2.urlopen(request, timeout=10)
			res = response.read()
		except urllib2.URLError as e:
			print '网络连接出现问题, 正在尝试再次请求!'
			return None
		except socket.timeout:
			print 'socket timeout'
			return None
		return res

	def getPageNum(self, content): #传入内容，获取共有多少页
		pattern = re.compile('<div class="page".*?<div>(.*?)&nbsp',re.S)
		result = re.search(pattern,content)
		Num = int(result.group(1).strip().split('/')[1].strip('页'))
		return Num

	def getTitle(self, content):
		res = []
		Soup = BeautifulSoup(content, 'lxml')
		thead = Soup.select('.result table thead tr th')[0:10]
		for th in thead:
			tag = th.get_text().strip()
			if th.attrs.has_key('colspan'):
				num = int(th['colspan'])
				for i in range(1, num+1):
					tmp = tag
					tmp += str(i)
					res.append(tmp)
			else:
				res.append(tag)
		return res

	def getInfo(self, content):
		result = []
		Soup = BeautifulSoup(content, 'lxml')
		tr_list = Soup.select('div.result tbody tr')
		for tr in tr_list:
			td_list = tr.select('td')
			tmp = [td.get_text() for td in td_list]
			if len(td_list)>4:
				tmp[-4] = self.url + td_list[-4].find('a')['href']
				result.append(tmp)
		return result

	def getAll(self):
		label = self.types[lot_id]
		N = self.getPageNum(self.getPage(1)) #总页数
		title = self.getTitle(self.getPage(1)) #表格列名
		filename = "data/lottery_%s.txt" % label
		with open(filename,'w') as f1:
			f1.write('\t'.join(title).encode('utf-8')+'\n')
			for i in range(1,N+1):
				while True:
					print '正在爬取%s的数据的第%d页...' %(label,i)
					content = self.getPage(i)
					if content: break
				info_list = self.getInfo(content)
				for j in range(len(info_list)):
					f1.write('\t'.join(info_list[j]).encode('utf-8')+'\n')

lot = Lottery()
lot.getAll()
