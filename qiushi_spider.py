#encoding=utf-8

import re
import time
import thread
import urllib
import urllib2

#糗事百科爬虫类
class QSBK(object):
	"""docstring for QSBK"""
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20161111 Firefox/3.5.6'
		self.headers = {'User-Agent':self.user_agent}
		self.stories = [] 	#存放段子的变量，每一个元素是每一页的所有段子
		self.enable = False #存放程序是否运行的变量
	def getPage(self,pageIndex):
		"""传入每一页的索引获得页面代码"""
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			request = urllib2.Request(url,headers=self.headers) #构建请求的request
			response = urllib2.urlopen(request) #利用urlopen获取页面代码
			pageCode = response.read().decode('utf-8')
			return pageCode

		except urllib2.URLError, e:
			if hasattr(e,'reason'):
				print u'链接糗事百科失败，错误原因', e.reason
				return None

	def getPageItems(self,pageIndex):
		"""传入某一页代码，返回本也不带图片的段子列表"""
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print '页面加载失败....'
			return None
		pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
		items = re.findall(pattern,pageCode)
		pageStories = [] #用来存储每页的段子
		for item in items:
			haveImg = re.search('img',item[3])
			if not haveImg:
				replacBR = re.compile(compile('<br/>'))
				text = re.sub(replacBR,'\n',item[1])
				#itme[0]是一个段子的发布者，item[1]是内容，item[2]是发布时间，item[4]是点赞数
				pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[4].strip()])
		return pageStories

	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1

	def getOneStory(self,pageStories,page):
		"""调用该方法，每次敲回车打印输出一个段子"""
		for story in pageStories:
			in_put = raw_input()
			self.loadPage()
			if in_put == 'Q':
				self.enable = False
				return
			print u'第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s' %(page,story[0],story[2],story[3],story[1])

	def start(self):
		print u'正在读取糗事百科,按回车查看新段子,Q退出'
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories)>0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories,nowPage)
spider = QSBK()
spider.start()

