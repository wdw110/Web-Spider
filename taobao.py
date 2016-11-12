#encoding=utf-8

import re
import os
import urllib
import urllib2
#import tool

class TBMM(object):
	"""docstring for TBMM"""
	def __init__(self):
		self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
		#self.tool = tool.Tool()

	def getPage(self,pageIndex):
		url = self.siteURL + '?page=' + str(pageIndex)
		#print url 
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read().decode('gbk')

	def getContents(self,pageIndex):
		page = self.getPage(pageIndex)
		pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
		items = re.findall(pattern,page)
		contents = []
		for item in items:
			#print list(item)
			contents.append(list(item))
		return contents

	def getDetailPage(self,infoURL):
		response = urllib2.urlopen(infoURL)
		return response.read().decode('gbk')

	def getBrief(self,page):
		pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		result = re.search(pattern,page)
		return self.tool.replace(result.group(1))

	def getAllImg(self,page):
		pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		content = re.search(pattern,page)
		patternImg = re.compile('<img.*?src="(.*?)"',re.S)
		images = re.findall(patternImg,content.group(1))
		return images

	#传入图片地址，文件名，保存单张图片
	def saveImgs(self,images,name):
		number = 1
		print '发现%s共有%d张照片' %(name,len(images))
		for imageURL in images:
			splitPath = imageURL.split('.')
			fTail = splitPath.pop()
			if len(fTail) > 3:
				fTail = 'jpg'
			fileName = name + '/' + str(number) + '.' + fTail
			self.saveImg(imageURL,fileName)

	def saveBrief(self,content,name):
		fileName = name + '/' + name + '.txt'
		f = open(fileName,'w+')
		print '正在保存的个人信息为',fileName
		f.write(content.encode('utf-8'))

	#创建新目录
	def mkdir(self,path):
		path = path.strip()
		isExists = os.path.exists(path)
		if not isExists:
			# 如果不存在则创建目录
			# 创建目录操作函数
			os.makedirs(path)
			return True
		else:
			# 如果目录存在则不创建，并提示目录已存在
			return False

spider = TBMM()
spider.getContents(1)
































