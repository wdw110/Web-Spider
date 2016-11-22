#encoding=utf-8

import re
import sys
import time
import types
import urllib
import urllib2
from bs4 import BeautifulSoup
import mysql
import page

#构造最佳答案的字典
good_ans_dict = {
		"text": good_ans[0],
		"answerer": good_ans[1],
		"date": good_ans[2],
		"is_good": str(good_ans[3]),
		"question_id": str(insert_id)
		}

class Spider(object):
	"""docstring for Spider"""
	def __init__(self):
		self.page_num = 1
		self.total_num = None
		self.page_spider = page.Page()
		self.mysql = mysql.Mysql()
		
	def getCurrentTime(self):
		return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
		
	def getCurrentDate(self):
		return time.strftime('%Y-%m-%d',time.localtime(time.time()))

	#通过网页的页码数来构建网页的URL
	def getPageURLByNum(self, page_num):
	page_url = "http://iask.sina.com.cn/c/187-all-%s-new.html" % str(page_num)
	return page_url

	#通过传入网页页码来获取网页的HTML
	def getPageByNum(self,page_num):
		request = urllib2.Request(self.getPageURLByNum(page_num))
		try:
			response = urllib2.urlopen(request)
		except urllib2.URLError,e:
			if hasattr(e, "code"):
				print self.getCurrentTime(),"获取页面失败,错误代号", e.code
				return None
			if hasattr(e, "reason"):
				print self.getCurrentTime(),"获取页面失败,原因", e.reason
				return None
		else:
			page =  response.read().decode("utf-8")
			return page
		

	def main(slef):
		f_handler = open('out.log','w')
		sys.stdout = f_handler
		page = open('page.txt','r')
		content = page.readline()
		start_page = int(content.strip()) -1
		page.close()
		print self.getCurrentTime(),'开始页码',start_page
		print self.getCurrentTime(),'爬虫正在启动，开始爬去爱问知识人问题'
		slef.total_num = self.getTotalPageNum()
		print self.getCurrentTime(),'获取到目录页面个数%d个' %self.total_num
		if not start_page:
			start_page = self.total_num
		for x in range(1,start_page):
			print self.getCurrentTime(),'正在抓取第%d个页面' %(start_page-x+1)
			try:
				self.getQuestions(start_page-x+1)
			except urllib2.URLError,e:
				if hasattr(e,'reason'):
					print self.getCurrentTime(),'某总页面内抓取或提取失败，错误原因', e.reason
			except Exception,e:
				print self.getCurrentTime(),'某总页面内抓取或提取失败，错误原因:',e 
			if start_page-x+1 < start_page:
				f = open('page.txt','w')
				f.write(str(start_page-x+1))
				print self.getCurrentTime(),'写入新页码',start_page-x+1
				f.close()




























