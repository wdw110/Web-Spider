#encoding=utf-8

import requests
from bs4 import BeautifulSoup

class PicDown(object):
	"""docstring for PicDown"""
	def __init__(self):
		self.url ='http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1485248120811_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1485248120812%5E00_729X612&word=%E5%B0%8F%E9%BB%84%E4%BA%BA'
	
	def getPage(self):
		html = requests.get(self.url)
		html.encoding='utf-8'
		print html.content
		Soup = BeautifulSoup(html.text, 'lxml')
		li_list = Soup.select('div #imgid')
		print li_list
		for li in li_list:
			print li['href']


if __name__ == '__main__':
	a = PicDown()
	a.getPage()