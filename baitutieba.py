#encoding=utf-8

import re
import urllib
import urllib2

#处理页面标签类
class Tool(object):
	"""docstring for Tool"""
	removeImg = re.compile('<img.*?| {7}|') #去除img标签，7位长空格
	removeAddr = re.compile('<a.*?>|</a>')  #删除超链接标签
	replaceLine = re.compile('<tr>|<div>|</div></p>') #把换行的标签换成\n
	replaceTD = re.compile('<td>')  #将表格制表符<td>替换为\t
	replacePara = re.compile('<p.*?>') #把段落开头换为\n加空两格
	replaceBR = re.compile('<br><br>|<br>') #将换行符或双换行符替换为\n
	removeExtraTag = re.compile('<.*?>')
	def replace(self,x):
		x = re.sub(self.removeImg,'',x)
		x = re.sub(self.removeAddr,'',x)
		x = re.sub(self.replaceLine,'\n',x)
		x = re.sub(self.replaceTD,'\t',x)
		x = re.sub(self.replacePara,'\n  ',x)
		x = re.sub(self.replaceBR,'\n',x)
		x = re.sub(self.removeExtraTag,'',x)
		return x.strip() #将前后多余的内容删除

#百度贴吧爬虫类
class BDTB(object):
	"""docstring for BDTB"""
	#初始化，传入基地址，是否只看楼主的参数
	def __init__(self,baseUrl,seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)
		self.tool = Tool()

	#传入页码，获取该页帖子的代码
	def getPage(self,pageNum):
		try:
			url = self.baseURL+self.seeLZ+'&pn='+str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			#print response.read()
			return response.read().decode('utf-8')
		except urllib2.URLError as e:
			if hasattr(e,'reason'):
				print u'链接百度贴吧失败，错误原因',e.reason
				return None

	#获取帖子标题
	def getTittle(self):
		page = self.getPage(1)
		pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>',re.S)
		result = re.search(pattern,page)
		if result:
			#print result.group(1) #测试输出
			return result.group(1).strip()
		else:
			return None

	#获取帖子一共有多少页
	def getPageNum(self):
		page = self.getPage(1)
		pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result = re.search(pattern,page)
		if result:
			#print result.group(1) #测试输出
			return result.group(1).strip()
		else:
			return None

	#获取每一层楼的内容，传入页面内容
	def getContent(self,page):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items = re.findall(pattern,page)
		floor = 1
		for item in items:
			print floor,u'楼-------------------------------------------------------------------------------------\
			-----------------------------------------------\n'
			print self.tool.replace(item)
			floor += 1
		

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
a=bdtb.getPage(1)
bdtb.getContent(a)


