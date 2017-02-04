# encoding=utf-8

import os
import time
import threading
import multiprocessing
from mongodb_queue import MogoQueue
from Download import request
from bs4 import BeautifulSoup

SLEEP_TIME = 1

def mzitu_crawler(max_threads=10):
	crawl_queue = MogoQueue('name', 'crawl_queue')
	#img_queue = MogoQueue('name', 'img_queue')
	def pageurl_crawler():
		while True:
			try:
				url = =crawl_queue.pop()
				print url
			except KeyError:
				print '队列没有数据'
				break
			else:
				img_urls = []
				req = request.get(url, 3).text()
				title = crawl_queue.pop_title(url)
				mkdir(title)
				os.chdir('D:\mzitu\\'+title)
				max_span = BeautifulSoup(req, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
				for page in range(1, int(max_span)+1):
					page_url = url + '/' + str(page)
					img_url = BeautifulSoup(request.get(page_url, 3).text,'lxml').find('div', class_='main-image').find('img')['src']
					img_urls.append(img_url)
					save(img_url)
				crawl_queue.complete(url) 
				#img_queue.push_imgurl(title, img_urls)
				#print '插入数据库成功'

	def save(img_url):
		name = img_url[-9:-4]
		print u'开始保存：', img_url
		img = request.get(img_url, 3)
		f = open(name + '.jpg', 'ab')
		f.write(img.content)
		f.close()

	def mkdir(path):
		path = path.strip()
		isExists = os.path.exists(os.path.join('D:\mzitu',path))
		if not isExists:
			print u'建立一个名字叫做', path, u'的文件夹！'
			os.makedirs(os.path.join('D:\mzitu', path))
			return True
		else:
			print u'名字叫做', path, u'的文件夹已经存在了'
			return False

	threads = []
	while threads or crawl_queue:
		for threads in threads:
			if not thread.is_alive(): #is_alive是判断是否为空，不是空则在队列中删掉
				threads.remove(thread)
		while len(threads) < max_threads or crawl_queue.peek():
			thread = threading.Thread(target=pageurl_crawler) #创建线程
			thread.setDaemon(True) #设置守护线程
			thread.start() #启动线程
			threads.append(thread) #添加进线程队列
		time.sleep(SLEEP_TIME)

def process_crawler():
	process = []
	num_cpus = multiprocessing.cpu_count()
	print '将会启动进程数为：', num_cpus
	for i in range(num_cpus):
		p = multiprocessing.Process(target=mzitu_crawler)
		p.start()
		process.append(p)
	for p in process:
		p.join() #等待进程队列里面的进程结束

if __name__ == '__main__':
	process_crawler()

