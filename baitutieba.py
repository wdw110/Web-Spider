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
	def __init__(self,baseUrl,seeLZ,floorTag=1):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)
		self.tool = Tool()
		self.file = None #全局file变量，文件写入操作对象
		self.floor = 1  #楼层标号，初始为1
		self.defaultTitle = u'百度贴吧' #默认的标题，如果没有成功获取到标题的话则会用这个标题
		self.floorTag = floorTag #是否写入楼分隔符的标记

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
	def getTittle(self,page):
		pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>',re.S)
		result = re.search(pattern,page)
		if result:
			#print result.group(1) #测试输出
			return result.group(1).strip()
		else:
			return None

	#获取帖子一共有多少页
	def getPageNum(self,page):
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
		contents = []
		for item in items:
			#将文本进行去除标签处理，同时在前后加入换行符
			content = '\n'+self.tool.replace(item)+'\n'
			contents.append(content.encode('utf-8'))
		return contents

	def setFileTitle(self,title):
		#如果标题不是为None，即成功获取标题
		if title is not None:
			self.file = open('data/'+title+'.txt','w+')
		else:
			self.file = open('data/'+self.defaultTitle+'.txt','w+')

	def writeData(self,contents):
		for item in contents:
			if self.floorTag == '1':
				floorLine = '\n' + str(self.floor) + u'--------------------------\
				---------------------------------------------------------------\n'
				self.file.write(floorLine)
			self.file.write(item)
			self.floor += 1

	def start(self):
		indexPage = self.getPage(1)
		pageNum = self.getPageNum(indexPage)
		title = self.getTittle(indexPage)
		self.setFileTitle(title)
		if pageNum == None:
			print u'URL已失效，请重试'
			return
		try:
			print '该贴共有%s页' %str(pageNum)
			for i in range(1,int(pageNum)+1):
				print '正在写入第%d页数据' %i
				page = self.getPage(i)
				contents = self.getContent(page)
				self.writeData(contents)
		except IOError as e: #出现写入异常
			print '写入异常，原因：' + e.massage
		finally:
			print '写入完成'

		
print u"请输入帖子代号"
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = BDTB(baseURL,seeLZ,floorTag)
bdtb.start()

