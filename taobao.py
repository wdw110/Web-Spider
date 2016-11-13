#encoding=utf-8

import re
import os
import urllib
import urllib2
import tool

class TBMM(object):
	"""docstring for TBMM"""
	def __init__(self):
		self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
		self.tool = tool.Tool()

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
			tmp = list(item)
			tmp[0] = 'https:' + tmp[0]
			tmp[1] = 'https:' + tmp[1]
			contents.append(tmp)
		return contents

	def getDetailPage(self,infoURL):
		print infoURL
		response = urllib2.urlopen(infoURL)
		return response.read().decode('gbk')

	#获取个人文字简介
	def getBrief(self,page):
		pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		result = re.search(pattern,page)
		return self.tool.replace(result.group(1))

	#获取页面所有图片
	def getAllImg(self,page):
		pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		content = re.search(pattern,page)
		patternImg = re.compile('<img.*?src="(.*?)"',re.S)
		images = re.findall(patternImg,content.group(1))
		return images

	#获取多张写真图片
	def saveImgs(self,images,name):
		number = 1
		print '发现%s共有%d张照片' %(name.encode('utf-8'),len(images))
		for imageURL in images:
			splitPath = imageURL.split('.')
			fTail = splitPath.pop()
			if len(fTail) > 3:
				fTail = 'jpg'
			fileName = name + '/' + str(number) + '.' + fTail
			self.saveImg(imageURL,fileName)
			number += 1

	#保存头像
	def saveIcon(self,iconURL,name):
		splitPath = iconURL.split('.')
		fTail = splitPath.pop()
		fileName = 'data/' + name + '/icon.' + fTail
		self.saveImg(iconURL,fileName)

	#保存个人简介
	def saveBrief(self,content,name):
		fileName = 'data/' + name + '/' + name + '.txt'
		f = open(fileName,'w+')
		print '正在保存的个人信息为%s' % name.encode('utf-8')
		f.write(content.encode('utf-8'))

	#传入图片地址，文件名，保存单张图片
	def saveImg(self,imageURL,fileName):
		u = urllib.urlopen(imageURL)
		data = u.read()
		f = open(fileName, 'wb')
		f.write(data)
		print u"正在悄悄保存她的一张图片为",fileName
		f.close()

	#创建新目录
	def mkdir(self,path):
		path = path.strip()
		isExists = os.path.exists(path)
		if not isExists:
			# 如果不存在则创建目录
			# 创建目录操作函数
			print '新建了名字叫做%s的文件夹' % path.strip('data/').encode('utf-8') 
			os.makedirs(path)
			return True
		else:
			# 如果目录存在则不创建，并提示目录已存在
			print '名为%s的文件夹已经创建成功' % path.strip('data/').encode('utf-8')
			return False

	#将一页淘宝MM的信息保存起来
	def savePageInfo(self,pageIndex):
		contents = self.getContents(pageIndex)
		for item in contents:
			#item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
			#个人详情页面的URL
			detailURL = item[0]
			#得到个人详情页面代码
			detailPage = self.getDetailPage(detailURL)
			#获取个人简介
			brief = self.getBrief(detailPage)
			#获取所有图片列表
			images = self.getAllImg(detailPage)
			self.mkdir('data/'+item[2])
			#保存个人简介
			self.saveBrief(brief,item[2])
			#保存头像
			self.saveIcon(item[1],item[2])
			#保存图片
			self.saveImgs(images,item[2])

	#传入起止页码，获取MM图片
	def savePagesInfo(self,start,end):
		for i in range(start,end+1):
			self.savePageInfo(i)

spider = TBMM()
spider.savePagesInfo(1,10)

