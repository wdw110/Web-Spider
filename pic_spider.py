#encoding=utf-8

import os
import requests
import urllib2
from bs4 import BeautifulSoup

class meitu(object):
	"""docstring for meitu"""
	def __init__(self):
		self.path_name = ''

	def all_url(self, url):
		html = self.request(url)
		all_a = BeautifulSoup(html, 'lxml').select('.all a')
		for a in all_a:
			title = a.get_text().encode('utf-8') #取出a标签的文本
			print '开始保存：%s' % title
			name = str(title).replace('?','_') #文件名
			tag = self.mkdir(name)
			if tag:
				href = a['href']   #取出a标签的href属性
				self.html(href)    #href:网页的地址
			else:
				continue

	def html(self, href):
		html = self.request(href)
		max_span = BeautifulSoup(html, 'lxml').select('.pagenavi span')[-2].get_text()
		for page in range(1,int(max_span)+1):
			page_url = href + '/' + str(page)
			self.img(page_url)

	def img(self, page_url):
		img_html = self.request(page_url)
		img_url = BeautifulSoup(img_html, 'lxml').select('.main-image img')[0]['src']
		self.save(img_url)

	def save(self, img_url):
		name = img_url[-9:-4]
		img = self.request(img_url)
		path = self.path_name
		with open(path+'/'+name+'.jpg','wb') as f:
			f.write(img)

	def request(self, url):
		headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
		request = urllib2.Request(url) #构建请求的request
		response = urllib2.urlopen(request)
		content = response.read()
		#content = requests.get(url, headers=headers)
		return content

	def mkdir(self, name): #name:文件名
		path = os.path.join('/Users/wdw/Desktop/test/Python/Web_Spider/data/pic',name)
		self.path_name = path
		isExists = os.path.exists(path)
		if not isExists:
			print '建一个名字叫做%s的文件夹' % name
			os.mkdir(path)
			return True
		else:
			print '名字叫做%s的文件夹已经存在了' % name
		return False

Mtu = meitu()
Mtu.all_url('http://www.mzitu.com/all')
